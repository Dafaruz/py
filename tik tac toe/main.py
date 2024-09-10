# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    return ' ' not in board

# Function to play the Tic Tac Toe game
def play_game():
    board = [' ' for _ in range(9)]  # Initialize the board
    current_player = 'X'  # Player X goes first

    while True:
        print_board(board)  # Display the current state of the board
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1

        # Check if the move is valid
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_game()
