# Dictionary Inversion Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that inverts a dictionary in place, swapping keys and values to demonstrate advanced dictionary manipulation and reference-based programming concepts. This solution showcases the three-step copy-clear-rebuild pattern for safe in-place dictionary modifications.

---

## 📖 Problem Description

Write a function named `invert(dictionary: dict)` that takes a dictionary as its argument and inverts it **in place** so that values become keys and keys become values. The original dictionary object must be modified directly rather than creating a new dictionary.

### Requirements
- **In-place modification**: The original dictionary object must be altered, not replaced
- **Key-value swap**: All keys become values and all values become keys
- **Reference preservation**: The dictionary reference passed to the function must remain valid
- **Complete inversion**: All key-value pairs must be successfully swapped

### Example Usage
```python
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
```

**Sample Output:**
```
{"first": 1, "second": 2, "third": 3, "fourth": 4}
```

**Key Challenge:**
- Cannot modify dictionary while iterating over it
- Must preserve the original dictionary object reference
- Values must become valid keys (hashable types)

---

## 💻 Code Implementation

```python
def invert(s: dict):
    copy = {}
    for key in s:
        copy[key] = s[key]
    for key in copy:
        del s[key]
    for key in copy:
        s[copy[key]] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
```

**Sample Output:**
```
{"first": 1, "second": 2, "third": 3, "fourth": 4}
```

**Additional Test Cases:**
```python
# Test case 1: String to integer mapping
test1 = {"a": 1, "b": 2, "c": 3}
invert(test1)
print(test1)  # {1: "a", 2: "b", 3: "c"}

# Test case 2: Mixed types
test2 = {"hello": 42, "world": 100}
invert(test2)
print(test2)  # {42: "hello", 100: "world"}

# Test case 3: Single entry
test3 = {"key": "value"}
invert(test3)
print(test3)  # {"value": "key"}
```

---

## 🧠 Algorithm Explanation

### **The Three-Phase Copy-Clear-Rebuild Pattern**
```python
def invert(s: dict):
    # Phase 1: Create backup copy
    copy = {}
    for key in s:
        copy[key] = s[key]
    
    # Phase 2: Clear original dictionary
    for key in copy:
        del s[key]
    
    # Phase 3: Rebuild with inverted pairs
    for key in copy:
        s[copy[key]] = key  # Value becomes key, key becomes value
```

**Key Insights:**
- **Safe Copying**: Create complete backup before any modifications
- **Complete Clearing**: Remove all entries to start fresh
- **Inversion Logic**: `s[copy[key]] = key` swaps the key-value relationship
- **Reference Preservation**: Original dictionary object `s` is modified, not replaced

**Why This Approach Works:**
```python
# Original state
s = {1: "first", 2: "second"}

# After copying
copy = {1: "first", 2: "second"}  # Backup created
s = {1: "first", 2: "second"}     # Original unchanged

# After clearing
copy = {1: "first", 2: "second"}  # Backup intact
s = {}                            # Original now empty

# After rebuilding  
copy = {1: "first", 2: "second"}  # Backup still intact
s = {"first": 1, "second": 2}     # Original now inverted
```

**Time Complexity:** O(n) - Three linear passes through the dictionary  
**Space Complexity:** O(n) - Additional dictionary for temporary storage

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 invert_dictionary.py
```

Or use the function in your own code:

```python
from invert_dictionary import invert

my_dict = {"apple": 1, "banana": 2, "cherry": 3}
invert(my_dict)
print(my_dict)  # {1: "apple", 2: "banana", 3: "cherry"}
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic integer-string mapping
original = {1: "first", 2: "second", 3: "third", 4: "fourth"}
expected = {"first": 1, "second": 2, "third": 3, "fourth": 4}
invert(original)
assert original == expected

# Test case 2: String-integer mapping  
original = {"a": 10, "b": 20, "c": 30}
expected = {10: "a", 20: "b", 30: "c"}
invert(original)
assert original == expected

# Test case 3: Empty dictionary
original = {}
expected = {}
invert(original)
assert original == expected

# Test case 4: Single entry
original = {"solo": "item"}
expected = {"item": "solo"}
invert(original)
assert original == expected

# Test case 5: Reference preservation test
original = {"test": "value"}
reference = original
invert(original)
assert reference is original  # Same object reference
assert reference == {"value": "test"}

# Test case 6: Mixed data types
original = {"str": 42, "num": "text", 99: "number"}
expected = {42: "str", "text": "num", "number": 99}
invert(original)
assert original == expected

# Test case 7: Duplicate values (potential key collision)
# Note: This would cause issues - values must be unique to become valid keys
# original = {"a": 1, "b": 1}  # Would overwrite in inverted form
```

---

## ✨ Key Learning Highlights

This problem demonstrates **in-place dictionary manipulation** and **reference semantics**:

### **The Copy-Clear-Rebuild Pattern**
```python
# Critical pattern for safe in-place modifications
def invert(s: dict):
    copy = {}               # Step 1: Create backup
    for key in s:
        copy[key] = s[key]  # Copy all key-value pairs
    
    for key in copy:        # Step 2: Clear original safely
        del s[key]          # Remove using backup keys
    
    for key in copy:        # Step 3: Rebuild with inversion
        s[copy[key]] = key  # Values become keys, keys become values
```

### **Why Direct Modification Fails**
```python
# This DOESN'T work - modifying while iterating
def broken_invert(s: dict):
    for key in s:
        value = s[key]
        del s[key]          # ERROR: Dictionary changed during iteration
        s[value] = key
