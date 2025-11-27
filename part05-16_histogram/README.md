# Histogram Letter Counter Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that creates a visual histogram displaying letter frequency in a string using star symbols. This solution demonstrates dictionary creation, list manipulation, and the separation of data processing from presentation logic through modular function design.

---

## 📖 Problem Description

Write a function `histogram(word: str)` that takes a string as its argument and prints out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.

### Requirements
- Create a visual representation of letter frequency
- Each letter appears on its own line
- Stars (*) represent occurrences of each letter
- Letters appear in the order they first occur in the string
- Function should print the histogram (no return value)

### Example Transformation
```python
histogram("abba")
```
**Output:**
```
a **
b **
```

```python
histogram("statistically")
```
**Output:**
```
s **
t ***
a **
i **
c *
l **
y *
```

---

## 💻 Code Implementation

```python
def create_stats(word: str):
    groups = {}
    
    for letter in word:
        if letter not in groups:
            groups[letter] = []
        
        groups[letter].append("*")
    
    return groups

def histogram(word: str):
    groups = create_stats(word)
    
    for key, value in groups.items():
        print(f"{key} ", end="")
        for stats in value:
            print(f"{stats}", end="")
        print()

if __name__ == "__main__":
    histogram("statistically")
```

**Output:**
```
s **
t ***
a **
i **
c *
l **
y *
```

---

## 🧠 Algorithm Explanation

### **The Two-Phase Strategy**
```python
# Phase 1: Data Collection
def create_stats(word: str):
    groups = {}
    for letter in word:
        if letter not in groups:
            groups[letter] = []
        groups[letter].append("*")
    return groups

# Phase 2: Visual Presentation
def histogram(word: str):
    groups = create_stats(word)
    for key, value in groups.items():
        print(f"{key} ", end="")
        for stats in value:
            print(f"{stats}", end="")
        print()
```

**Key Insights:**
- **Separation of Concerns**: Data processing separated from presentation
- **Dictionary with Lists**: Each letter maps to a list of stars
- **Order Preservation**: Python dictionaries maintain insertion order (Python 3.7+)
- **Modular Design**: Two functions handle different responsibilities

**Step-by-Step Process:**
1. **Initialize**: Create empty dictionary `groups = {}`
2. **Process Each Letter**: Iterate through every character in the string
3. **Check Existence**: If letter not in dictionary, create empty list
4. **Add Star**: Append "*" to the letter's list
5. **Display Results**: Print each letter followed by its stars

**Time Complexity:** O(n) - Single pass through the string  
**Space Complexity:** O(k) - Where k is the number of unique letters

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 histogram.py
```

Or import the functions in your own code:

```python
from histogram import histogram, create_stats

# Create histogram for a word
histogram("hello")

# Or get the raw stats data
stats = create_stats("hello")
print(stats)  # {'h': ['*'], 'e': ['*'], 'l': ['*', '*'], 'o': ['*']}
```

---

## 🧪 Test Cases

```python
# Test case 1: Simple example
print("Test 1 - 'abba':")
histogram("abba")
# Expected:
# a **
# b **

# Test case 2: Complex word
print("\nTest 2 - 'statistically':")
histogram("statistically")
# Expected:
# s **
# t ***
# a **
# i **
# c *
# l **
# y *

# Test case 3: Single character repeated
print("\nTest 3 - 'aaaa':")
histogram("aaaa")
# Expected:
# a ****

# Test case 4: All unique letters
print("\nTest 4 - 'abcd':")
histogram("abcd")
# Expected:
# a *
# b *
# c *
# d *

# Test case 5: Mixed case and spaces
print("\nTest 5 - 'Hello World':")
histogram("Hello World")
# Expected:
# H *
# e *
# l ***
#   *
# o **
# W *
# r *
# d *

# Test case 6: Empty string
print("\nTest 6 - Empty string:")
histogram("")
# Expected: (no output)

# Test case 7: Testing create_stats function
print("\nTest 7 - Raw stats for 'test':")
stats = create_stats("test")
print(stats)
# Expected: {'t': ['*', '*'], 'e': ['*'], 's': ['*']}
```

---

## ✨ Key Learning Highlights

This problem demonstrates **modular programming design** and **data structure selection**:

### **Modular Function Design**
```python
# OPTION 1: Single function approach (less modular)
def histogram_simple(word: str):
    letter_counts = {}
    # Count letters and print in one function
    
# OPTION 2: Two-function approach (chosen solution)
def create_stats(word: str):
    # Handle data collection only
    
def histogram(word: str):
    # Handle presentation only
```

### **Dictionary with Lists Strategy**
```python
# Why lists of stars instead of just counts?
groups = {
    'a': ['*', '*'],      # Visual representation ready
    'b': ['*']            # Easy to iterate for printing
}

