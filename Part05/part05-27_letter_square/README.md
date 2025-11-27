# A Square of Letters

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)
![Difficulty](https://img.shields.io/badge/Difficulty-Challenging-red)

A Python program that generates layered letter squares with alphabetic borders. This solution demonstrates advanced problem-solving skills, string manipulation techniques, and algorithmic thinking through a two-phase construction approach that builds the pattern line by line.

---

## 📖 Problem Description

Write a program that prints out a square of letters based on the number of layers specified. Each layer uses consecutive letters from the alphabet, with the outermost layer using the nth letter of the alphabet (where n is the number of layers). The pattern creates a symmetric square with nested letter borders.

### Requirements
- **Input**: Number of layers (1-26)
- **Output**: Square pattern with alphabetic layers
- **Pattern Rules**: Outermost layer uses nth letter, inner layers use previous letters
- **Symmetry**: Perfect horizontal and vertical symmetry
- **No Functions**: Solution should not use function definitions
- **Maximum Layers**: Up to 26 layers (full alphabet)

### Example Usage
```
Layers: 3
CCCCC
CBBBC
CBABC
CBBBC
CCCCC
```

```
Layers: 4
DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD
```

**Pattern Analysis:**
- Layer 3 uses 'C' as outermost, 'B' as middle, 'A' as center
- Layer 4 uses 'D' as outermost, 'C', 'B', 'A' progressing inward
- Each layer forms a complete border around inner layers

---

## 💻 Code Implementation

```python
# Write your solution here
n = int(input("Layers: "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

left = ""
right = ""
k = n - 1
m = 2 * n - 1

# First phase: Build top half (including middle)
while k >= 1:
    left += alphabet[k]
    right = alphabet[k] + right
    m -= 2
    print(left + alphabet[k] * m + right)
    k -= 1

# Second phase: Build bottom half  
while k <= n - 1:
    print(left + alphabet[k] * m + right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1
```

**Sample Output (n=3):**
```
Layers: 3
CCCCC
CBBBC
CBABC
CBBBC
CCCCC
```

**Sample Output (n=4):**
```
Layers: 4
DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD
```

**Additional Test Cases:**
```python
# Layer 1
Layers: 1
A

# Layer 2  
Layers: 2
BBB
BAB
BBB

# Layer 5
Layers: 5
EEEEEEEEE
EDDDDDDDE
EDCCCCCDE
EDCBBBCDE
EDCBABCDE
EDCBBBCDE
EDCCCCCDE
EDDDDDDDE
EEEEEEEEE
```

---

## 🧠 Algorithm Explanation

### **Two-Phase Construction Strategy**
```python
# Phase 1: Top half (including middle row)
k = n - 1          # Start from outermost layer
while k >= 1:      # Build down to center
    # Build sides progressively
    left += alphabet[k]
    right = alphabet[k] + right
    # Print row with center fill
    print(left + alphabet[k] * m + right)

# Phase 2: Bottom half (mirror of top)
while k <= n - 1:  # Build back up to outermost
    # Remove outermost characters
    left = left[:-1]
    right = right[1:]
    # Print mirrored rows
    print(left + alphabet[k] * m + right)
```

**Key Insights:**
- **Progressive Building**: Left and right sides built incrementally
- **Center Calculation**: Middle portion uses `alphabet[k] * m` for fill
- **Symmetric Construction**: Second phase mirrors first phase structure
- **String Manipulation**: Efficient building and trimming of border strings

### **Mathematical Relationships**
```python
# For n layers:
total_width = 2 * n - 1    # Total square width
center_width = m          # Width of center fill area

# Row structure: left_border + center_fill + right_border
row = left + alphabet[k] * m + right

# Variables evolution:
# k: layer index (n-1 down to 0, then back up)
# m: center fill width (starts at 2*n-1, decreases, then increases)
# left: accumulating left border characters  
# right: accumulating right border characters
```

**Pattern Analysis:**
```python
# For n=4 example:
# Row 0: "" + "D"*7 + "" = "DDDDDDD"
# Row 1: "D" + "C"*5 + "D" = "DCCCCCD"  
# Row 2: "DC" + "B"*3 + "CD" = "DCBBBCD"
# Row 3: "DCB" + "A"*1 + "BCD" = "DCBABCD"
# Then mirror for bottom half
```

**Time Complexity:** O(n²) - Prints n×n characters across 2n-1 rows  
**Space Complexity:** O(n) - Left and right border strings grow to size n

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 square_letters.py
```

The program will prompt for input:
```
Layers: 3
```

---

## 🧪 Test Cases

```python
# Test case 1: Minimum size
# Input: 1
# Expected:
# A

# Test case 2: Small square
# Input: 2  
# Expected:
# BBB
# BAB
# BBB

# Test case 3: Medium square
# Input: 3
# Expected:
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

# Test case 4: Larger square
# Input: 4
# Expected:
# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

# Test case 5: Alphabet boundary
# Input: 26
# Expected: 51x51 square with 'Z' as outer layer

# Test case 6: Pattern verification
# For any layer n:
# - Total rows: 2*n - 1
# - Total columns: 2*n - 1  
# - Outermost letter: alphabet[n-1]
# - Center letter: 'A'
# - Perfect symmetry: row[i] == row[2*n-2-i]

# Test case 7: Edge verification  
# For layer n:
# - Top row: all alphabet[n-1]
# - Bottom row: all alphabet[n-1]
# - Left column: all alphabet[n-1]
# - Right column: all alphabet[n-1]
```

---

## ✨ Key Learning Highlights

This problem demonstrates **advanced algorithmic thinking** and **pattern construction**:

### **Two-Phase Mirror Construction**
```python
# Phase 1: Build top half + middle
while k >= 1:
    left += alphabet[k]           # Accumulate left border
    right = alphabet[k] + right   # Accumulate right border (prepend)
    print(left + alphabet[k] * m + right)  # Construct row
    
# Phase 2: Mirror bottom half
while k <= n - 1:
    left = left[:-1]             # Trim rightmost from left
    right = right[1:]            # Trim leftmost from right  
    print(left + alphabet[k] * m + right)  # Use existing structure
```

### **Progressive String Building**
```python
# Left border grows by appending
left = ""
left += "D"    # "D"
left += "C"    # "DC"  
left += "B"    # "DCB"

# Right border grows by prepending
right = ""
right = "D" + right    # "D"
right = "C" + right    # "CD"
right = "B" + right    # "BCD"
```

### **Mathematical Pattern Recognition**
```python
# Center width calculation
m = 2 * n - 1    # Initial width
m -= 2           # Decrease by 2 each row going in
m += 2           # Increase by 2 each row going out

# Layer index management
k = n - 1        # Start from outermost layer index
k -= 1           # Move inward (k goes: n-1, n-2, ..., 1, 0)
k += 1           # Move outward (k goes: 0, 1, ..., n-2, n-1)
```

### **Symmetry Through Structure**
```python
# Top half builds the pattern
# Bottom half reuses the same left/right strings
# But trims them progressively to create mirror effect

# This avoids duplicating the pattern logic
# and ensures perfect symmetry
```

---

## 🎯 Design Philosophy

### **Why Two-Phase Construction Works**
1. **Efficiency**: Reuses calculated border strings instead of recalculating
2. **Symmetry**: Guarantees perfect mirror by using same structure
3. **Clarity**: Separates the building phase from the mirroring phase  
4. **Simplicity**: Avoids complex coordinate calculations or matrix operations

### **Alternative Approaches Considered**
```python
# Approach 1: Matrix-based (initially attempted)
# Create 2D array, fill layer by layer
# Problems: Complex indexing, memory overhead

# Approach 2: Row-by-row calculation (rejected)
# Calculate each row independently
# Problems: Redundant calculations, harder to ensure symmetry

# Approach 3: Recursive pattern (possible but complex)
# Define pattern recursively
# Problems: Stack overhead, less intuitive for this problem

# Chosen approach: Progressive building with mirroring
# Build incrementally, then mirror efficiently
# Benefits: Clear logic, efficient execution, guaranteed symmetry
```

### **Clean Code Principles Applied**
- **Single Responsibility**: Each while loop has distinct purpose
- **Variable Clarity**: `left`, `right`, `m`, `k` have clear meanings
- **Minimal Logic**: No unnecessary complexity or redundant calculations
- **Readable Flow**: Algorithm follows natural construction process

---

## 🔄 Problem-Solving Process

### **Initial Approach: Matrix Method**
```python
# First attempt: Create matrix and fill layer by layer
matrix = [['' for _ in range(2*n-1)] for _ in range(2*n-1)]
# Problem: Complex coordinate calculations
# for layer in range(n):
#     for i in range(layer, 2*n-1-layer):
#         for j in range(layer, 2*n-1-layer):
#             if condition_for_border:
#                 matrix[i][j] = alphabet[n-1-layer]
# Abandoned: Too complicated for this problem
```

### **Breakthrough: Line-by-Line Construction**
```python
# Key insight: Build each row as a string directly
# Instead of filling a matrix, construct the output line by line
# Pattern recognition: Each row = left_border + center_fill + right_border
```

### **Two-Phase Strategy Development**
```python
# Realization: The pattern has perfect symmetry
# Top half (including middle): Borders grow inward
# Bottom half: Mirror of top half with borders shrinking outward
# This allows reusing the border strings instead of recalculating
```

### **Final Implementation Details**
```python
# Critical decisions:
# 1. Use string concatenation for borders
# 2. Calculate center fill width dynamically
# 3. Build top half first, then mirror for bottom
# 4. Use alphabet indexing for letter selection
```

---

## 🎓 Learning Outcomes

* **Advanced Problem Decomposition**: Breaking complex patterns into manageable phases
* **String Manipulation Mastery**: Efficient building, trimming, and concatenation techniques
* **Algorithmic Pattern Recognition**: Identifying symmetry and reusable structures
* **Mathematical Modeling**: Converting visual patterns into mathematical relationships
* **Iterative Development**: Learning from failed approaches to reach elegant solutions
* **Memory-Efficient Design**: Avoiding unnecessary data structures while maintaining clarity
* **Loop Design**: Using while loops effectively for pattern generation

---

## 💡 Developer Reflection

> *"Reflection: This was an interesting problem for me because it really challenged my problem solving skills, that is to say I couldn't just go back into my course notes and find a hint on how to do this, I had to really apply all that I have learned so far and come up with an original solution. At first I thought about using a matrix and filling it in with the desired pattern similar to my sudoku challenge solutions I came up with but that soon became way too over complicated and I had to start again from scratch. After attempting this problem off and on again for about two days I finally got the idea to build the structure in two parts - the top half first and then the second half by having two while loops that will build the structure line by line and adding the desired letter when needed based on what row of the structure we're on. In the end I got it working and I learned a lot more about string manipulation and working with while loops."*

### **Problem-Solving Journey**

**Initial Confidence Challenge:**
- **Beyond Course Material**: First encounter with a problem requiring original algorithmic thinking
- **No Template Available**: Had to synthesize multiple learned concepts into new solution
- **Real Problem-Solving**: Moved from following patterns to creating patterns

**Failed Approach Learning:**
- **Matrix Complexity**: Discovered that 2D arrays aren't always the best choice for geometric patterns
- **Overengineering Recognition**: Learned to identify when an approach is becoming too complex
- **Pivot Courage**: Developed ability to abandon failing approaches and start fresh

**Breakthrough Moment:**
- **Two-Phase Insight**: Recognizing that symmetric patterns can be built in halves
- **Line-by-Line Construction**: Shifting from position-based to structure-based thinking
- **Pattern Reuse**: Understanding how to leverage symmetry for efficiency

### **Technical Skills Developed**

**String Manipulation Mastery:**
- **Progressive Building**: Adding characters to both ends of strings efficiently
- **Dynamic Trimming**: Removing characters systematically to create patterns
- **Concatenation Strategies**: Combining multiple string components into complex patterns

**Algorithmic Thinking Growth:**
- **Phase-Based Design**: Breaking complex problems into manageable sequential steps
- **Symmetry Exploitation**: Using mathematical properties to reduce problem complexity
- **Variable State Management**: Tracking multiple changing values through complex iterations

**Persistence and Iteration:**
- **Multi-Day Problem Solving**: Learning that complex problems require extended thinking time
- **Approach Evolution**: Developing skills to refine and completely restart approaches
- **Original Solution Creation**: Building confidence in creating novel algorithmic solutions

### **Programming Maturity Demonstrated**
This project marked a significant leap from:
- **Following Patterns** → **Creating Patterns**
- **Using Templates** → **Designing Algorithms**  
- **Simple Implementation** → **Complex Problem Decomposition**
- **Course Examples** → **Original Solutions**

The two-day problem-solving journey demonstrates growing comfort with the iterative nature of complex programming challenges and the development of true algorithmic thinking skills.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- Advanced string manipulation techniques
- While loop design and control
- Pattern recognition and algorithmic thinking
- Mathematical modeling of visual patterns
- Symmetric structure construction
- Problem decomposition strategies
