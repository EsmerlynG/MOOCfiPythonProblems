# Phone Book Application, Version 2

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

An enhanced Python phone book application that allows users to store multiple phone numbers per contact. This solution demonstrates advanced dictionary operations with nested data structures, list manipulation within dictionaries, and the evolution from simple key-value storage to complex data relationships.

---

## 📖 Problem Description

Write an improved version of the phone book application where each entry can accommodate multiple phone numbers. The application should work exactly like the previous version, but this time *all* numbers attached to a name should be printed when searching.

### Requirements
- **Multiple Numbers**: Each contact can have multiple phone numbers
- **Search functionality**: Find and display ALL phone numbers for a contact
- **Add functionality**: Store additional numbers for existing contacts
- **Interactive interface**: Same continuous command loop as version 1
- **Backward compatibility**: Same user experience with enhanced capability

### Example Usage
```
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
09-22223333
```

**Key Enhancement:**
- Multiple phone numbers per contact stored and displayed
- Adding to existing contacts appends new numbers instead of replacing

---

## 💻 Code Implementation

```python
def add(people: dict, name: str, phone_num: str):
    if name not in people:
        people[name] = []
    people[name].append(phone_num)

def search(people: dict, name: str):
    if name in people:
        for number in people[name]:
            print(number)
    else:
        print("no number")

def phone_book():
    people = {}
    
    while True:
        command = input("Command (1 search, 2 add, 3 quit): ")
        
        if command == "1":
            name = input("Name: ")
            name = name.lower()
            search(people, name)
        
        elif command == "2":
            name = input("Name: ")
            phone_num = input("Phone: ")
            add(people, name, phone_num)
            print("ok!")
        else:
            break
    
    print("quitting...")

phone_book()
```

**Sample Output:**
```
Command (1 search, 2 add, 3 quit): 2
Name: peter
Phone: 040-5466745
ok!
Command (1 search, 2 add, 3 quit): 2
Name: peter
Phone: 09-22223333
ok!
Command (1 search, 2 add, 3 quit): 1
Name: peter
040-5466745
09-22223333
Command (1 search, 2 add, 3 quit): 3
quitting...
```

---

## 🧠 Algorithm Explanation

### **The Dictionary-of-Lists Architecture**
```python
def add(people: dict, name: str, phone_num: str):
    if name not in people:
        people[name] = []           # Initialize empty list for new contact
    people[name].append(phone_num)  # Add number to contact's list

def search(people: dict, name: str):
    if name in people:
        for number in people[name]: # Iterate through all numbers
            print(number)           # Print each number on separate line
    else:
        print("no number")
```

**Key Insights:**
- **Nested Data Structure**: Dictionary keys map to lists of phone numbers
- **Dynamic List Growth**: Lists expand automatically as numbers are added
- **Initialization Pattern**: Check existence before creating new list
- **Iteration Strategy**: Loop through all numbers for comprehensive display

**Data Structure Evolution:**
```python
# Version 1: Simple key-value pairs
people = {"peter": "040-5466745"}

# Version 2: Key-list pairs  
people = {"peter": ["040-5466745", "09-22223333"]}
```

**Time Complexity:** O(1) for add operations, O(n) for search display (n = numbers per contact)  
**Space Complexity:** O(m×n) - where m is contacts and n is average numbers per contact

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 phonebook_v2.py
```

The program will start immediately and prompt for commands:

```python
# The application runs as a standalone program
# Same interface as version 1, but with enhanced functionality
# Add multiple numbers to the same contact to see the difference
```

---

## 🧪 Test Cases

```python
# Test case 1: Single number per contact
# Command: 2
# Name: alice
# Phone: 123-456-7890
# Expected: "ok!"
# Command: 1
# Name: alice
# Expected: "123-456-7890"

# Test case 2: Multiple numbers for same contact
# Command: 2
# Name: bob
# Phone: 111-111-1111
# Command: 2
# Name: bob  
# Phone: 222-222-2222
# Command: 1
# Name: bob
# Expected: 
# 111-111-1111
# 222-222-2222

# Test case 3: Search non-existent contact
# Command: 1
# Name: unknown
# Expected: "no number"

# Test case 4: Mixed single and multiple numbers
# Command: 2 (add single number to contact1)
# Command: 2 (add multiple numbers to contact2)
# Command: 1 (search both contacts)
# Expected: Proper display for each contact type

# Test case 5: Case sensitivity consistency
# Command: 2
# Name: Charlie
# Phone: 555-1234
# Command: 1
# Name: charlie (lowercase)
# Expected: "555-1234"