# Alternative approach with counts:
counts = {'a': 2, 'b': 1}  # Would need conversion for printing
```

### **Order Preservation Insight**
- **Python 3.7+ Feature**: Dictionaries maintain insertion order
- **First Occurrence Order**: Letters appear in the order they first appear in string
- **Consistent Output**: Predictable histogram layout

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Separation of Concerns**: Data processing separated from display logic
2. **Reusability**: `create_stats` can be used independently for data analysis
3. **Visual Representation**: Lists of stars make printing straightforward
4. **Order Maintenance**: Dictionary preserves the natural letter appearance order

### **Clean Code Principles Applied**
- **Single Responsibility**: Each function has one clear purpose
- **Descriptive Names**: `create_stats`, `groups`, `histogram` show intent
- **Modular Design**: Functions can be tested and used independently
- **Clear Logic Flow**: Collect data → Process data → Display results

---

## 🔄 Problem-Solving Process

### **Understanding the Requirements**
The problem needs:
1. Letter frequency counting
2. Visual representation with stars
3. Maintaining order of first occurrence
4. Printing format: "letter stars"

### **Data Structure Decision**
```python
# Chosen: Dictionary with lists of stars
groups = {'a': ['*', '*'], 'b': ['*']}

# Alternative: Dictionary with counts
counts = {'a': 2, 'b': 1}  # Requires conversion for display
```

### **Implementation Strategy**
```python
def create_stats(word: str):
    groups = {}
    for letter in word:
        if letter not in groups:
            groups[letter] = []        # Initialize empty list
        groups[letter].append("*")     # Add star for each occurrence
    return groups
```

### **Display Logic**
```python
def histogram(word: str):
    groups = create_stats(word)
    for key, value in groups.items():  # Iterate in insertion order
        print(f"{key} ", end="")       # Print letter and space
        for stats in value:            # Print each star
            print(f"{stats}", end="")
        print()                        # New line after each letter
```

---

## 🎓 Learning Outcomes

* **Modular Programming**: Separating data processing from presentation logic
* **Dictionary Operations**: Using dictionaries with complex values (lists)
* **List Manipulation**: Appending and iterating through list elements
* **Order Preservation**: Understanding Python dictionary insertion order
* **Print Control**: Managing output formatting with `end=""` parameter
* **Data Structure Selection**: Choosing appropriate structures for the task
* **Function Design**: Creating reusable and testable function components

---



---

## 💡 Developer Reflection

> *"**Reflection:** This problem was interesting because I got to use a new dictionary-specific function, `.items()`, and saw firsthand how to iterate through a dictionary. It wasn't a particularly challenging problem, but it was still engaging.
After reviewing my solution, I realized I got too hung up on adding everything to the dictionary all at once. If I were to redo it, I would instead make the keys the letters in the words and the values the number of times each letter appears. Then, in my histogram function, I could print the stars by simply multiplying the value by an asterisk string (`value * "*"`)—which feels cleaner, more readable, and easier to understand overall."*

### **Learning Insights from the Experience**

**New Dictionary Methods:**
- **`.items()` Discovery**: First hands-on experience with dictionary key-value iteration
- **Dictionary Iteration**: Understanding how to loop through both keys and values simultaneously
- **Practical Application**: Seeing dictionary methods in action rather than just theory

**Current Solution Analysis:**
- **Overcomplication**: Recognized that storing lists of stars was unnecessarily complex
- **String Multiplication Insight**: Realized `value * "*"` is much cleaner than list iteration
- **Simpler Data Structure**: Understanding that integer counts are more straightforward than star lists

**Planned Improvement Strategy:**
```python
# Current approach (complex)
groups = {'a': ['*', '*'], 'b': ['*']}
for stats in value:
    print(f"{stats}", end="")

# Planned approach (simpler)
counts = {'a': 2, 'b': 1}
print(count * "*")
```

**Key Takeaways:**
1. **Dictionary Method Mastery**: Learning `.items()` for key-value pair iteration
2. **Code Evolution**: Recognizing opportunities to simplify after initial implementation
3. **String Operations**: Discovering Python's string multiplication for cleaner output
4. **Data Structure Reflection**: Understanding when simpler data structures are better
5. **Continuous Improvement**: Planning to refactor for better readability and maintainability

### **Technical Growth Demonstrated**
This experience shows important development practices:
- **Self-Assessment**: Critically evaluating your own code after completion
- **Simplification Mindset**: Recognizing when solutions can be made cleaner
- **Learning Integration**: Connecting new dictionary methods to practical applications
- **Refactoring Planning**: Thinking about how to improve code structure

The planned improvement demonstrates mature programming thinking - moving from "make it work" to "make it clean and understandable."

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
