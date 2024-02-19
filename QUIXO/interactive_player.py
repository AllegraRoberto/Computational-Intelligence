from game import Game, Move, Player

class InteractivePlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.player = None

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        slide = None
        current_player = game.get_current_player()
        board = game.get_board()
        self.player = current_player
        moves = self.get_legal_moves(board, current_player)
        accettable = 0
        while accettable == 0:
            x=str(input("Insert coordinate x of your move:"))
            from_pos_x = int(x)
            y=str(input("Insert coordinate y of your move:"))
            from_pos_y = int(y)
            move = str(input("Insert slide of your move:"))
            match move.upper():
                case("TOP"): slide = Move.TOP
                case("BOTTOM"): slide = Move.BOTTOM
                case("LEFT"): slide = Move.LEFT
                case("RIGHT"): slide = Move.RIGHT

            if ((from_pos_x, from_pos_y), slide) in moves:
                accettable = 1
            else:
                print("Move not valid")

        return ((from_pos_x, from_pos_y), slide)
    
    def get_legal_moves(self, board, player):
        board_size=5
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
                else:
                    if (board[y][x] == player or board[y][x] == -1):
                        moves.append(((x, y), Move.LEFT))
        
        return moves
