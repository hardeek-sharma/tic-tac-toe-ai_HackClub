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


board = new_board()

board[0][2] = "X"
board[2][1] = "O"

render(board)
