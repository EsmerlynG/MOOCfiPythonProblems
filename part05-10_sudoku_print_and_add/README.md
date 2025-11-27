# Sudoku Grid Functions

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

Two Python functions that handle Sudoku grid visualization and modification: `print_sudoku` for formatted grid display and `add_number` for placing values. This solution demonstrates 2D array manipulation, formatted output control, and modular function design.

---

## 📖 Problem Description

Complete two functions for a Sudoku project:

1. **`print_sudoku(sudoku: list)`** - Displays a 9×9 Sudoku grid with proper formatting
2. **`add_number(sudoku: list, row_no: int, column_no: int, number: int)`** - Places a digit in the specified grid location

### Requirements
- Display empty cells as underscores (`_`)
- Group columns in sets of 3 with extra spacing
- Group rows in sets of 3 with blank lines
- Modify the grid in-place when adding numbers
- Handle 9×9 two-dimensional arrays

### Example Output Format
```
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
```

---

## 💻 Code Implementation

```python
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
    sudoku = [
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
```

**Output:**
```
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Three numbers added:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
```

---

## 🧠 Algorithm Explanation

### **`print_sudoku` Function**
1. **Row Iteration**: Loop through each row in the 9×9 grid
2. **Cell Processing**: Check if cell is empty (0) or contains a number
3. **Column Spacing**: Add extra space after every 3rd column using `count` tracker
4. **Row Spacing**: Add blank line after every 3rd row using `row_count` tracker
5. **Formatted Output**: Use `end=""` parameter to control line breaks

### **`add_number` Function**
1. **Direct Assignment**: Simply assign the number to the specified grid position
2. **In-Place Modification**: Changes the original grid structure

**Time Complexity:** 
- `print_sudoku`: O(81) = O(1) - Always processes 81 cells
- `add_number`: O(1) - Single assignment operation

**Space Complexity:** O(1) - No additional data structures needed

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 sudoku_grid.py
```

Or import the functions in your own code:

```python
from sudoku_grid import print_sudoku, add_number

# Create empty grid
grid = [[0 for _ in range(9)] for _ in range(9)]

# Add some numbers
add_number(grid, 0, 0, 5)
add_number(grid, 4, 4, 9)

# Display the grid
print_sudoku(grid)
```

---

## 🧪 Test Cases

```python
# Test case 1: Empty grid
empty_grid = [[0 for _ in range(9)] for _ in range(9)]
print("Empty Grid:")
print_sudoku(empty_grid)

# Test case 2: Add numbers to different positions
add_number(empty_grid, 0, 8, 1)  # Top-right corner
add_number(empty_grid, 8, 0, 9)  # Bottom-left corner
add_number(empty_grid, 4, 4, 5)  # Center
print("\nThree numbers added:")
print_sudoku(empty_grid)

# Test case 3: Partially filled grid
partial_grid = [
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
print("\nPartially Filled Grid:")
print_sudoku(partial_grid)

# Test case 4: Overwrite existing number
add_number(partial_grid, 0, 0, 1)  # Change 5 to 1
print("\nAfter modification:")
print_sudoku(partial_grid)
```

---

## ✨ Key Learning Highlights

This problem introduced important concepts in **output formatting** and **2D array manipulation**:

### **Advanced Print Control**
```python
print(f"_ ", end="")  # Print without newline
print(" ", end="")    # Add spacing
print()               # Just a newline
```
- **Discovery**: The `end=""` parameter allows precise output control
- **Application**: Essential for creating structured, formatted displays
- **Benefits**: Complete control over spacing and line breaks

### **Counter-Based Formatting**
```python
count += 1
if count == 3:
    print(" ", end="")
    count = 0
```
- **Pattern**: Use counters to track position within patterns
- **Implementation**: Reset counters at pattern boundaries
- **Result**: Clean, organized grid structure

### **In-Place Modification**
- **Goal**: Modify existing data structures rather than creating new ones
- **Implementation**: Direct assignment to list indices
- **Best Practice**: Simple, efficient operations for data updates

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Clear Separation**: Two distinct functions with single responsibilities
2. **Counter Logic**: Simple tracking for pattern-based formatting
3. **Direct Modification**: Efficient in-place updates
4. **Readable Output**: Visual structure matches Sudoku conventions

### **Clean Code Principles Applied**
- **Single Responsibility**: Each function has one clear purpose
- **Descriptive Logic**: Counter variables make formatting intentions clear
- **Minimal Complexity**: Straightforward loops without over-engineering

---

## 🔄 Code Structure Analysis

### **`print_sudoku` Breakdown**
- **Outer Loop**: Iterate through rows
- **Inner Loop**: Process each cell in the row
- **Column Counter**: Track position for spacing (every 3 columns)
- **Row Counter**: Track position for blank lines (every 3 rows)
- **Conditional Display**: Show `_` for zeros, numbers for values

### **`add_number` Simplicity**
- **Single Line**: Direct assignment to 2D array position
- **Parameter Mapping**: Clear correspondence between function args and grid coordinates

---

## 🎓 Learning Outcomes

* **Print Control Mastery**: Understanding `end=""` parameter for custom formatting
* **2D Array Manipulation**: Efficient access and modification of grid structures
* **Counter-Based Logic**: Using simple counters for pattern recognition
* **Output Formatting**: Creating visually structured displays
* **Modular Design**: Building focused functions that work together
* **Grid Visualization**: Translating data structures into readable formats

---

## 💡 Developer Reflection

> *"This was a fairly difficult problem for me at first. I was initially too hung up on how I was going to add the desired number into the correct location. I overcomplicated things by thinking I had to create a new board every time I added a number—but that wasn't the case.*
> 
> *After taking a step back and breathing, I realized that I was first adding the number into the matrix and then creating the board from that. Once I understood that, everything became much easier.*
> 
> *I ended up creating two functions: One to add the number into the correct location, and the second function creates the board display, which already includes the updated numbers, since it's referencing the modified list.*
> 
> *All in all, this was a fun challenge. It pushed me to think more simply, and I came to the realization that just because a problem seems complicated at first, that doesn't mean it actually is. In fact, the solution is usually much simpler than we think."*

### **Key Takeaways**
1. **Don't overcomplicate** - Sometimes the simplest approach is the correct one
2. **Understanding references** - Lists are passed by reference, no return needed for `add_number`
3. **Step back when stuck** - Taking a breath and reassessing can reveal simple solutions
4. **Problem decomposition** - Breaking complex problems into simple functions
5. **List modification** - Understanding how in-place changes affect all references
6. **Visual programming** - Code that produces visual output requires careful formatting consideration

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
