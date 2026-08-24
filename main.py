def new_board():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def render(init_board):
    print("    0 1 2")
    print("  ---------")
    for i in range(3):
        print(f"{i} | ", end="")
        for j in range(3):
            if init_board[i][j] is None:
                print(" ", end="")
            else:
                print(init_board[i][j], end="")

            print(" ", end="")
        print("|")
    print("  ---------")


def get_move():
    x = int(input("What is your move's X co-ordinate?: "))
    y = int(input("What is your move's Y co-ordinate?: "))

    return x, y


def make_move(init_board, cords, symbol):
    temp_board = init_board
    x, y = cords

    temp_board[y][x] = symbol

    return temp_board


def is_valid_move(init_board, cords):
    return init_board[cords[1]][cords[0]] is None


board = new_board()
board[0][0] = "X"

move_coords = None
while True:
    move_coords = get_move()
    if is_valid_move(board, move_coords):
        break
    else:
        print("Invalid move, try again")

