# Numbers Spelled Out

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Refactored-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that generates a dictionary mapping integers (0-99) to their spelled-out English equivalents. This project demonstrates algorithm evolution from complex list-based solutions to elegant dictionary-driven approaches, showcasing the iterative refinement process in software development.

---

## 📖 Problem Description

Write a function named `dict_of_numbers()` that returns a new dictionary containing numbers from 0 to 99 as keys, with their corresponding English words as values. The solution must use loops and dictionaries rather than manually typing each number.

### Requirements
- **Complete Range**: Cover all numbers from 0 to 99
- **Programmatic Generation**: Use loops and data structures, not manual entry
- **Correct Spelling**: Handle special cases (teens, compound numbers with hyphens)
- **Dictionary Output**: Return a dictionary with integer keys and string values
- **Efficient Implementation**: Avoid unnecessary complexity or redundancy

### Example Usage
```python
numbers = dict_of_numbers()
print(numbers[2])    # "two"
print(numbers[11])   # "eleven" 
print(numbers[45])   # "forty-five"
print(numbers[99])   # "ninety-nine"
print(numbers[0])    # "zero"
```

**Sample Output:**
```
two
eleven
forty-five
ninety-nine
zero
```

**Key Challenges:**
- Handle special cases for teens (10-19)
- Format compound numbers with hyphens (21-99, excluding multiples of 10)
- Generate systematically without manual enumeration

---

## 💻 Code Implementation

### **Final Solution (Optimized)**
```python
def dict_of_numbers():
    numbers = {}
    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
            6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 
            7: "seventy", 8: "eighty", 9: "ninety"}
    
    # Handle 0-9
    for i in range(10):
        numbers[i] = ones[i]
    
    # Handle teens (10-19) - special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"
    
    # Handle 20-99
    for i in range(2, 10):
        numbers[i * 10] = tens[i]  # Multiples of 10
        for j in range(1, 10):
            numbers[i * 10 + j] = tens[i] + "-" + ones[j]  # Compound numbers
    
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[5])    # "five"
    print(numbers[12])   # "twelve" 
    print(numbers[19])   # "nineteen"
    print(numbers[54])   # "fifty-four"
    print(numbers[96])   # "ninety-six"
```

### **First Solution (List-Based Approach)**
```python
def tens_list(tens: list, ones: list):
    string_num = []
    for numbers in tens:
        string_num.append(numbers)
        for num in range(len(ones)):
            tens_num = numbers + "-" + ones[num]
            string_num.append(tens_num)
    return string_num

def complete_numbers_list():
    complete_list = ["zero"]
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    complete_tens = tens_list(tens, ones)
    complete_list += ones[:]
    complete_list += teens[:]
    complete_list += complete_tens[:]
    return complete_list

def dict_of_numbers():
    dictionary = {}
    complete_list = complete_numbers_list()
    for num in range(100):
        dictionary[num] = complete_list[num]
    return dictionary
```

**Sample Output (Both Solutions):**
```
five
twelve
nineteen
fifty-four
ninety-six
```

---

## 🧠 Algorithm Explanation

### **Final Solution Architecture**
```python
def dict_of_numbers():
    # Foundation dictionaries for building blocks
    ones = {0: "zero", 1: "one", ..., 9: "nine"}
    tens = {2: "twenty", 3: "thirty", ..., 9: "ninety"}
    
    # Phase 1: Handle single digits (0-9)
    for i in range(10):
        numbers[i] = ones[i]
    
    # Phase 2: Handle teens (10-19) - irregular patterns
    numbers[10] = "ten"
    # ... manual assignment for irregular forms
    
    # Phase 3: Handle compound numbers (20-99)
    for i in range(2, 10):              # Tens digit (2-9)
        numbers[i * 10] = tens[i]       # Pure tens: 20, 30, 40...
        for j in range(1, 10):          # Ones digit (1-9)
            numbers[i * 10 + j] = tens[i] + "-" + ones[j]  # Compounds: 21, 22...
```

**Key Insights:**
- **Dictionary Lookup**: O(1) access to base number words
- **Mathematical Generation**: `i * 10 + j` formula creates all compound numbers
- **Pattern Recognition**: Teens require special handling due to irregular forms
- **Systematic Construction**: Three distinct phases for different number ranges

### **First Solution Analysis**
```python
# List-based approach with multiple helper functions
def tens_list(tens: list, ones: list):
    # Creates: ["twenty", "twenty-one", "twenty-two", ..., "ninety-nine"]
    # Problem: Fixed ordering assumes specific list concatenation

def complete_numbers_list():
    # Assembles: ["zero"] + ones + teens + compound_tens
    # Issues: Order-dependent, harder to maintain, indirect mapping
```

