import math

# Creating the board
board = [" " for _ in range(9)]


# Function to print the board
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# Function to check winner
def check_winner(player):

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player
        ):
            return True

    return False


# Function to check draw
def check_draw():
    return " " not in board


# Function for player move
def player_move():

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = "X"
                break

            else:
                print("Invalid move. Try again.")

        except:
            print("Please enter a valid number.")


# Minimax algorithm
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if check_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


# AI move function
def ai_move():

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main game function
def play_game():

    print("===================================")
    print("        Tic-Tac-Toe AI")
    print("===================================")
    print("You are X")
    print("AI is O")
    print("Positions are from 1 to 9\n")

    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:

        print_board()

        # Player turn
        player_move()

        if check_winner("X"):
            print_board()
            print("Congratulations! You won!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # AI turn
        print("AI is making a move...\n")

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break


# Start game
play_game()