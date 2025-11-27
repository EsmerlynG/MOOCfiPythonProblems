# Create Tuple

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen) ![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)  

A Python function that constructs a tuple containing the **minimum value**, **maximum value**, and **sum** of three integers. The solution demonstrates Python’s built-in `min`, `max`, and `sum` functions in combination with tuple creation.  

---

## 📖 Problem Description

Write a function named `create_tuple(x: int, y: int, z: int)` that takes three integers as input and returns a tuple with the following structure:

1. **First element**: The smallest of the arguments  
2. **Second element**: The largest of the arguments  
3. **Third element**: The sum of all the arguments  

### Requirements
- Input: Three integers `x`, `y`, and `z`  
- Output: A tuple `(min, max, sum)`  
- Must use consistent tuple structure for all inputs  

### Example Usage
```python
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
````

**Sample Output:**

```
(-1, 5, 7)
```

---

## 💻 Code Implementation

```python
# Write your solution here
def create_tuple(x: int, y: int, z: int):
    numbers = (x, y, z)
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    
    return (smallest, largest, total)


if __name__ == "__main__":
    print(create_tuple(1, 4, 7))
```

**Sample Output:**

```
(1, 7, 12)
```

---

## 🧠 Algorithm Explanation

### **Tuple Construction**

```python
numbers = (x, y, z)
smallest = min(numbers)
largest = max(numbers)
total = sum(numbers)
return (smallest, largest, total)
```

**Key Insights:**

* `min()` finds the smallest integer
* `max()` finds the largest integer
* `sum()` calculates the total of all three integers
* Returning a tuple groups results into a single immutable structure

**Time Complexity:** O(1) — only three values are processed
**Space Complexity:** O(1) — constant space for three integers

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 create_tuple.py
```

Or import the function into your own project:

```python
from create_tuple import create_tuple

result = create_tuple(2, 9, 4)
print(result)  # Output: (2, 9, 15)
```

---

## 🧪 Test Cases

```python
# Test case 1: Positive numbers
assert create_tuple(1, 4, 7) == (1, 7, 12)

# Test case 2: Includes negative numbers
assert create_tuple(5, 3, -1) == (-1, 5, 7)

# Test case 3: All numbers equal
assert create_tuple(2, 2, 2) == (2, 2, 6)

# Test case 4: Mixed values
assert create_tuple(-10, 0, 10) == (-10, 10, 0)

# Test case 5: Large numbers
assert create_tuple(1000, 5000, 3000) == (1000, 5000, 9000)
```

---

## ✨ Key Learning Highlights

* **Tuple construction** to group related values
* **Built-in functions**: `min`, `max`, and `sum`
* **Deterministic order**: always returns `(smallest, largest, sum)`
* **Immutability**: tuples provide safe, fixed data grouping

---

## 🎯 Design Philosophy

1. **Clarity**: Straightforward use of built-in functions
2. **Consistency**: Always returns three values in fixed positions
3. **Reusability**: Works with any integers, positive or negative
4. **Efficiency**: Constant-time operations, minimal code

---

## 🔄 Problem-Solving Process

* Identified need for smallest, largest, and total values
* Used Python’s built-ins instead of writing manual loops
* Stored results in descriptive variables before constructing tuple
* Returned a tuple `(smallest, largest, total)` to meet requirements

---

## 🎓 Learning Outcomes

* Learned how to **aggregate multiple related results** in a tuple
* Practiced **using built-in functions** for efficiency
* Reinforced **data structure selection** (tuple for grouped results)
* Saw how simple problems can model **real-world patterns** (e.g., min/max/sum statistics)

---

## 💡 Developer Reflection

> *"No reflection, I was only creating a tuple. The exercise simply reinforced using Python’s built-in functions to simplify basic operations."*