# Test case 6: Large number of contacts and numbers
# Add 3+ numbers to multiple contacts
# Search each contact
# Expected: All numbers displayed correctly for each contact
```

---

## ✨ Key Learning Highlights

This problem demonstrates **nested data structures** and **data model evolution**:

### **Dictionary-List Combination**
```python
# Data structure progression understanding
people = {
    "peter": ["040-5466745", "09-22223333"],  # List of numbers
    "emily": ["045-1212344"],                 # Single item list
    "john": []                                # Empty list (possible state)
}
```

### **Initialization vs Appending Pattern**
```python
# Critical pattern for nested structures
def add(people: dict, name: str, phone_num: str):
    if name not in people:
        people[name] = []        # MUST initialize empty list first
    people[name].append(phone_num)  # Then can safely append
```

### **List Iteration for Display**
```python
# Handling variable-length lists
def search(people: dict, name: str):
    if name in people:
        for number in people[name]:  # Works for 1 or many numbers
            print(number)            # Each number on own line
```

### **Backward Compatibility Design**
- Same user interface as version 1
- Enhanced functionality without breaking existing workflow
- Graceful handling of both single and multiple numbers

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Scalability**: Unlimited numbers per contact without structural changes
2. **Consistency**: Same user experience with enhanced capability  
3. **Data Integrity**: Proper initialization prevents runtime errors
4. **Flexibility**: Easy to extend with additional contact information

### **Clean Code Principles Applied**
- **Minimal Changes**: Built on version 1 with targeted enhancements
- **Safe Operations**: Proper existence checking before list operations
- **Clear Logic**: Initialization and appending clearly separated
- **User Experience**: Maintains familiar interface while adding power

---

## 🔄 Problem-Solving Process

### **Understanding the Enhancement**
The key change from version 1:
- Version 1: `people[name] = phone_num` (replacement)
- Version 2: `people[name].append(phone_num)` (accumulation)

### **Data Structure Decision**
```python
# Considered options:
# Option 1: Dictionary of lists (chosen)
people = {"name": ["num1", "num2"]}

# Option 2: List of tuples (rejected - harder to search)
people = [("name", "num1"), ("name", "num2")]

# Option 3: Complex nested dictionaries (overkill for this use case)
```

### **Implementation Strategy**
```python
def add(people: dict, name: str, phone_num: str):
    if name not in people:     # Check if contact exists
        people[name] = []      # Create empty list for new contact  
    people[name].append(phone_num)  # Add number to contact's list
```

### **Critical Implementation Detail**
The initialization check `if name not in people:` is essential:
- Without it: `KeyError` when trying to append to non-existent key
- With it: Safe creation of empty list before first append operation

---

## 🎓 Learning Outcomes

* **Nested Data Structures**: Combining dictionaries and lists effectively
* **Data Model Evolution**: Upgrading simple structures to handle complex relationships
* **Safe Initialization**: Preventing runtime errors in nested structures
* **List Operations**: Appending and iterating within dictionary values
* **Backward Compatibility**: Enhancing functionality without breaking interfaces
* **Algorithm Adaptation**: Modifying existing code for new requirements
* **Pattern Recognition**: Understanding when to use nested vs flat data structures

---

## 💡 Developer Reflection

> *"Reflection: This was a more interesting project because it made me think deeply about how to structure my functions. Getting a function to add and print multiple numbers isn’t difficult, but writing the code so that it’s clear and easy to understand is a different challenge. Simplifying the code while keeping the time complexity as low as possible added another layer of thought. In the end, I approached it in the best way I could, balancing clarity, efficiency, and functionality."*

### **Anticipated Learning Insights**

**Enhanced Complexity:**
- **Nested Structures**: Moving from simple key-value pairs to dictionary-of-lists
- **Data Relationships**: Understanding how to model one-to-many relationships
- **Initialization Logic**: Learning the critical importance of proper list initialization

**Architectural Thinking:**
- **Structure Evolution**: Seeing how data models can grow to meet new requirements
- **Backward Compatibility**: Maintaining familiar user interfaces while adding functionality
- **Scalability Considerations**: Designing for multiple items rather than single values

**Technical Challenges:**
- **Safe Appending**: Understanding why checking existence before appending is crucial
- **Display Logic**: Iterating through variable-length lists for user output
- **Code Reuse**: Building on version 1 rather than starting from scratch

### **Programming Growth Demonstrated**
This project likely provided insights into:
- How small changes in data structure can enable major functionality improvements
- The importance of initialization patterns in nested data structures
- The elegance of solutions that maintain simplicity while adding power
- Understanding when complexity is justified by enhanced capability

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
