# Course Grading System - Part 4

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python program for processing student course data and generating formatted results in both human-readable and CSV formats. This solution demonstrates file I/O operations, data processing, and multi-format output generation for academic record management.

---

## 📖 Problem Description

Create a program that reads student information, exercise completion data, exam points, and course details from multiple files, then generates two output files: a formatted text report and a CSV file with final grades.

### Requirements
- **Input Files**: 
  - Student information (CSV)
  - Exercises completed (CSV)
  - Exam points (CSV)
  - Course information (TXT)
- **Output Files**:
  - `results.txt` - Formatted report with headers and aligned columns
  - `results.csv` - Semicolon-delimited grade records
- **Processing**: Calculate exercise points, total points, and final grades
- **Formatting**: Aligned columns, proper headers, structured output
- **User Interaction**: Only prompt for filenames, confirm completion

### Example Usage
```
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
Course information: course1.txt
Results written to files results.txt and results.csv
```

**Sample Input - course1.txt:**
```
name: Introduction to Programming
study credits: 5
```

**Sample Output - results.txt:**
```
Introduction to Programming, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
```

**Sample Output - results.csv:**
```
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3
```

**Key Concepts:**
- Multi-file data processing
- Type conversion with `map()`
- Formatted text output
- CSV generation

---

## 💻 Code Implementation

```python
# Read student information
student_file = input("Student information: ")
students = {}
with open(student_file) as f:
    for line in f:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1]

# Read exercises completed
exercise_file = input("Exercises completed: ")
exercises = {}
with open(exercise_file) as f:
    for line in f:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        exercises[parts[0]] = list(map(int, parts[1:]))

# Read exam points
exam_file = input("Exam points: ")
exams = {}
with open(exam_file) as f:
    for line in f:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        exams[parts[0]] = list(map(int, parts[1:]))

# Read course information
course_file = input("Course information: ")
with open(course_file) as f:
    course_name = f.readline().strip().split(': ')[1]
    credits = f.readline().strip().split(': ')[1]

# Calculate results
results = []
for student_id, name in students.items():
    total_exercises = sum(exercises.get(student_id, [0]*8))
    exercise_points = total_exercises // 4
    exam_total = sum(exams.get(student_id, [0]*3))
    total = exercise_points + exam_total
    
    if total < 15:
        grade = 0
    elif total < 18:
        grade = 1
    elif total < 21:
        grade = 2
    elif total < 24:
        grade = 3
    elif total < 28:
        grade = 4
    else:
        grade = 5
    
    results.append((student_id, name, total_exercises, exercise_points, exam_total, total, grade))

# Write results.txt
with open("results.txt", "w") as f:
    f.write(f"{course_name}, {credits} credits\n")
    f.write("=" * 38 + "\n")
    f.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade'}\n")
    
    for result in results:
        student_id, name, total_ex, ex_pts, exam_pts, total, grade = result
        f.write(f"{name:<30}{total_ex:<10}{ex_pts:<10}{exam_pts:<10}{total:<10}{grade}\n")

# Write results.csv
with open("results.csv", "w") as f:
    for result in results:
        student_id, name, _, _, _, _, grade = result
        f.write(f"{student_id};{name};{grade}\n")

print("Results written to files results.txt and results.csv")
```

**Sample Console Output:**
```
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
Course information: course1.txt
Results written to files results.txt and results.csv
```

**Extended Usage Examples:**
```python
# Processing different course files
# Simply run the program and provide different filenames:
# students2.csv, exercises2.csv, exam_points2.csv, course2.txt

# The program handles any number of students
# As long as the file format remains consistent

# Results are always written to:
# - results.txt (formatted report)
# - results.csv (grade data)
```

---

## 🧠 Algorithm Explanation

### **Multi-Source Data Integration Pattern**
```python
# Step 1: Load all data sources into memory
students = {}      # {student_id: name}
exercises = {}     # {student_id: [week1, week2, ...]}
exams = {}        # {student_id: [exam1, exam2, exam3]}

# Step 2: Process and calculate derived values
for each student:
    total_exercises = sum(exercises)
    exercise_points = total_exercises // 4
    exam_total = sum(exams)
    total = exercise_points + exam_total
    grade = calculate_grade(total)

# Step 3: Generate multiple output formats
results.txt: Formatted with aligned columns
results.csv: Semicolon-delimited for data processing
```

