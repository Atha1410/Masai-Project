import os

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return all(cell != " " for cell in board)

def save_game(board, current_player):
    with open("game_state.txt", "w") as file:
        file.write("".join(board) + "\n")
        file.write(current_player)

def load_game():
    if os.path.exists("game_state.txt"):
        with open("game_state.txt", "r") as file:
            board = list(file.readline().strip())
            current_player = file.readline().strip()
        return board, current_player
    return [" "] * 9, "X"

def main():
    print("Welcome to Tic Tac Toe!")
    board, current_player = load_game()

    while True:
        display_board(board)
        print(f"{current_player}'s turn")
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                if check_winner(board, current_player):
                    display_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
        
        save_game(board, current_player)

    if os.path.exists("game_state.txt"):
        os.remove("game_state.txt")
    print("Game over!")

if __name__ == "__main__":
    main()
