RED = "\033[31m"
RESET = "\033[0m"

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
    x = None
    y = None

    while True:
        try:
            x = int(input("What is your move's X co-ordinate?: "))
            if x > 2 or x < 0:
                print(f"{RED} Number has to be between 0-2 {RESET}")
                continue

            y = int(input("What is your move's Y co-ordinate?: "))
            if y > 2 or y < 0:
                print(f"{RED} Number has to between 0-2 {RESET}")
                continue
            else:
                break

        except ValueError:
            print(f"{RED} Enter a NUMBER {RESET}")
            continue

    return x, y


def make_move(init_board, cords, symbol):
    temp_board = init_board
    x, y = cords

    temp_board[y][x] = symbol

    return temp_board


def is_valid_move(init_board, cords):
    return init_board[cords[1]][cords[0]] is None


def get_winner(init_board):
    # Rows
    for row in init_board:
        if set(row) == 1:
            return row[0]

    # Columns
    if len({init_board[0][0], init_board[1][0], init_board[2][0]}) == 1:
        return init_board[0][0]

    if len({init_board[0][1], init_board[1][1], init_board[2][1]}) == 1:
        return init_board[0][1]

    if len({init_board[0][2], init_board[1][2], init_board[2][2]}) == 1:
        return init_board[0][2]

    # Diagonals
    if len({init_board[0][0], init_board[1][1], init_board[2][2]}) == 1:
        return init_board[0][0]

    if len({init_board[0][2], init_board[1][1], init_board[0][2]}) == 1:
        return init_board[0][2]

    return None


def check_draw(init_board):
    for row in init_board:
        for space in row:
            if space is None:
                return False
    return True


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
                print(f"{RED} Invalid move, try again {RESET}")

        board = make_move(board, move_coords, current_player)

        current_player = player2 if current_player == player1 else player1

        winner = get_winner(board)
        if winner is not None:
            print(f"Player {winner} Won!!!")
            break

        if check_draw(board):
            print("Game Over")
            print("Draw")
            break
