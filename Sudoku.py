# Function to check if a number can be placed on the board
def is_valid(board, row, col, num):
    # Check if num is not in the given row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is not in the given column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if num is not in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to find an empty position (represented by 0)
def find_empty(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
