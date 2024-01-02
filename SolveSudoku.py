board = [
    [0,0,0,0,0,3,8,0,7],
    [0,0,3,8,0,0,0,0,9],
    [0,0,0,9,0,1,0,0,0],
    [0,0,2,5,0,9,0,0,0],
    [1,0,7,0,0,2,0,0,4],
    [0,9,0,1,0,0,0,0,6],
    [0,0,0,0,0,0,4,6,0],
    [0,0,1,0,0,0,0,0,8],
    [7,4,0,0,0,0,2,0,1]
]


def visualize_board(board):
    for line in range(len(board)):
        if line % 3 == 0 and line != 0: # dotted line every 3 rows
            print("- - - - - - - - - - - -")
        for column in range(len(board[line])): # num is also column index
            if column % 3 == 0 and column != 0:
                print(" | ", end="") # divider every 3 columns
            if column == 8:
                print(board[line][column]) # number with newline character
            else:
                print(str(board[line][column]) + " ", end="") # number with no newline character

def empty_cell(board):
    for line in range(len(board)):
        for column in range(len(board[line])):
            if board[line][column] == 0:
                return (line, column) # row number, column number
    return None

"""
Given these parameters, we want to check if the number is already in the row or in the column or in the box.
The parameter 'position' will be the tuple returned from empty_cell(board).
"""

def check_valid(board, number, position): # board, number we want to check, location out of 81 squares we want to check
    (row, column) = position # (y, x)
    for col in range(len(board[row])): # checks the row
        if board[row][col] == number:
            return False
    for line in range(len(board)): # checks the column
        if board[line][column] == number:
            return False
    # divide the grid into groups of 3x3 grids, creating 9 3x3 grids
    grid_x = column // 3
    grid_y = row // 3
    # determine from (0,0) to (3,3), which 3x3 grid we are in
    for i in range(grid_x * 3, grid_x * 3 + 3): # column we are in
        for j in range(grid_y * 3, grid_y * 3 + 3): # row we are in
            if board[j][i] == number:
                return False
    return True

def solve_sudoku(board):
    cell = empty_cell(board)
    if cell == None: # if there are no more cells to fill in, solve_sudoku(board) == True. This is our base case
        return True
    else:
        for i in range(1, 10):
            if check_valid(board, i, cell): # checking: can we put i into the cell?
                board[cell[0]][cell[1]] = i # puts i into cell
                if solve_sudoku(board) == True: # if the cells are all full, solve_sudoku(board) == True
                    return True
                else: # when we find that our solution wont work, we reset to the cell that was last valid
                    board[cell[0]][cell[1]] = 0 
    return False

visualize_board(board)
solve_sudoku(board)
print("\n SOLVED PUZZLE BELOW \n")
visualize_board(board)

"""
    for line in range(len(board)): # checks the row
        if line == row: # check if the row is the row we want
            for num in range(len(board[line])): # iterate through the numbers on the line
                if board[line][num] == number and board[line][num] != 0:
                    return False
    # iterate through every row ON the exact same index, ranging from 0 to 8
    for line in range(len(board)):
        for num in range(0, 9):
            if num == column: # checks if the column is the column we want
                if board[line][num] == number and board[line][num] != 0:
                    return False
"""