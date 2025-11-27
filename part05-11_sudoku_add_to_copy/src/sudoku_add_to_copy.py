# Write your solution here
def print_sudoku(sudoku: list):
    count = 0
    row_count = 0
    for row in sudoku:
        for num in row:
            if num == 0:
                print(f"_ ", end="")
            else:
                print(f"{num} ", end="")
            
            count += 1
            
            if count == 3:
                print(" ", end="")
                count = 0

        print()

        row_count += 1
        if row_count == 3:
            print(" ")
            row_count = 0
            

def copy_and_add(sudoku: list, row_num: int, col_num: int, number: int):
    grid_copy = [row[:] for row in sudoku]
    grid_copy[row_num][col_num] = number

    return grid_copy

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)