**Key Insights:**
- **Dictionary-Based Storage**: Student ID serves as the key across all data structures
- **Efficient Type Conversion**: Using `map()` to convert string data to integers in one step
- **Data Aggregation**: Combining information from multiple sources using common keys
- **Dual Output Generation**: Creating both human-readable and machine-readable formats

**Data Flow:**
```python
# Input phase
CSV files → Parse lines → Split by delimiter → Convert types (map!) → Store in dictionaries

# Processing phase
For each student → Lookup exercises → Lookup exams → Calculate points → Determine grade

# Output phase
Format text report → Write results.txt
Generate CSV records → Write results.csv
```

**Grading Thresholds:**
```
Total Points: 0-14  → Grade 0 (fail)
Total Points: 15-17 → Grade 1
Total Points: 18-20 → Grade 2
Total Points: 21-23 → Grade 3
Total Points: 24-27 → Grade 4
Total Points: 28+   → Grade 5
```

**Time Complexity:** O(n) - Single pass through student records for calculations  
**Space Complexity:** O(n) - Store all student data in dictionaries

---

## 🛠 How to Run

Prepare your input files in the same directory:
- `students1.csv`
- `exercises1.csv`
- `exam_points1.csv`
- `course1.txt`

Run the program:

```bash
python3 course_grading.py
```

Or use with different course files:

```bash
# Program will prompt for filenames
# Enter: students2.csv, exercises2.csv, exam_points2.csv, course2.txt
python3 course_grading.py
```

---

## 🧪 Test Cases

```python
# Test case 1: map() function correctness
parts = ['id', '5', '10', '15', '20']
result = list(map(int, parts[1:]))
assert result == [5, 10, 15, 20]
assert all(isinstance(x, int) for x in result)

# Test case 2: Passing student (grade 3)
total_exercises = 35
exam_total = 14
exercise_points = total_exercises // 4  # 8 points
total = exercise_points + exam_total    # 22 points
assert total == 22

# Test case 3: Failing student (grade 0)
total_exercises = 21
exam_total = 9
exercise_points = total_exercises // 4  # 5 points
total = exercise_points + exam_total    # 14 points
assert total == 14

# Test case 4: Excellent student (grade 5)
total_exercises = 40
exam_total = 20
exercise_points = total_exercises // 4  # 10 points
total = exercise_points + exam_total    # 30 points
assert total == 30

# Test case 5: Grade boundary validation
assert 15 < 18  # Grade 1 threshold
assert 18 < 21  # Grade 2 threshold
assert 21 < 24  # Grade 3 threshold
assert 24 < 28  # Grade 4 threshold

# Test case 6: File output validation
with open("results.txt") as f:
    lines = f.readlines()
    assert "Introduction to Programming" in lines[0]
    assert "=" * 38 in lines[1]
    assert "name" in lines[2]

# Test case 7: CSV structure validation
with open("results.csv") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split(';')
        assert len(parts) == 3
        assert parts[2].isdigit()
```

---

## ✨ Key Learning Highlights

This problem demonstrates **file-based data processing** and **efficient type conversion**:

### **The `map()` Function for Type Conversion**
```python
# Converting multiple string values to integers efficiently
parts = ['id', '5', '10', '15', '20', '8', '12', '18', '22']

# Without map() - verbose and tedious
exercises[parts[0]] = [int(parts[1]), int(parts[2]), int(parts[3]), ...]

# With map() - clean and scalable
exercises[parts[0]] = list(map(int, parts[1:]))

# map() applies int() to every item in parts[1:]
# Returns: [5, 10, 15, 20, 8, 12, 18, 22]
```