**Comparison:**
- **First Solution**: 3 functions, list manipulation, order-dependent
- **Final Solution**: 1 function, direct dictionary mapping, mathematical generation

**Time Complexity:** O(1) - Both generate exactly 100 entries  
**Space Complexity:** O(1) - Fixed 100-entry dictionary output

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 number_dictionary.py
```

Or use the function in your own code:

```python
from number_dictionary import dict_of_numbers

numbers = dict_of_numbers()
print(f"The number 42 is spelled: {numbers[42]}")  # "forty-two"
```

---

## 🧪 Test Cases

```python
# Test case 1: Single digits (0-9)
numbers = dict_of_numbers()
assert numbers[0] == "zero"
assert numbers[5] == "five"
assert numbers[9] == "nine"

# Test case 2: Teens (10-19) - irregular patterns
assert numbers[10] == "ten"
assert numbers[11] == "eleven"
assert numbers[12] == "twelve"
assert numbers[15] == "fifteen"
assert numbers[19] == "nineteen"

# Test case 3: Round tens (20, 30, 40, ..., 90)
assert numbers[20] == "twenty"
assert numbers[30] == "thirty"
assert numbers[50] == "fifty"  # Note: "fifty" not "fivety"
assert numbers[90] == "ninety"

# Test case 4: Compound numbers (21-99, excluding multiples of 10)
assert numbers[21] == "twenty-one"
assert numbers[35] == "thirty-five"
assert numbers[67] == "sixty-seven"
assert numbers[99] == "ninety-nine"

# Test case 5: Complete range validation
numbers = dict_of_numbers()
assert len(numbers) == 100
assert all(i in numbers for i in range(100))

# Test case 6: Hyphen formatting
compound_numbers = [numbers[i] for i in range(21, 100) if i % 10 != 0]
assert all("-" in num for num in compound_numbers)

# Test case 7: No hyphens in non-compound numbers
non_compounds = [numbers[i] for i in range(20) or i % 10 == 0 for i in range(20, 100)]
assert all("-" not in num for num in [numbers[i] for i in range(20)])
assert all("-" not in num for num in [numbers[i] for i in range(20, 100, 10)])

# Test case 8: Specific edge cases
assert numbers[40] == "forty"   # Not "fourty"
assert numbers[50] == "fifty"   # Not "fivety"
assert numbers[80] == "eighty"  # Not "eightty"
```

---

## ✨ Key Learning Highlights

This problem demonstrates **algorithm evolution** and **data structure optimization**:

### **Dictionary vs List-Based Approaches**
```python
# List approach: Order-dependent, indirect access
complete_list = ["zero"] + ones + teens + compound_tens
dictionary[num] = complete_list[num]  # Relies on correct ordering

# Dictionary approach: Direct mapping, mathematical generation  
numbers[i * 10 + j] = tens[i] + "-" + ones[j]  # Direct calculation
```

### **Mathematical Pattern Recognition**
```python
# Compound number generation formula
for i in range(2, 10):          # Tens place: 2,3,4,5,6,7,8,9
    for j in range(1, 10):      # Ones place: 1,2,3,4,5,6,7,8,9
        number = i * 10 + j     # Results: 21,22,23...91,92,93...99
        word = tens[i] + "-" + ones[j]  # "twenty-one", "twenty-two"...
```

### **Special Case Handling**
```python
# Teens require individual handling due to irregular patterns
irregular_teens = {
    10: "ten",      # Not "onety" 
    11: "eleven",   # Not "onety-one"
    12: "twelve",   # Not "twoty" or "twenty-two"
    13: "thirteen", # Not "threety" 
    15: "fifteen"   # Not "fiveteen"
}
```

### **Code Evolution Patterns**
```python
# Version 1: Complex multi-function approach
def dict_of_numbers():
    return {i: complete_numbers_list()[i] for i in range(100)}

# Version 2: Streamlined single-function approach  
def dict_of_numbers():
    # Build dictionary directly with mathematical patterns
    # Handle special cases explicitly
    # Use lookup dictionaries for efficiency
```

---

## 🎯 Design Philosophy

### **Why the Final Solution is Superior**
1. **Clarity**: Mathematical generation is more obvious than list assembly
2. **Maintainability**: Changes to word spellings require single updates
3. **Efficiency**: Direct dictionary construction without intermediate lists
4. **Readability**: Three clear phases match the logical problem structure

### **Refactoring Benefits Demonstrated**
```python
# Before: Multiple functions, complex data flow
tens_list() → complete_numbers_list() → dict_of_numbers()

