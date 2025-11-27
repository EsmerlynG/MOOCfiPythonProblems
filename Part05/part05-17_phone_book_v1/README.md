# Phone Book Application, Version 1

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python phone book application that allows users to search for contacts, add new entries, and quit the program through an interactive command-line interface. This solution demonstrates dictionary manipulation, user input handling, and modular function design with a continuous program loop.

---

## 📖 Problem Description

Write a phone book application that provides three main functionalities: searching for contacts, adding new contacts, and quitting the program. The application should run continuously until the user chooses to quit.

### Requirements
- **Search functionality**: Find and display phone numbers by name
- **Add functionality**: Store new name-phone number pairs
- **Replace capability**: Update existing entries with new numbers
- **Interactive interface**: Continuous command loop until quit
- **Case handling**: Handle searches for non-existent contacts

### Example Usage
```
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 3
quitting...
```

**Key Behaviors:**
- Each name can only have one number (replacements allowed)
- Searching for non-existent names returns "no number"
- Adding entries provides confirmation with "ok!"

---

## 💻 Code Implementation

```python
def add(people: dict, name: str, phone_num: str):
    people[name] = phone_num

def search(people: dict, name: str):
    if name in people:
        return people[name]
    
    return "no number"

def phone_book():
    people = {}
    
    while True:
        command = input("Command (1 search, 2 add, 3 quit): ")
        
        if command == "1":
            name = input("Name: ")
            name = name.lower()
            print(search(people, name))
        
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
Command (1 search, 2 add, 3 quit): 1
Name: peter
040-5466745
Command (1 search, 2 add, 3 quit): 3
quitting...
```

---

## 🧠 Algorithm Explanation

### **The Three-Function Architecture**
```python
def add(people: dict, name: str, phone_num: str):
    people[name] = phone_num  # Direct dictionary assignment

def search(people: dict, name: str):
    if name in people:        # Check existence before access
        return people[name]
    return "no number"        # Default for missing entries

def phone_book():
    # Main program loop with user interface
```

**Key Insights:**
- **Modular Design**: Separate functions for each core operation
- **Dictionary Operations**: Direct key-value storage and retrieval
- **Input Validation**: Checking existence before dictionary access
- **Continuous Loop**: `while True` with break condition for user control

**Step-by-Step Process:**
1. **Initialize**: Create empty dictionary `people = {}`
2. **Get Command**: Prompt user for operation choice (1, 2, or 3)
3. **Route Operation**: Execute appropriate function based on input
4. **Handle Results**: Display output and continue loop
5. **Exit Gracefully**: Break loop and show quit message

**Time Complexity:** O(1) for add/search operations (dictionary hash lookup)  
**Space Complexity:** O(n) - where n is the number of stored contacts

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 phonebook.py
```

The program will start immediately and prompt for commands:

```python
# The application runs as a standalone program
# No need to import or call functions manually
# Just run the file and interact with the prompts
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic add and search
# Command: 2
# Name: john
# Phone: 123-456-7890
# Expected: "ok!"
# Command: 1
# Name: john
# Expected: "123-456-7890"

# Test case 2: Search non-existent contact
# Command: 1
# Name: unknown
# Expected: "no number"

# Test case 3: Replace existing entry
# Command: 2
# Name: john
# Phone: 987-654-3210
# Expected: "ok!"
# Command: 1
# Name: john
# Expected: "987-654-3210" (updated number)

# Test case 4: Case sensitivity test
# Command: 2
# Name: Alice
# Phone: 555-1234
# Command: 1
# Name: alice (lowercase)
# Expected: "555-1234" (search converts to lowercase)

# Test case 5: Multiple entries
# Command: 2 (add multiple contacts)
# Command: 1 (search each one)
# Expected: All contacts retrievable by name

# Test case 6: Quit functionality
# Command: 3
# Expected: "quitting..." and program exit
```

---

## ✨ Key Learning Highlights

This problem demonstrates **interactive application design** and **dictionary-based data management**:

### **Modular Function Design**
```python
# Separation of concerns - each function has one responsibility
def add(people: dict, name: str, phone_num: str):
    # Only handles adding entries
    