### **Multi-File Data Correlation**
```python
# Using student ID as the joining key
students = {id: name}
exercises = {id: [weekly_exercises]}
exams = {id: [exam_scores]}

# Lookup all data for a student
for student_id in students:
    student_name = students[student_id]
    student_exercises = exercises.get(student_id, [])
    student_exams = exams.get(student_id, [])
```

### **String Formatting for Aligned Output**
```python
# Left-aligned with specific column widths
f"{name:<30}{total_ex:<10}{ex_pts:<10}"

# Creates output like:
# pekka peloton                 21        5
# jaana javanainen              27        6

# Dynamic separator generation
"=" * 38  # ======================================
```

### **Dual Format Output Generation**
```python
# Human-readable format (results.txt)
name                          exec_nbr  exec_pts.
pekka peloton                 21        5

# Machine-readable format (results.csv)
12345678;pekka peloton;0
```

---

## 🎯 Design Philosophy

### **Why This Approach Works**
1. **Separation of Concerns**: Read all data first, process second, write last
2. **Efficient Type Conversion**: `map()` function handles bulk conversions elegantly
3. **Dictionary-Based Joining**: Student ID serves as natural join key across datasets
4. **Flexible Output**: Generate multiple formats from same processed data
5. **Error Tolerance**: Use `.get()` with defaults for missing data

### **Data Processing Pipeline**
```python
# Stage 1: Input
Read files → Parse lines → Convert types (map!) → Store in dictionaries

# Stage 2: Processing
Lookup by ID → Calculate points → Determine grades → Build results

# Stage 3: Output
Format text report → Generate CSV → Write to files
```

### **File I/O Best Practices**
```python
# Context managers for automatic file closing
with open(filename) as f:
    # File automatically closed after block

# Skipping header rows
if parts[0] == "id":
    continue

# Default values for missing data
exercises.get(student_id, [0]*8)
```

---

## 🔄 Problem-Solving Process

### **Understanding the Requirements**
```python
# Analysis of the problem:
# 1. Four input files with different formats
# 2. Need to correlate data using student IDs
# 3. Calculate derived values (exercise points, total points, grades)
# 4. Generate two distinct output formats
# 5. Handle potentially missing student data
```

### **Solution Strategy**
```python
# Direct approach:
# 1. Load all data into dictionaries keyed by student ID
# 2. Use map() for efficient type conversion of numeric data
# 3. Process each student's complete record
# 4. Generate formatted text and CSV outputs
# 5. Write results to files
```

### **Implementation Details**
```python
# Key decision: Using map() for type conversion
# Before: exercises[parts[0]] = [int(parts[1]), int(parts[2]), ...]
# After:  exercises[parts[0]] = list(map(int, parts[1:]))

# Benefits:
# - Concise: One line instead of multiple
# - Flexible: Works for any number of values
# - Readable: Clear intent (convert all to int)
# - Efficient: Optimized built-in function
```

### **Alternative Approaches Considered**
```python
# Approach 1: List comprehension (good alternative)
exercises[parts[0]] = [int(p) for p in parts[1:]]

# Approach 2: Manual loop (inefficient)
exercises[parts[0]] = []
for i in range(1, len(parts)):
    exercises[parts[0]].append(int(parts[i]))

# Approach 3: CSV library (more robust)
import csv
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
```

---

## 🎓 Learning Outcomes

* **File I/O Operations**: Reading multiple files, writing formatted output
* **Data Parsing**: Handling CSV and text file formats
* **Type Conversion Mastery**: Using `map()` for efficient bulk conversions
* **Dictionary Operations**: Using dictionaries for data correlation
* **String Formatting**: Creating aligned, formatted text output
* **Data Aggregation**: Combining data from multiple sources
* **Calculation Logic**: Implementing business rules (grading thresholds)
* **Multi-Format Output**: Generating both human and machine-readable formats

---

## 💡 Developer Reflection

> *"I ran into many issues when solving this problem. The main one was that converting the numbers retrieved from the CSV files into integers was overcomplicating the program. I thought long and hard about what I should do, and that's when I remembered seeing the `map()` function in a LeetCode solution some time ago. Once I recalled it, I searched for its documentation and learned how to implement it properly. Using `map()`, I was able to convert all the string values into integers in one step, which solved my issue efficiently. Overall, this was a challenging problem since it involved working with multiple files and required careful data handling. However, it was also a valuable learning experience that pushed me to think beyond what I already knew and to find new, more efficient solutions."*

