"""
project_2.py: second project for Engeto Online Python Academy

author: Michal Kolar
email: kobracz.mkgmail.com
"""

def create_game_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_game_board(board):
    separator = "\t+---+---+---+"  
    print(separator)
    for i, row in enumerate(board):
        print("\t| " + " | ".join(row) + " |")
        if i < 2:
            print(separator)
    print(separator)

def is_winner(board, player):
    for x in range(3):
        if all(board[x][y] == player for y in range(3)) or all(board[y][x] == player for y in range(3)):
            return True
    if all(board[x][x] == player for x in range(3)) or all(board[x][2 - x] == player for x in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[x][y] != " " for x in range(3) for y in range(3))

def get_move(player, board):
    position_mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
    }
    
    while True:
        print("========================================")
        try:
            move = int(input(f"Player {player.lower()} | Enter field number (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input! Enter a number between 1 and 9.")
                continue

            x, y = position_mapping[move]
            if board[x][y] != " ":
                print("This field is already occupied, try another one!")
                continue
            return x, y
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def tic_tac_toe():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game\n")
    
    player_1 = input("Enter player X name: ")
    player_2 = input("Enter player O name: ")

    score = {player_1: 0, player_2: 0}
    while True:
        board = create_game_board()
        player = player_1
        while True:
            display_game_board(board)
            x, y = get_move(player, board)
            board[x][y] = "X" if player == player_1 else "O"
            if is_winner(board, "X" if player == player_1 else "O"):
                display_game_board(board)
                print(f"============================================")
                print(f"Congratulations, the player {player.lower()} WON!")
                print(f"============================================")
                score[player] += 1
                break
            if is_draw(board):
                display_game_board(board)
                print("It's a draw!")
                break
            player = player_2 if player == player_1 else player_1
        print(f"Score: {player_1} - {score[player_1]}, {player_2} - {score[player_2]}")
        if input("Do you want to play again? Otherwise, the program will exit. (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    tic_tac_toe()
