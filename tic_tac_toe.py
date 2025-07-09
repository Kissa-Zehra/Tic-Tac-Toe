board = [str(i) for i in range(1, 10)]

current_player = "X"

game_is_still_going = True

# --- Functions ---

def display_board():
    """Prints the current state of the game board."""
    print("\n" + "Tic-Tac-Toe")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-----------")

def handle_turn():
    """Gets input from the current player and updates the board."""
    global current_player
    
    print(f"\nPlayer {current_player}'s turn.")
    position = input("Choose a position from 1-9: ")

    while True:
        if not position.isdigit() or int(position) not in range(1, 10):
            position = input("Invalid input. Please choose a number from 1-9: ")
            continue
        
        position = int(position) - 1
        
        if board[position] == "X" or board[position] == "O":
            position = input("That position is already taken. Choose a different one: ")
        else:
            break  

    board[int(position)] = current_player

def check_if_game_over():
    """Checks for a win or a tie and updates the game status."""
    check_for_winner()
    check_if_tie()

def check_for_winner():
    """Checks all win conditions (rows, columns, diagonals)."""
    global game_is_still_going

    # --- Check Rows ---
    row_1 = board[0] == board[1] == board[2] != str(1) 
    row_2 = board[3] == board[4] == board[5] != str(4)
    row_3 = board[6] == board[7] == board[8] != str(7)
    
    # --- Check Columns ---
    col_1 = board[0] == board[3] == board[6] != str(1)
    col_2 = board[1] == board[4] == board[7] != str(2)
    col_3 = board[2] == board[5] == board[8] != str(3)
    
    # --- Check Diagonals ---
    diag_1 = board[0] == board[4] == board[8] != str(1)
    diag_2 = board[2] == board[4] == board[6] != str(3)

    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or diag_1 or diag_2:
        game_is_still_going = False
        display_board()
        print(f"\nCongratulations! Player {current_player} wins!")
        return

def check_if_tie():
    """Checks if all positions are filled and there is no winner."""
    global game_is_still_going
    
    is_full = all(spot in ["X", "O"] for spot in board)
    
    if is_full and game_is_still_going:
        game_is_still_going = False
        display_board()
        print("\nIt's a tie!")
        return

def flip_player():
    """Switches the turn to the other player."""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def play_game():
    """The main function that orchestrates the entire game."""
    global board, current_player, game_is_still_going
    
    while True: 
        # --- Reset game state for a new game ---
        board = [str(i) for i in range(1, 10)]
        current_player = "X"
        game_is_still_going = True
        
        # --- Gameplay Loop for a single game ---
        while game_is_still_going:
            display_board()
            handle_turn()
            check_if_game_over()
            flip_player()
        
        # --- Ask to play again ---
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# --- Start the Game ---
if __name__ == "__main__":
    play_game()