### **The Learning Journey**

**Initial Struggle:**
- **Type Conversion Complexity**: Converting CSV string data to integers felt cumbersome
- **Repetitive Code**: Writing multiple `int()` conversions manually seemed inefficient
- **Pattern Recognition**: Sensed there must be a more elegant solution
- **Critical Thinking**: Paused to reflect rather than forcing a suboptimal approach

**The Breakthrough:**
- **Memory Recall**: Remembered encountering `map()` in LeetCode solutions
- **Active Research**: Searched Python documentation to understand proper usage
- **Implementation Success**: Applied `map()` to convert entire lists in one step
- **Code Simplification**: Reduced multiple lines to a single elegant expression

**The Transformation:**
```python
# Before: The complicated way
exercises[parts[0]] = [int(parts[1]), int(parts[2]), int(parts[3]), 
                       int(parts[4]), int(parts[5]), int(parts[6]),
                       int(parts[7]), int(parts[8])]

# After: The elegant solution
exercises[parts[0]] = list(map(int, parts[1:]))
```

### **Understanding `map()` Function**

**How `map()` Works:**
```python
# Syntax: map(function, iterable)
# Applies function to every element in iterable

# Example 1: Converting strings to integers
numbers = ['1', '2', '3', '4', '5']
result = list(map(int, numbers))  # [1, 2, 3, 4, 5]

# Example 2: Converting to floats
scores = ['9.5', '8.7', '10.0']
result = list(map(float, scores))  # [9.5, 8.7, 10.0]

# Example 3: Applying custom function
def double(x):
    return x * 2
result = list(map(double, [1, 2, 3]))  # [2, 4, 6]
```

**Why `map()` is Powerful:**
- **Concise**: One line replaces multiple conversions
- **Scalable**: Works for any number of elements
- **Readable**: Clear intent (apply function to all items)
- **Efficient**: Optimized C implementation in CPython

### **Multi-File Processing Challenges**

**Complexity Factors:**
- **Four Different Sources**: Student info, exercises, exams, and course details
- **Format Diversity**: Both CSV (semicolon-delimited) and text (key-value pairs)
- **Data Correlation**: Matching records across files using student IDs
- **Missing Data Handling**: Gracefully dealing with incomplete records
- **Output Duality**: Creating both formatted report and machine-readable CSV

**Problem-Solving Strategy:**
```python
# Load-Process-Write pipeline
Input files → Parse and store → Calculate grades → Generate outputs

# Key insight: Keep data separate until processing phase
# This allows flexible calculations and multiple output formats
```

### **Real-World Application**

**This Pattern Appears Everywhere:**
- **Academic Systems**: Grade calculation and transcript generation
- **Business Reporting**: Combining sales data, inventory, and customer info
- **Data Analytics**: Merging datasets from multiple sources
- **ETL Pipelines**: Extract, Transform (using map!), Load operations

**Professional Skills Developed:**
- **Research Ability**: Finding solutions through documentation
- **Pattern Recognition**: Identifying when to use functional programming tools
- **Code Simplification**: Replacing verbose code with elegant solutions
- **Persistence**: Working through challenges rather than settling for suboptimal code

### **Key Takeaway**

**Growth Through Challenge:**
This problem taught more than just file handling—it demonstrated the importance of:
- **Recognizing inefficiency** in initial solutions
- **Recalling past experiences** (LeetCode) to find better approaches
- **Researching thoroughly** rather than guessing implementations
- **Applying new knowledge** confidently in different contexts

The journey from struggling with type conversion to discovering `map()` mirrors real software development: encountering obstacles, researching solutions, and emerging with cleaner, more efficient code.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- File input/output operations
- CSV parsing and processing
- The `map()` function for type conversion
- Dictionary-based data structures
- String formatting and alignment
- Data aggregation and calculation
- Multi-format report generation