# After: Single function, clear phases
Phase 1: Handle 0-9
Phase 2: Handle 10-19 (special cases)  
Phase 3: Handle 20-99 (mathematical pattern)
```

### **Clean Code Principles Applied**
- **Single Responsibility**: Each loop handles one number range
- **DRY Principle**: Base dictionaries eliminate repetition
- **Explicit is Better**: Special cases handled explicitly rather than hidden
- **Mathematical Clarity**: Formula-based generation over list manipulation

---

## 🔄 Problem-Solving Process

### **Initial Approach: List Assembly**
```python
# First instinct: Build complete list, then convert to dictionary
complete_list = assemble_all_words()
dictionary = {i: complete_list[i] for i in range(100)}
```

### **Challenges with List Approach**
- **Order Dependency**: Required perfect list ordering
- **Complexity**: Multiple helper functions obscured main logic
- **Maintenance**: Changes required updates in multiple places
- **Indirection**: Number→index→word mapping was not intuitive

### **Breakthrough: Direct Mathematical Mapping**
```python
# Key insight: Generate numbers mathematically, not through list assembly
for tens_digit in range(2, 10):
    for ones_digit in range(1, 10):
        number = tens_digit * 10 + ones_digit
        word = tens_words[tens_digit] + "-" + ones_words[ones_digit]
```

### **Final Refinement**
```python
# Organized into logical phases matching number system structure:
# 1. Single digits (0-9): Direct mapping
# 2. Teens (10-19): Irregular forms require explicit handling  
# 3. Compound numbers (20-99): Mathematical pattern with hyphenation
```

---

## 🎓 Learning Outcomes

* **Algorithm Evolution**: Experience refactoring complex solutions into elegant ones
* **Data Structure Selection**: Understanding when dictionaries outperform lists
* **Pattern Recognition**: Identifying mathematical relationships in problem domains
* **Code Simplification**: Techniques for reducing complexity while maintaining functionality
* **Special Case Handling**: Balancing systematic generation with irregular exceptions
* **Mathematical Generation**: Using arithmetic to create systematic data structures
* **Refactoring Skills**: Process of improving code structure without changing behavior

---

## 💡 Developer Reflection

> *"Reflection: This first solution was a very daunting challenge to complete, mainly because I was having a lot of trouble figuring out how to even begin. I didn't know what data structure to use at first, but eventually I settled on lists. At the time it made sense to me, although later on I ended up refactoring my solution and using dictionaries instead. With the list idea, I kind of brute forced my way to the solution, but it taught me a lot—mainly how to manipulate lists in new and creative ways. Obviously though, I realized this solution was way too overcomplicated, so I decided to try something new. I deleted all my code and started fresh, this time using dictionaries, which is what led me to my final solution. The trickiest part of this approach was the final for loop, mostly because of the bit of math needed to get the correct numbers to appear, but other than that it turned out to be a fairly simple solution once I stopped overcomplicating it."*

### **Evolution of Understanding**

**Initial Data Structure Choice:**
- **First Instinct**: Lists seemed natural for ordered sequences
- **Implementation Challenge**: Complex assembly process with helper functions
- **Realization**: List ordering created unnecessary coupling between components

**Breakthrough Moment:**
- **Key Insight**: Dictionary keys can be generated mathematically
- **Simplification**: Direct number→word mapping eliminates intermediate steps
- **Mathematical Pattern**: `i * 10 + j` generates all compound numbers systematically

**Technical Growth Demonstrated:**
- **Refactoring Courage**: Willingness to completely restart with better approach
- **Pattern Recognition**: Seeing mathematical relationships in linguistic problems  
- **Code Quality Awareness**: Recognizing overcomplication and seeking simplification

### **Problem-Solving Skills Developed**

**Algorithm Design:**
- Moving from brute-force list manipulation to elegant mathematical generation
- Understanding when complexity is necessary vs when it indicates wrong approach
- Learning to identify and handle special cases (teens) within systematic patterns

**Code Organization:**
- Evolution from multiple helper functions to single, clear function
- Balancing systematic generation with explicit special case handling
- Creating self-documenting code through logical phase organization

**Mathematical Thinking:**
- Recognizing that `tens_digit * 10 + ones_digit` generates all two-digit numbers
- Understanding how linguistic patterns map to mathematical relationships
- Using arithmetic to drive systematic data structure construction

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- Dictionary construction and manipulation
- Mathematical pattern recognition in programming
- Algorithm optimization and refactoring
- Special case handling in systematic solutions
- Code evolution and iterative improvement
