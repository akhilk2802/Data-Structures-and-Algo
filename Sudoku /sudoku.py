def solve(grid):
    empty_cell = find_next(grid)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for num in range(1, 7):
        if check_placement(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False  


def find_next(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return row, col
    return None


def check_placement(grid, row, col, num):
    # Check row and column for the number
    for i in range(6):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check the 3x2 rectangle for the number
    start_row, start_col = 2 * (row // 2), 3 * (col // 3)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


sudoku = [
    [0, 0, 4, 0, 0, 0],
    [3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0],
    [6, 0, 0, 0, 1, 4],
    [0, 2, 0, 0, 0, 6]
]

if solve(sudoku):
    for row in sudoku:
        print(row)
else:
    print("Unsolvable")

