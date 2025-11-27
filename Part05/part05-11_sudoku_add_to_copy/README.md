# Sudoku Copy and Add Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that creates a copy of a Sudoku grid with a new number added, preserving the original grid unchanged. This solution demonstrates deep copying techniques for 2D arrays, immutable operations, and the critical difference between shallow and deep copies in nested data structures.

---

## 📖 Problem Description

Create a function `copy_and_add(sudoku: list, row_no: int, column_no: int, number: int)` that takes a Sudoku grid and returns a **new copy** with a number added at the specified location. The original grid must remain completely unchanged.

### Requirements
- Return a copy of the original grid with the new number added
- **Never modify** the original grid (immutable operation)
- Handle 9×9 two-dimensional arrays
- Place digits 1-9 at specified row/column coordinates
- Maintain proper deep copying of nested structures

### Key Challenge
Working with nested lists requires careful copying - a shallow copy `[:]` only copies the outer structure, leaving inner lists as shared references!

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

def copy_and_add(sudoku: list, row_num: int, col_num: int, number: int):
    grid_copy = [row[:] for row in sudoku]
    grid_copy[row_num][col_num] = number
    return grid_copy

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
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
```

**Output:**
```
Original:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Copy:
2 _ _  _ _ _  _ _ _
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

## 🧠 Algorithm Explanation

### **The Deep Copy Solution**
```python
grid_copy = [row[:] for row in sudoku]  # Deep copy using list comprehension
grid_copy[row_num][col_num] = number    # Modify the copy
return grid_copy                        # Return new grid
```

1. **Create Deep Copy**: Each `row[:]` creates a new list for every row
2. **Modify Copy**: Change the specified position in the copied grid
3. **Return New Grid**: Original remains completely unchanged

**Time Complexity:** O(n²) where n=9 for Sudoku (copying 81 elements)  
**Space Complexity:** O(n²) for the new grid structure

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 sudoku_copy.py
```

Or import the function in your own code:

```python
from sudoku_copy import copy_and_add, print_sudoku

# Create a partially filled grid
grid = [[1, 2, 3] + [0]*6 for _ in range(9)]

# Add number without modifying original
new_grid = copy_and_add(grid, 1, 1, 9)

print("Original grid:")
print_sudoku(grid)
print("\nModified copy:")
print_sudoku(new_grid)
```

---

## 🧪 Test Cases

```python
# Test case 1: Verify original unchanged
original = [[0 for _ in range(9)] for _ in range(9)]
modified = copy_and_add(original, 4, 4, 5)

print("Original after copy_and_add:")
print_sudoku(original)  # Should still be all zeros

print("Modified copy:")
print_sudoku(modified)  # Should have 5 in center

# Test case 2: Multiple additions
grid = [[0 for _ in range(9)] for _ in range(9)]
copy1 = copy_and_add(grid, 0, 0, 1)
copy2 = copy_and_add(copy1, 1, 1, 2)
copy3 = copy_and_add(copy2, 2, 2, 3)

print("Final copy with three numbers:")
print_sudoku(copy3)
print("Original still empty:")
print_sudoku(grid)

# Test case 3: Edge positions
corner_grid = [[0 for _ in range(9)] for _ in range(9)]
top_right = copy_and_add(corner_grid, 0, 8, 9)
bottom_left = copy_and_add(corner_grid, 8, 0, 1)

