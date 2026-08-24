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


if __name__ == '__main__':
    player1 = "X"
    player2 = "O"
    current_player = player1

    board = new_board()

    while True:
        print("---------------")
        print(f"Player '{current_player}' turn")
        print("---------------")

        render(board)

        move_coords = None
        while True:
            move_coords = get_move()
            if is_valid_move(board, move_coords):
                break
            else:
                print("Invalid move, try again")

        board = make_move(board, move_coords, current_player)

        current_player = player2 if current_player == player1 else player1
