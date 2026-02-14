def display_board(board):
    print(board[0][0], board[0][1], board[0][2], sep=" | ")
    print("--+---+--")
    print(board[1][0], board[1][1], board[1][2], sep=" | ")
    print("--+---+--")
    print(board[2][0], board[2][1], board[2][2], sep=" | ")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return True
        
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    
    if board[0][2] == board[1][1] == board[2][0]:
        return True

def check_draw(move_counter):
    return move_counter >= 9

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

end_game = False
sign = "X"
move_counter = 0

print("\nWelcome to Tic Tac Toe\n")
display_board(board)

while not end_game:
    player_input = input(f"\nEnter the number of your place in board (player {sign}'s turn): ")

    if player_input.isnumeric() == False:
        print("Invalid number! Please enter a number between 1-9.")
        continue

    player_num = int(player_input)

    if player_num > 9 or player_num <= 0:
        print("Invalid number! Please enter a number between 1-9.")
        continue

    i = (player_num - 1) // 3
    j = (player_num - 1) % 3

    if board[i][j] == "X" or board[i][j] == "O":
        print("This cell is already occupied! Please choose another one.")
        continue

    board[i][j] = sign
    move_counter += 1

    display_board(board)

    if check_win(board):
        print(f"\nPlayer {sign} wins!")
        end_game = True

    elif check_draw(move_counter):
        print("\nIt's a draw!")
        end_game = True
        
    if sign == "X":
        sign = "O"
    else:
        sign = "X"