def search(people: dict, name: str):
    # Only handles searching and return logic
    
def phone_book():
    # Only handles user interface and program flow
```

### **Dictionary Key Management**
```python
# Safe dictionary access pattern
if name in people:          # Check before access
    return people[name]     # Safe retrieval
return "no number"          # Default fallback
```

### **User Interface Design**
- **Clear Prompts**: Descriptive input messages
- **Command Numbers**: Simple numeric choices (1, 2, 3)
- **Immediate Feedback**: Confirmation messages for actions
- **Graceful Exit**: Clean quit message and program termination

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Modularity**: Each function handles a single responsibility
2. **User-Friendly**: Clear prompts and immediate feedback
3. **Data Integrity**: Safe dictionary operations with existence checks
4. **Flexibility**: Easy to extend with additional features

### **Clean Code Principles Applied**
- **Function Names**: `add`, `search`, `phone_book` clearly indicate purpose
- **Parameter Clarity**: Explicit parameter names and types
- **Single Responsibility**: Each function does exactly one thing
- **Error Handling**: Graceful handling of non-existent entries

---

## 🔄 Problem-Solving Process

### **Understanding the Requirements**
The application needed:
1. Continuous operation until quit command
2. Three distinct operations (search, add, quit)
3. Dictionary-based storage for name-number pairs
4. User-friendly command interface

### **Architecture Decision**
```python
# Chose modular approach with three functions
def add()      # Handle adding contacts
def search()   # Handle searching contacts  
def phone_book()  # Handle user interface and main loop
```

### **Implementation Strategy**
```python
def phone_book():
    people = {}  # Local dictionary for contact storage
    while True:  # Continuous operation
        command = input("Command (1 search, 2 add, 3 quit): ")
        # Route to appropriate operation based on input
```

### **Key Design Decisions**
- **Dictionary Choice**: Perfect for key-value pair storage (name → number)
- **Function Separation**: Makes testing and maintenance easier
- **Input Handling**: Numeric commands for simplicity
- **Case Conversion**: `name.lower()` for consistent searching

---

## 🎓 Learning Outcomes

* **Interactive Applications**: Building programs with continuous user interaction
* **Dictionary Operations**: Storing, retrieving, and updating key-value pairs
* **Function Design**: Creating modular functions with clear responsibilities
* **User Interface**: Designing clear prompts and feedback systems
* **Program Flow Control**: Using loops and conditionals for application logic
* **Input Handling**: Processing and routing user commands
* **Error Prevention**: Safe dictionary access patterns

---

## 💡 Developer Reflection

> *"This problem was very straightforward. I did have some issues when it came to mentally visualizing how to get the name and value associated with it out of the dictionary, but I easily got around that after looking back at my notes."*

### **Learning Insights from the Experience**

**Smooth Implementation:**
- **Straightforward Logic**: Problem requirements were clear and easy to understand
- **Familiar Patterns**: Built on previous dictionary knowledge from earlier exercises
- **Quick Resolution**: Minor confusion resolved by reviewing reference materials

**Dictionary Access Challenge:**
- **Mental Visualization**: Initially struggled with conceptualizing key-value retrieval
- **Reference Strategy**: Successfully used notes to clarify dictionary operations
- **Knowledge Application**: Applied previous learning to solve current problem

**Key Takeaways:**
1. **Reference Materials**: Notes and documentation are valuable problem-solving tools
2. **Building on Basics**: Complex applications built from simple dictionary operations
3. **Confidence Building**: Straightforward problems reinforce fundamental concepts
4. **Pattern Recognition**: Similar structures across different programming challenges
5. **Resource Utilization**: Knowing when and how to use available learning resources

### **Technical Growth Demonstrated**
This experience shows:
- **Problem Assessment**: Accurately identifying problem difficulty level
- **Resource Management**: Effectively using notes when needed
- **Incremental Learning**: Building complex applications from simple operations
- **Self-Reliance**: Resolving confusion independently through available resources

The straightforward nature of this problem provided solid reinforcement of dictionary operations and interactive programming concepts.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
