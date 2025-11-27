# Factorials Dictionary Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that calculates and stores the factorials of numbers 1 through n in a dictionary. This solution demonstrates iterative factorial calculation, cumulative computation optimization, and dictionary building with mathematical relationships.

---

## 📖 Problem Description

Write a function `factorials(n: int)` that returns the factorials of the numbers 1 to `n` in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

**Reminder:** The factorial of number `n` is written `n!` and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

### Requirements
- Create a dictionary with integer keys from 1 to n (inclusive)
- Calculate the factorial for each number
- Map each number to its corresponding factorial value
- Return the completed dictionary

### Example Transformation
```python
factorials(5)
# Returns: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
```

**Mathematical Breakdown:**
- 1! = 1
- 2! = 2 * 1 = 2
- 3! = 3 * 2 * 1 = 6
- 4! = 4 * 3 * 2 * 1 = 24
- 5! = 5 * 4 * 3 * 2 * 1 = 120

---

## 💻 Code Implementation

```python
def factorials(n: int):
    numbers = {}
    num = 1
    
    for i in range(1, n + 1):
        num *= i
        numbers[i] = num
    
    return numbers

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
```

**Output:**
```
1
6
120
```

---

## 🧠 Algorithm Explanation

### **The Cumulative Multiplication Strategy**
```python
num = 1  # Start with 1 (factorial base)
for i in range(1, n + 1):
    num *= i        # Multiply by current number
    numbers[i] = num # Store factorial in dictionary
```

**Key Insights:**
- **Cumulative Calculation**: Each factorial builds on the previous one
- **Single Variable Tracking**: `num` keeps running factorial product
- **Efficient Computation**: Avoid recalculating from scratch each time

**Step-by-Step Process:**
1. **Initialize**: Set `num = 1` (factorial starting point) and empty dictionary
2. **Iterate**: Loop from 1 to n (inclusive)
3. **Multiply**: Update `num *= i` to get current factorial
4. **Store**: Map `numbers[i] = num` to save the result
5. **Return**: Send back the completed dictionary

**Time Complexity:** O(n) - Single pass through range calculating each factorial  
**Space Complexity:** O(n) - Dictionary stores n key-value pairs

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 factorials.py
```

Or import the function in your own code:

```python
from factorials import factorials

# Calculate factorials 1-5
result = factorials(5)
print("Factorials 1-5:", result)

# Access specific factorial values
print("3! =", result[3])
print("5! =", result[5])
```

---

## 🧪 Test Cases

```python
# Test case 1: Small range
print("Test 1 - Factorials 1-3:")
print(factorials(3))
# Expected: {1: 1, 2: 2, 3: 6}

# Test case 2: Single factorial
print("\nTest 2 - Just 1!:")
print(factorials(1))
# Expected: {1: 1}

# Test case 3: Standard example
print("\nTest 3 - Factorials 1-5:")
result = factorials(5)
print(result)
print("1! =", result[1])  # 1
print("3! =", result[3])  # 6
print("5! =", result[5])  # 120
# Expected: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

# Test case 4: Larger range
print("\nTest 4 - Factorials 1-7:")
result = factorials(7)
print(result)
print("7! =", result[7])  # 5040
# Expected: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}

# Test case 5: Verify mathematical accuracy
print("\nTest 5 - Mathematical verification:")
result = factorials(4)
print("4! should be 4*3*2*1 =", 4*3*2*1, "| Got:", result[4])
print("Match:", result[4] == 4*3*2*1)
```

---

## ✨ Key Learning Highlights

This problem demonstrates **efficient iterative computation** and **cumulative calculation patterns**:

### **Cumulative vs Recalculation**
```python
# INEFFICIENT - Recalculate each factorial from scratch
def factorials_slow(n: int):
    numbers = {}
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):  # Recalculate every time
            factorial *= j
        numbers[i] = factorial
    return numbers

# EFFICIENT - Build on previous results
def factorials(n: int):
    numbers = {}
    num = 1  # Running product
    for i in range(1, n + 1):
        num *= i  # Use previous result
        numbers[i] = num
    return numbers