print("Top-right corner:")
print_sudoku(top_right)
print("Bottom-left corner:")
print_sudoku(bottom_left)
```

---

## ✨ Key Learning Highlights

This problem was a masterclass in **memory management** and **copying strategies** for nested data structures:

### **The Shallow Copy Trap**
```python
# WRONG - This is a shallow copy!
copy_grid = sudoku[:]  # Only copies outer list structure
```
- **Problem**: Inner lists are still shared references
- **Result**: Modifying copy affects the original
- **Lesson**: Shallow copies don't work for nested structures

### **Deep Copy Solution**
```python
# CORRECT - This creates a deep copy
grid_copy = [row[:] for row in sudoku]  # Copies each inner list
```
- **Discovery**: List comprehension with slice copying for each row
- **Result**: Complete independence between original and copy
- **Benefits**: True immutable operations

### **Memory Reference Understanding**
- **Visualization**: Understanding how Python manages references to nested objects
- **Core Concept**: The difference between copying structure vs. copying content
- **Best Practice**: Always consider depth when copying nested data

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Immutable Operations**: Never modify input parameters
2. **Clear Intent**: List comprehension shows copying purpose clearly  
3. **Memory Safety**: Complete separation between original and copy
4. **Functional Style**: Return new data rather than modifying existing

### **Clean Code Principles Applied**
- **Predictable Functions**: No side effects on input parameters
- **Single Responsibility**: Function does one thing - copy and add
- **Clear Implementation**: Readable list comprehension over complex loops

---

## 🔄 Code Evolution Story

### **Initial Attempt (Shallow Copy Problem)**
```python
def copy_and_add(sudoku, row, col, number):
    copy_grid = sudoku[:]  # WRONG - shallow copy!
    copy_grid[row][col] = number
    return copy_grid
# Problem: Modifying copy affected original!
```

### **Understanding the Issue**
```python
# Manual deep copy approach
copy_grid = []
for row in sudoku:
    copy_grid.append(row[:])  # Copy each row individually
```

### **Final Solution (Clean Deep Copy)**
```python
def copy_and_add(sudoku, row_num, col_num, number):
    grid_copy = [row[:] for row in sudoku]  # Elegant deep copy
    grid_copy[row_num][col_num] = number
    return grid_copy
```

---

## 🎓 Learning Outcomes

* **Deep vs Shallow Copying**: Understanding the critical difference in nested structures
* **Memory Reference Management**: How Python handles object references
* **List Comprehension Mastery**: Using comprehensions for complex copying operations
* **Immutable Function Design**: Creating functions that don't modify input data
* **2D Array Operations**: Advanced manipulation of nested list structures
* **Debugging Memory Issues**: Recognizing and solving reference-sharing problems

---

## 💡 Developer Reflection

> *"This was an interesting problem because it really challenged my thinking when it came to working with matrices (2D arrays). At first, when I tried to copy the matrix, I used `copy_grid = sudoku[:]`. I believed this was the correct approach, since up to this point, I had understood this as the way to copy a list. However, I quickly noticed that whenever I modified the copy, the original matrix was also being affected. That left me genuinely confused.*
> 
> *After a few minutes of tinkering and re-reading the challenge, I noticed the warning that was provided and realized what was going on: I was only copying the *outer structure* of the matrix. The inner lists were still referencing the same objects in memory. That meant any change to a row in the copy would also affect the original—because both were pointing to the same inner lists.*
> 
> *I later learned this is called making a **shallow copy**. To fix this, I wrote a `for` loop that iterates through each row of the `sudoku` matrix and appends a *copy* of each row to a new list. This gave me the **deep copy** I needed to avoid altering the original matrix.*
> 
> *After I got this working, I asked myself: *How can I make this cleaner or more modular?* From there, I refined the code until I ended up with my final `copy_and_add()` function.*
> 
> *All in all, this was a very informative problem that taught me how to properly copy a matrix. It clarified a core concept that I had misunderstood and gave me a much better understanding of how memory and references work in Python."*

### **Key Takeaways**
1. **Shallow vs Deep copying** - Understanding the critical difference for nested structures
2. **Memory reference awareness** - How Python manages object references in memory
3. **Problem-solving persistence** - Working through confusion to find the root cause
4. **Continuous improvement** - Always asking "how can this be cleaner?"
5. **Fundamental concepts matter** - Core understanding of references affects everything
6. **Learning from mistakes** - The shallow copy error led to deeper understanding

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
