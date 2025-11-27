# Double Items Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that creates a new list with all values from the original list doubled, while preserving the original list unchanged. This solution demonstrates list copying techniques, immutable operations, and clean code principles.

---

## 📖 Problem Description

Write a function named `double_items(numbers: list)` that takes a list of integers and returns a new list containing all values from the original list multiplied by 2. The function must **not modify** the original list.

### Requirements
- Take a list of integers as input
- Return a new list with all values doubled
- Preserve the original list (immutable operation)
- Handle positive, negative, and zero values

### Example
Input: `[2, 4, 5, 3, 11, -4]`  
Output: `[4, 8, 10, 6, 22, -8]`  
Original: `[2, 4, 5, 3, 11, -4]` *(unchanged)*

---

## 💻 Code Implementation

```python
def double_items(numbers: list):
    new_list = numbers[:]
    for i in range(len(numbers)):
        new_list[i] *= 2
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
```

**Output:**
```
original: [2, 4, 5, 3, 11, -4]
doubled: [4, 8, 10, 6, 22, -8]
```

---

## 🧠 Algorithm Explanation

The solution uses a **copy-and-modify approach**:

1. **Create a shallow copy** using slice notation `numbers[:]`
2. **Iterate through indices** using `range(len(numbers))`
3. **Double each element** in the copied list using `*= 2`
4. **Return the new list** while original remains unchanged

**Time Complexity:** O(n) where n is the length of the list  
**Space Complexity:** O(n) for the new list creation

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 double_items.py
```

Or import the function in your own code:

```python
from double_items import double_items

my_numbers = [1, 2, 3, 4, 5]
doubled = double_items(my_numbers)
print(f"Original: {my_numbers}")
print(f"Doubled: {doubled}")
```

---

## 🧪 Test Cases

```python
# Test case 1: Positive numbers
numbers1 = [1, 2, 3, 4, 5]
result1 = double_items(numbers1)
print(result1)  # Output: [2, 4, 6, 8, 10]

# Test case 2: Mixed positive and negative
numbers2 = [-1, 0, 1, -5, 10]
result2 = double_items(numbers2)
print(result2)  # Output: [-2, 0, 2, -10, 20]

# Test case 3: Single element
numbers3 = [42]
result3 = double_items(numbers3)
print(result3)  # Output: [84]

# Test case 4: Empty list
numbers4 = []
result4 = double_items(numbers4)
print(result4)  # Output: []

# Test case 5: All zeros
numbers5 = [0, 0, 0]
result5 = double_items(numbers5)
print(result5)  # Output: [0, 0, 0]

# Verify original lists remain unchanged
print("Original numbers1:", numbers1)  # Still [1, 2, 3, 4, 5]
```

---

## ✨ Key Learning Highlights

This seemingly simple problem introduced **valuable new techniques** and reinforced clean coding principles:

### **New Technique: List Slice Copying**
```python
new_list = numbers[:]  # Shorthand for creating a shallow copy
```
- **Discovery**: Learned the elegant `[:]` syntax for list copying
- **Alternative to**: `new_list = numbers.copy()` or `new_list = list(numbers)`
- **Benefits**: Concise, readable, and Pythonic approach

### **Immutable Operations**
- **Goal**: Preserve original data while creating modified versions
- **Implementation**: Always work on copies, never modify input parameters
- **Best Practice**: Functions should be predictable and side-effect free

### **Clean, Modular Code**
- **Readable Logic**: Clear step-by-step approach
- **Single Responsibility**: Function does one thing well
- **Maintainable**: Easy to test and modify

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Explicit Copying**: `numbers[:]` makes the copying intention clear
2. **Index-based Iteration**: `range(len())` provides clear control over modification
3. **In-place Doubling**: `*= 2` is efficient and readable
4. **Preservation of Original**: Immutable operations maintain data integrity

### **Clean Code Principles Applied**
- **Descriptive Naming**: `new_list` clearly indicates purpose
- **Simple Logic**: Straightforward loop without complex operations
- **No Side Effects**: Original list remains completely unchanged

---

---

## 🎓 Learning Outcomes

* **List Copying Techniques**: Mastered the `[:]` slice notation for shallow copying
* **Immutable Operations**: Understanding the importance of preserving input data
* **Index Manipulation**: Effective use of `range(len())` for list traversal
* **Clean Code Practices**: Writing readable, maintainable functions
* **Testing Mindset**: Ensuring original data remains unchanged
* **Python Idioms**: Learning concise, Pythonic approaches to common operations

---

## 💡 Developer Reflection

> *"This was a fairly simple problem but a fun one because I used new techniques like the shorthand for copying a list (`list[:]`). Other than that fun new twist, I had no issues and the goal remained the same: to make clean and modular code."*

### **Key Takeaways**
1. **Simple problems can teach valuable techniques** - The `[:]` copying method was a great discovery
2. **Consistency in clean code approach** - Maintaining focus on readable, maintainable solutions
3. **Learning through practice** - Each problem reinforces good coding habits
4. **Importance of immutability** - Preserving original data is a crucial programming principle

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