```

### **Mathematical Insight**
- **Factorial Property**: n! = n × (n-1)!
- **Cumulative Building**: Each factorial contains all previous calculations
- **Single Pass Efficiency**: Calculate all factorials in one loop

### **Variable Management**
- **`num`**: Tracks running factorial product
- **`i`**: Current number being processed (also dictionary key)
- **`numbers[i] = num`**: Store computed factorial as value

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Efficiency**: O(n) time instead of O(n²) for naive recalculation
2. **Simplicity**: Single loop with cumulative multiplication
3. **Memory Conscious**: Only one extra variable needed for computation
4. **Mathematical Elegance**: Leverages factorial relationship properties

### **Clean Code Principles Applied**
- **Descriptive Names**: `numbers` for dictionary, `num` for running factorial
- **Single Responsibility**: Function calculates and returns factorial dictionary
- **Clear Logic Flow**: Initialize → Iterate → Multiply → Store → Return

---

## 🔄 Problem-Solving Process

### **Initial Misunderstanding**
The first attempt tried to calculate factorials within nested loops:
```python
# WRONG APPROACH - Attempted nested calculation
for n in range(1, n+1):
    for num in range(num, n):
        numbers[n] *= num
```

### **The Overthinking Problem**
- **Complex Nested Logic**: Tried to do factorial math and dictionary building simultaneously
- **Variable Confusion**: Mixed up loop variables and calculation variables
- **Mathematical Errors**: Attempted to multiply ranges incorrectly

### **The Breakthrough Moment**
After 20 minutes of complex attempts, the realization came:
> *"All I needed to do was store the index I was in into a separate variable then after each iteration do `*=` so that I would be getting the factorial of the index I was on"*

### **Final Clean Solution**
```python
def factorials(n: int):
    numbers = {}
    num = 1          # Simple running product
    
    for i in range(1, n + 1):
        num *= i     # Cumulative multiplication
        numbers[i] = num  # Store result
    
    return numbers
```

---

## 🎓 Learning Outcomes

* **Iterative Computation**: Building complex calculations through simple loops
* **Cumulative Algorithms**: Using previous results to compute new ones efficiently
* **Dictionary Construction**: Creating mathematical mappings programmatically
* **Variable Management**: Tracking multiple pieces of state in algorithms
* **Factorial Mathematics**: Understanding and implementing mathematical sequences
* **Optimization Thinking**: Recognizing when to avoid redundant calculations
* **Problem Simplification**: Learning to step back and find simpler approaches

---

## 💡 Developer Reflection

> *"This one stumped me for a while because I made the same mistake I usually do and overthought the problem. I kept trying to do the factorial math adding it to the dictionary at the same time `(for n in range(1, n+1):) for num in range(num, n): numbers[n] *= num)` looking back this makes no sense what so ever, but to give myself some grace I was a little sleep deprived, regardless after attempting to solve this like this for around 20 min I realized I was being a bit extra, and all I needed to do was store the index I was in into a separate variable then after each iteration do `*=` so that I would be getting the factorial of the index I was on, from there I just added the index as the key and the value stored in num which was the factorial into the as the value."*

### **Learning Insights from the Experience**

**The Overthinking Trap:**
- **Complex First Attempts**: Tried to solve everything in nested loops simultaneously
- **Variable Confusion**: Mixed up iteration variables with calculation variables
- **Mathematical Logic Errors**: Attempted incorrect range-based multiplication

**The Breakthrough Process:**
- **Step Back Moment**: Recognized after 20 minutes that the approach was overly complex
- **Simplification Insight**: Realized a single running variable could track factorials
- **Clean Implementation**: Used cumulative multiplication with `*=` operator

**Key Takeaways:**
1. **Sleep and Problem Solving**: Fatigue can lead to overcomplicated thinking
2. **Stepping Back Strategy**: Sometimes the best solution comes from simplifying
3. **Cumulative Patterns**: Many mathematical sequences can be built iteratively
4. **Variable Purpose**: Each variable should have a clear, single responsibility
5. **Self-Grace**: Recognizing that complex first attempts are part of learning

### **Problem-Solving Evolution**
This experience demonstrates the importance of:
- Recognizing when you're overcomplicating a solution
- Taking breaks to reassess your approach
- Understanding that simpler is often better
- Learning from mistakes without harsh self-judgment

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
