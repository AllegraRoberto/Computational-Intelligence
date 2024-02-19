from game import Player, Move
from clone_game import GameCloned as Game
import random
from copy import deepcopy

class MiniMaxPlayer(Player):
    def __init__(self, max_depth):
        super().__init__()
        self.player = None
        self.max_depth = max_depth

    def make_move(self, game: "Game") -> tuple[tuple[int, int], Move]:
        
        best_score = float("-inf")
        best_move = None
        current_player = game.get_current_player()
        self.player = current_player
        
        moves=get_possible_moves(game.get_board(), current_player)
        
        for move in moves:

            board = deepcopy(game.get_board())
            cloned_game = Game(board, game.get_current_player())
            cloned_game.move(move[0], move[1], current_player)

            score = self.minimax(cloned_game, self.max_depth, float("-inf"), float("inf"), False)

            if score > best_score:
                best_score = score
                best_move = move

        if best_move:
            return best_move
        else: 
            return random.choice(get_possible_moves(game.get_board(), current_player))

    def minimax(self, game, depth, alpha, beta, is_maximizing):
        
        end=game.check_winner()

        if depth == 0 or end != -1:
            return evaluate_game(game.get_board(), end, self.player)

        if is_maximizing:
            max_eval = float("-inf")
            for move in get_possible_moves(game.get_board(), self.player):
                
                cloned_game = game.clone()
                cloned_game.move(move[0], move[1], self.player)

                evaluation = self.minimax(cloned_game, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break

            return max_eval
        else:
            min_eval = float("inf")
            for move in get_possible_moves(game.get_board(), (self.player + 1) % 2):
                
                cloned_game = game.clone()
                cloned_game.move(move[0], move[1], (self.player + 1) % 2)

                evaluation = self.minimax(cloned_game, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

            return min_eval

def evaluate_game(board, end, player):
    
    sum = 0
    sum_tot = 0
    sum_opponent = 0
    sum_tmp = 0
    sum_tmp_opponent = 0
    sum_tmp_1 = 0
    sum_tmp_1_opponent = 0
    sum_tmp_2 = 0
    sum_tmp_2_opponent = 0
    board_size = 5
    
    if end == -1:
        sum = 0
 
        for y in range(0, board_size):
            for x in range(0, board_size):
                if board[x][y] == player:
                    sum_tmp_1 += 1
                    sum_tot += 1
                elif board[x][y] == (player + 1) % 2:
                    sum_tmp_1_opponent += 1
                if board[y][x] == player:
                    sum_tmp_2 += 1
                    sum_tot += 1
                elif board[y][x] == (player + 1) % 2:
                    sum_tmp_2_opponent += 1
            if sum_tmp_1 > sum:
                sum_opponent = sum_tmp_1
            elif sum_tmp_1_opponent > sum_opponent:
                sum_opponent = sum_tmp_1_opponent
            if sum_tmp_2 > sum:
                sum = sum_tmp_2
            elif sum_tmp_2_opponent > sum_opponent:
                sum_opponent = sum_tmp_2_opponent
            sum_tmp_1 = sum_tmp_2 = sum_tmp_1_opponent = sum_tmp_2_opponent = 0

        x = y = 0
        while x < 5 and y < 5:
            if board[x][y]==player:
                sum_tmp += 1
                sum_tot += 1
            elif board[x][y] == (player + 1) % 2:
                sum_tmp_opponent += 1
            x += 1
            y += 1
        if sum_tmp > sum:
            sum = sum_tmp
        elif sum_tmp_opponent > sum_opponent:
            sum_opponent = sum_tmp_opponent
        sum_tmp = 0  
        sum_tmp_opponent = 0

        x = 4
        y = 0
        while x >= 0 and y < 5:
            if board[x][y]==player:
                sum_tmp += 1
                sum_tot += 1
            elif board[x][y] == (player + 1) % 2:
                sum_tmp_opponent += 1
            x -= 1
            y += 1
        if sum_tmp > sum:
            sum = sum_tmp
        elif sum_tmp_opponent > sum_opponent:
            sum_opponent = sum_tmp_opponent
            
        return sum + (sum - sum_opponent) + (sum_tot * 0.5)
    
    elif end == player:
        return 30
    else:
        return -30

def get_possible_moves(board, player, board_size=5):
    
    moves = []

    for y in [0, board_size - 1]:
        for x in range(0, board_size):
            if x == 0 and y == 0 and (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.RIGHT))
                moves.append(((x, y), Move.BOTTOM))
            elif x == 0 and y == board_size - 1 and (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.RIGHT))
                moves.append(((x, y), Move.TOP))
            elif x == board_size - 1 and y == 0 and (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.BOTTOM))
                moves.append(((x, y), Move.LEFT))
            elif x == board_size - 1 and y == board_size - 1 and (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.TOP))
                moves.append(((x, y), Move.LEFT))
            elif y == 0 and (board[y][x] == player or board[y][x] == -1):
                    moves.append(((x, y), Move.RIGHT))
                    moves.append(((x, y), Move.LEFT))
                    moves.append(((x, y), Move.BOTTOM))
            elif y == board_size - 1 and (board[y][x] == player or board[y][x] == -1):
                    moves.append(((x, y), Move.RIGHT))
                    moves.append(((x, y), Move.LEFT))
                    moves.append(((x, y), Move.TOP))

    for x in [0, board_size - 1]:
        for y in range(1, board_size - 1):
            if (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.TOP))
                moves.append(((x, y), Move.BOTTOM))
            if x == 0  and (board[y][x] == player or board[y][x] == -1):
                moves.append(((x, y), Move.RIGHT))
            elif (board[y][x] == player or board[y][x] == -1):
                    moves.append(((x, y), Move.LEFT))
    
    return moves