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
            

def add_number(sudoku: list, row_num: int, col_num: int, number: int):
    sudoku[row_num][col_num] = number

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
    

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)