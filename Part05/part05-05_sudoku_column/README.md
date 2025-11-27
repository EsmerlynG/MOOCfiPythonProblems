# Sudoku Column Validator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that validates whether a specific column in a Sudoku grid follows the game's fundamental rule: each number 1-9 appears at most once per column. This solution demonstrates 2D array column traversal, duplicate detection, and the importance of code visualization in problem-solving.

---

## 📖 Problem Description

Write a function named `column_correct(sudoku: list, column_no: int)` that takes a two-dimensional array representing a Sudoku grid and an integer specifying a column index (0-based). The function should return `True` if the column is valid according to Sudoku rules, or `False` if it contains duplicate numbers.

### Sudoku Column Rules
- Each column must contain numbers 1-9 **at most once**
- Empty cells are represented by `0` and don't count as duplicates
- Multiple `0`s in a column are allowed (incomplete puzzle)
- Any duplicate of numbers 1-9 makes the column invalid

### Example
For the given Sudoku grid:
- Column 0: `[9, 2, 0, 2, 0, 7, 0, 0, 3]` → **Invalid** (duplicate 2)
- Column 1: `[0, 0, 2, 9, 0, 0, 0, 0, 0]` → **Valid** (no duplicates)

---

## 💻 Code Implementation

```python
def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        num = row[column_no]
        if num > 0 and num in column:
            return False
        column.append(num)
    
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(column_correct(sudoku, 0))  # False
    print(column_correct(sudoku, 1))  # True
```

**Output:**
```
False
True
```

---

## 🧠 Algorithm Explanation

The solution traverses the 2D array **vertically** to extract and validate a column:

1. **Initialize** an empty list to track seen numbers in the column
2. **Iterate** through each row of the Sudoku grid
3. **Extract** the element at position `column_no` from each row
4. **Check duplicates**: If the number is positive (not 0) and already exists in our tracking list, return `False` immediately
5. **Track numbers**: Add the current number to our tracking list
6. **Return success**: If no duplicates are found, return `True`

**Key Insight:** `row[column_no]` extracts the column element from each row, building the column vertically.

**Time Complexity:** O(n²) worst case, O(n) average case (early termination)  
**Space Complexity:** O(n) for the tracking list

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 sudoku_column_validator.py
```

Or import the function in your own code:

```python
from sudoku_column_validator import column_correct

# Test with your own Sudoku grid
my_sudoku = [[1, 0, 3], [2, 0, 4], [1, 0, 5]]  # Column 0 has duplicate 1
print(column_correct(my_sudoku, 0))  # False
print(column_correct(my_sudoku, 1))  # True (all zeros)
```

---

## 🧪 Test Cases

```python
# Test case 1: Valid column with zeros
sudoku1 = [[1, 0], [2, 0], [3, 0]]
print(column_correct(sudoku1, 0))  # Output: True
print(column_correct(sudoku1, 1))  # Output: True (all zeros)

# Test case 2: Invalid column with duplicates
sudoku2 = [[1, 5], [2, 6], [1, 7]]  # Column 0 has duplicate 1
print(column_correct(sudoku2, 0))  # Output: False

# Test case 3: Complete valid column
sudoku3 = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
print(column_correct(sudoku3, 0))  # Output: True

# Test case 4: Early duplicate detection
sudoku4 = [[5], [5], [1], [2], [3]]  # Duplicate in first two rows
print(column_correct(sudoku4, 0))  # Output: False (stops early)
```

---

## 🎯 Learning Journey & Visualization Challenges

This problem presented unique **visualization challenges** that led to important learning insights:

### **The Column Indexing Challenge**
Initially, understanding **where to use `column_no`** in the 2D array traversal was difficult:
- **Problem**: How does `column_no` relate to `sudoku[row][column]`?
- **Confusion**: Visualizing vertical traversal in a horizontal code structure
- **Solution**: Using Python Tutor code visualizer to see the execution step-by-step

### **Breakthrough with Code Visualization**
Using **Python Tutor** provided crucial insights:
- **Visual Understanding**: Seeing how `row[column_no]` extracts column elements
- **Step-by-step Execution**: Watching the column list build vertically
- **Mental Model**: Understanding 2D array indexing patterns

### **Key Realizations**
1. **Column traversal** requires iterating through **rows** but accessing the **same index**
2. **`row[column_no]`** is the key to extracting vertical data from horizontal structure
3. **Visualization tools** are invaluable for understanding complex data structures

---

## 🔧 Development Tools That Helped

### **Python Tutor Code Visualizer**
- **Website**: [pythontutor.com](http://pythontutor.com)
- **Benefits**: Step-by-step code execution visualization
- **Use Case**: Understanding 2D array traversal patterns
- **Impact**: Transformed confusion into clear understanding

### **Problem-Solving Strategy**
1. **Initial Attempt**: Struggled with abstract thinking about column access
2. **Visualization**: Used Python Tutor to see actual execution
3. **Understanding**: Gained clarity on `row[column_no]` pattern
4. **Implementation**: Applied insights to create working solution

---

## ✨ Algorithm Design Insights

### **2D Array Column Access Pattern**
```python
# To access column 'col' from 2D array:
for row in array_2d:
    element = row[col]  # This builds the column vertically
```

### **Early Termination Optimization**
- Returns `False` immediately upon finding first duplicate
- Efficient for invalid columns (stops processing early)
- Optimal performance for most validation scenarios

---

## 🔍 Alternative Approach

While the current implementation is efficient, here's another valid approach:

### List Comprehension with Set:
```python
def column_correct_set(sudoku: list, column_no: int):
    column_values = [row[column_no] for row in sudoku if row[column_no] > 0]
    return len(column_values) == len(set(column_values))
```

---

## 📚 Key Learning Outcomes

* **2D Array Traversal**: Understanding column access patterns in matrices
* **Visualization Tools**: Learning the value of code execution visualizers
* **Problem-Solving Process**: Overcoming conceptual barriers with the right tools
* **Index Manipulation**: Mastering `row[column_no]` pattern for vertical data extraction
* **Debugging Strategies**: Using visualization to understand complex logic flows
* **Sudoku Validation**: Building foundation for complete puzzle validation

---

## 🎓 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

---

## 💡 Developer Note

*"This challenge taught me the importance of visualization tools in programming. When abstract thinking isn't enough, seeing the code execute step-by-step can provide the clarity needed to solve complex problems."*
