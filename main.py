import random

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


def human_player(init_board, symbol):
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
    x = cords[0]
    y = cords[1]
    # x, y = cords

    temp_board[y][x] = symbol

    return temp_board


def is_valid_move(init_board, cords):
    return init_board[cords[1]][cords[0]] is None


def get_winner(init_board):
    # Rows
    for row in init_board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]

    # Columns
    if len({init_board[0][0], init_board[1][0], init_board[2][0]}) == 1 and init_board[0][0] is not None:
        return init_board[0][0]

    if len({init_board[0][1], init_board[1][1], init_board[2][1]}) == 1 and init_board[0][1] is not None:
        return init_board[0][1]

    if len({init_board[0][2], init_board[1][2], init_board[2][2]}) == 1 and init_board[0][2] is not None:
        return init_board[0][2]

    # Diagonals
    if len({init_board[0][0], init_board[1][1], init_board[2][2]}) == 1 and init_board[0][0] is not None:
        return init_board[0][0]

    if len({init_board[0][2], init_board[1][1], init_board[2][0]}) == 1 and init_board[0][2] is not None:
        return init_board[0][2]

    return None


def check_draw(init_board):
    for row in init_board:
        for space in row:
            if space is None:
                return False
    return True


def get_legal_moves(init_board):
    legal_moves = []
    for r_indx, row in enumerate(init_board):
        for c_indx, space in enumerate(row):
            if space is None:
                legal_moves.append((c_indx, r_indx))
    return legal_moves


def random_ai(init_board, symbol):
    return random.choice(get_legal_moves(init_board))


def find_winning_move(init_board, symbol):
    legal_moves = get_legal_moves(init_board)
    print(legal_moves)

    for x, y in legal_moves:
        init_board = make_move(init_board, (x, y), symbol)
        if get_winner(init_board) == symbol:
            init_board[y][x] = None
            return x, y

        init_board[y][x] = None

    return None


def find_losing_move(init_board, symbol):
    symbol = player1 if symbol == player2 else player2
    legal_moves = get_legal_moves(init_board)
    print(legal_moves)

    for x, y in legal_moves:
        init_board = make_move(init_board, (x, y), symbol)
        if get_winner(init_board) == symbol:
            init_board[y][x] = None
            return x, y

        init_board[y][x] = None

    return None


def finds_winning_moves_ai(init_board, symbol):
    winning_move = find_winning_move(init_board, symbol)
    if winning_move:
        return winning_move
    return random_ai(init_board, symbol)


def finds_winning_and_losing_moves_ai(init_board, symbol):
    winning_move = find_winning_move(init_board, symbol)
    if winning_move:
        return winning_move

    losing_move = find_losing_move(init_board, symbol)
    if losing_move:
        return losing_move

    return random_ai(init_board, symbol)


if __name__ == '__main__':
    player1 = "X"
    player2 = "O"
    current_player = player1

    board = new_board()

    while True:
        print("***************")
        print(f"Player '{current_player}' turn")
        print("---------------")

        render(board)

        move_coords = None
        while True:
            # move_coords = human_player(board, current_player)
            # move_coords = random_ai(board, current_player)
            # move_coords = finds_winning_moves_ai(board, current_player)
            move_coords = finds_winning_and_losing_moves_ai(board, current_player)
            if is_valid_move(board, move_coords):
                break
            else:
                print(f"{RED} Invalid move, try again {RESET}")

        board = make_move(board, move_coords, current_player)
        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"Player {winner} Won!!!")
            break

        if check_draw(board):
            render(board)
            print("Game Over")
            print("Draw")
            break

        current_player = player2 if current_player == player1 else player1
