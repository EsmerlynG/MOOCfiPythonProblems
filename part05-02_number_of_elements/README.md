# Count Matching Elements in Matrix

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A clean and efficient Python function that counts how many elements within a two-dimensional matrix match a specified target value. This exercise demonstrates matrix traversal, built-in list methods, and clean code principles.

---

## 📖 Problem Description

Write a function named `count_matching_elements(my_matrix: list, element: int)` that takes a two-dimensional array of integers and a single integer value as arguments. The function should count how many elements within the matrix match the target value.

### Example

Given the matrix:
```python
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
```

Calling `count_matching_elements(m, 1)` should return `3` because the number `1` appears three times in the matrix.

---

## 💻 Code Implementation

```python
def count_matching_elements(my_matrix: list, searched_number: int):
    count = 0
    for row in my_matrix:
        count += row.count(searched_number)
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
```

**Output:**
```
3
```

---

## 🧠 Algorithm Explanation

The solution uses Python's built-in `count()` method for maximum efficiency and readability:

1. **Initialize** a counter variable to zero
2. **Iterate** through each row in the matrix
3. **Use `count()` method** to count occurrences of the target number in each row
4. **Accumulate** the count from each row
5. **Return** the total count

**Time Complexity:** O(m × n) where m is the number of rows and n is the number of columns  
**Space Complexity:** O(1) using only a single counter variable

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 count_matching.py
```

Or import the function in your own code:

```python
from count_matching import count_matching_elements

matrix = [[5, 2, 5], [1, 5, 8], [5, 0, 2]]
result = count_matching_elements(matrix, 5)
print(f"Number 5 appears {result} times")
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic functionality
m1 = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m1, 1))  # Output: 3

# Test case 2: No matches
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(count_matching_elements(m2, 0))  # Output: 0

# Test case 3: All elements match
m3 = [[7, 7], [7, 7]]
print(count_matching_elements(m3, 7))  # Output: 4

# Test case 4: Single row matrix
m4 = [[1, 2, 3, 2, 2]]
print(count_matching_elements(m4, 2))  # Output: 3

# Test case 5: Single element matrix
m5 = [[42]]
print(count_matching_elements(m5, 42))  # Output: 1
```

---

## ✨ Design Philosophy & Clean Code

This solution prioritizes **code clarity and efficiency** through several key decisions:

### **Leveraging Built-in Methods**
- Used Python's `list.count()` method instead of manual iteration
- Reduces code complexity and potential for bugs
- Takes advantage of optimized C implementations

### **Readable Variable Names**
- `my_matrix` clearly indicates the two-dimensional structure
- `searched_number` explicitly describes the target value
- `count` provides obvious purpose tracking

### **Minimal Code Footprint**
- Only 4 lines of core logic
- No nested loops required
- Single responsibility principle maintained

### **Pythonic Approach**
- Embraces Python's philosophy of "simple is better than complex"
- Uses idiomatic Python patterns
- Maximizes readability while maintaining performance

---

## 🔍 Alternative Approach

While the current implementation is optimal, here's another valid approach:

### Nested Loop Approach:
```python
def count_matching_nested(my_matrix: list, searched_number: int):
    count = 0
    for row in my_matrix:
        for element in row:
            if element == searched_number:
                count += 1
    return count
```

---

## 🎯 Reflection

This exercise was particularly interesting because it challenged me to find the **cleanest possible solution**. The key insight was recognizing that Python's built-in `count()` method could handle the inner loop logic, resulting in:

- **Fewer lines of code** without sacrificing readability
- **Better performance** through optimized built-in methods  
- **Reduced complexity** by eliminating nested loops
- **Enhanced maintainability** with clear, concise logic

The solution demonstrates that sometimes the most elegant approach is not about writing more code, but about leveraging the right tools effectively.

---

## 📚 Key Learning Outcomes

* **Matrix traversal techniques:** Understanding how to work with 2D data structures
* **Built-in method utilization:** Leveraging Python's powerful list methods
* **Code optimization:** Choosing efficient approaches over verbose solutions
* **Clean code principles:** Writing readable, maintainable code
* **Algorithm analysis:** Understanding time and space complexity trade-offs

---

## 🎓 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