```

### **Reference vs New Object Creation**
```python
# Wrong approach - creates new dictionary
def wrong_invert(s: dict):
    return {v: k for k, v in s.items()}  # Returns new dict, doesn't modify s

# Correct approach - modifies existing dictionary
def correct_invert(s: dict):
    # Three-phase process modifies s in place
    copy = dict(s)
    s.clear()
    for k, v in copy.items():
        s[v] = k
```

### **Dictionary Iteration Safety**
```python
# Safe: Iterate over copy while modifying original
for key in copy:        # Iterate over static backup
    del s[key]          # Modify original dictionary

# Unsafe: Iterate over dictionary being modified
for key in s:           # Iterator becomes invalid
    del s[key]          # Runtime error
```

---

## 🎯 Design Philosophy

### **Why This Three-Phase Approach?**
1. **Safety**: Avoids runtime errors from modifying during iteration
2. **Clarity**: Each phase has a distinct, understandable purpose
3. **Correctness**: Guarantees complete inversion without data loss
4. **Reference Integrity**: Preserves the original dictionary object

### **Alternative Approaches Considered**
```python
# Approach 1: Dictionary comprehension (creates new dict)
def alt1(s: dict):
    s = {v: k for k, v in s.items()}  # Doesn't modify original

# Approach 2: Items() with clear (chosen alternative)
def alt2(s: dict):
    items = list(s.items())  # Convert to list first
    s.clear()                # Clear original
    for k, v in items:
        s[v] = k            # Rebuild inverted

# Approach 3: Pop-based (works but less clear)
def alt3(s: dict):
    temp = {}
    while s:
        k, v = s.popitem()
        temp[v] = k
    s.update(temp)
```

### **Clean Code Principles Applied**
- **Single Responsibility**: Each loop has one clear purpose
- **Readability**: Code structure mirrors the logical steps
- **Safety First**: Prevents common dictionary modification errors
- **Explicit Intent**: Three phases make the algorithm obvious

---

## 🔄 Problem-Solving Process

### **Initial Approach Attempts**
```python
# First attempt (failed): Direct modification
def attempt1(s: dict):
    for key in s:
        s[s[key]] = key  # Creates new entries while iterating
        del s[key]       # Modifies dictionary during iteration - ERROR!
```

### **Understanding the Core Challenge**
The key insight: **Cannot modify a dictionary while iterating over it**
```python
# The fundamental problem
for key in dictionary:      # Creates iterator
    del dictionary[key]     # Invalidates iterator - RuntimeError!
```

### **Solution Evolution**
```python
# Evolution of thought process:
# 1. Need to swap keys and values
# 2. Cannot modify during iteration  
# 3. Must preserve original dictionary reference
# 4. Solution: Copy → Clear → Rebuild pattern
```

### **Critical Implementation Details**
```python
# The inversion logic
for key in copy:
    s[copy[key]] = key
#   ↑        ↑     ↑
#   |        |     └─ Original key becomes new value
#   |        └─ Original value becomes new key  
#   └─ Assign to original dictionary
```

---

## 🎓 Learning Outcomes

* **In-place Modification**: Understanding when and how to modify objects vs creating new ones
* **Dictionary Iteration Rules**: Learning the constraints of modifying collections during iteration
* **Reference Semantics**: Grasping how Python passes mutable objects by reference
* **Safe Copying Patterns**: Creating backups before destructive operations
* **Algorithm Design**: Breaking complex operations into clear, safe phases
* **Error Prevention**: Understanding common pitfalls in dictionary manipulation
* **Data Structure Invariants**: Maintaining object identity while changing contents

---

## 💡 Developer Reflection

> *"Reflection: This was a fairly challenging problem for me because it really pushed me to think much deeper about how dictionaries work. At first, I thought I could just invert the dictionary in a similar way as a list, but for obvious reasons that didn't work, mainly because a dictionary isn't a list. Then I thought more simply and realized I needed another dictionary to hold the items from the first one in reverse order, and that I would have to shuffle the keys and values in a similar way to how I'd shuffle items between two variables. With that thought process I came to my final answer. All in all, I learned a lot more about the inner workings of a dictionary."*

### **Key Insights Gained**

**Dictionary vs List Understanding:**
- **Structural Differences**: Dictionaries aren't ordered sequences like lists
- **Iteration Constraints**: Cannot modify dictionary structure during iteration
- **Key-Value Relationships**: Understanding bidirectional mapping concepts

**Reference Semantics Discovery:**
- **Object Identity**: Learning that function parameters are references, not copies
- **In-place Operations**: Distinguishing between modifying vs replacing objects
- **Memory Management**: Understanding how Python handles mutable object references

**Algorithm Development Process:**
- **Problem Decomposition**: Breaking complex operations into manageable steps
- **Safety Patterns**: Developing habits that prevent common runtime errors
- **Code Clarity**: Writing code that expresses intent clearly through structure

### **Programming Growth Demonstrated**
This project provided deep insights into:
- How Python's reference system works with mutable objects
- The importance of understanding iteration constraints in data structures
- Problem-solving strategies for operations that seem simple but have hidden complexity
- The value of step-by-step approaches to complex data transformations

**Technical Skills Developed:**
- Dictionary manipulation techniques
- Safe iteration patterns
- In-place modification strategies
- Error prevention in collection operations

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- Dictionary operations and methods
- Mutable object references in Python
- Safe iteration patterns
- In-place vs functional programming approaches
