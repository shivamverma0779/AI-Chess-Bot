import chess
import random

# Define evaluation charts here
pawn_chart = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knight_chart = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishops_chart = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rooks_chart = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queens_chart = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

kings_chart = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]




class group1:
    def __init__(self, color):
        self.color = color

    def evaluate_board(self, board):
        if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999
        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0

        pw = len(board.pieces(chess.PAWN, chess.WHITE))
        pb = len(board.pieces(chess.PAWN, chess.BLACK))
        nw = len(board.pieces(chess.KNIGHT, chess.WHITE))
        nb = len(board.pieces(chess.KNIGHT, chess.BLACK))
        bw = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))
        rw = len(board.pieces(chess.ROOK, chess.WHITE))
        rb = len(board.pieces(chess.ROOK, chess.BLACK))
        qw = len(board.pieces(chess.QUEEN, chess.WHITE))
        qb = len(board.pieces(chess.QUEEN, chess.BLACK))

        material = 100 * (pw - pb) + 320 * (nw - nb) + 330 * (bw - bb) + 500 * (rw - rb) + 900 * (qw - qb)

        pawnsq = sum([pawn_chart[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
        pawnsq = pawnsq + sum([-pawn_chart[chess.square_mirror(i)]
                               for i in board.pieces(chess.PAWN, chess.BLACK)])
        knightsq = sum([knight_chart[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
        knightsq = knightsq + sum([-knight_chart[chess.square_mirror(i)]
                                   for i in board.pieces(chess.KNIGHT, chess.BLACK)])
        bishopsq = sum([bishops_chart[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
        bishopsq = bishopsq + sum([-bishops_chart[chess.square_mirror(i)]
                                   for i in board.pieces(chess.BISHOP, chess.BLACK)])
        rooksq = sum([rooks_chart[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
        rooksq = rooksq + sum([-rooks_chart[chess.square_mirror(i)]
                               for i in board.pieces(chess.ROOK, chess.BLACK)])
        queensq = sum([queens_chart[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
        queensq = queensq + sum([-queens_chart[chess.square_mirror(i)]
                                 for i in board.pieces(chess.QUEEN, chess.BLACK)])
        kingsq = sum([kings_chart[i] for i in board.pieces(chess.KING, chess.WHITE)])
        kingsq = kingsq + sum([-kings_chart[chess.square_mirror(i)]
                               for i in board.pieces(chess.KING, chess.BLACK)])

        eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq

        if self.color == "white":
            eval = -eval

        return eval



    def select_move(self, board):
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in board.legal_moves:
            board.push(move)
            board_value = -self.alphabeta(-beta, -alpha, 2, board)
            board.pop()

            if board_value > best_value:
                best_value = board_value
                best_move = move
            alpha = max(alpha, board_value)

        return best_move

    def alphabeta(self, alpha, beta, depthleft, board):
        if depthleft == 0:
            return self.quiesce(alpha, beta, board)

        for move in board.legal_moves:
            board.push(move)
            score = -self.alphabeta(-beta, -alpha, depthleft - 1, board)
            board.pop()

            alpha = max(alpha, score)
            if alpha >= beta:
                return alpha  # Beta cutoff
        return alpha

    def quiesce(self, alpha, beta, board):
        stand_pat = self.evaluate_board(board)
        if stand_pat >= beta:
            return beta
        if alpha < stand_pat:
            alpha = stand_pat

        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                score = -self.quiesce(-beta, -alpha, board)
                board.pop()

                alpha = max(alpha, score)
                if alpha >= beta:
                    return alpha  # Beta cutoff
        return alpha



    def makemove(self, board):
        bot_move = self.select_move(board)
        return bot_move.uci() if bot_move else None
