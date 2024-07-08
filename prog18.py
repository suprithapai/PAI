Row = int(input("Enter the number of rows: "))
Coloumn = int(input("Enter the number of columns: "))
matrix = []
print("Enter the entries row-wise (separate each number with a space):")

for row in range(Row):
    while True:
        a = list(map(int, input().split()))
        if len(a) == Coloumn:
            matrix.append(a)
            break
        else:
            print(f"Error: Please enter exactly {Coloumn} numbers.")

for row in range(Row):
    for coloumn in range(Coloumn):
        print(matrix[row][coloumn], end=" ")
    print()

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied, try again.")
            continue
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()



