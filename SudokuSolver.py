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

# Function to print the Sudoku board
def print_board(board):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):

    empty_position = find_empty(board)
    if empty_position is None:
        return print_board(board) # No more empty positions, puzzle solved

    row, col = empty_position

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Solution found

            board[row][col] = 0  # Backtrack if no solution

# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(board)
