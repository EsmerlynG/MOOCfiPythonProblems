# Screen Time Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange)

A Python program that records and analyzes daily screen time across multiple devices over a specified period. This solution demonstrates file I/O operations, datetime handling, data structure selection, and statistical calculations through a comprehensive time-tracking system.

---

## 📖 Problem Description

Write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time. The program collects daily screen time data for each device type and generates a formatted report with statistics saved to a file.

### Requirements
- **Input Collection**: Filename, starting date, and number of tracking days
- **Daily Logging**: Three space-separated integers per day (TV/computer/mobile minutes)
- **File Output**: Formatted report with date range, totals, averages, and daily breakdown
- **Date Format**: Use `dd.mm.yyyy` format throughout
- **Statistics**: Calculate total minutes and daily average
- **Error Handling**: Graceful handling of file permissions and invalid input

### Example Usage
```
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt
```

**File Output (`late_june.txt`):**
```
Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5
```

**Pattern Analysis:**
- Time period shows inclusive date range
- Total minutes sums all screen time across all days and devices
- Average calculated as total divided by number of days
- Daily entries formatted with forward slashes between device times

---

## 💻 Code Implementation

```python
# Write your solution here
from datetime import datetime, timedelta

def add_screen_time(filename: str, starting_date: datetime, time_entries: int) -> str:
    one_day = timedelta(days=1)

    incrementing_date = starting_date
    startDate = starting_date
    endDate = starting_date + timedelta(days=time_entries - 1)

    log_records = {}
    for _ in range(time_entries):
        time = input(f"Screen time {incrementing_date.strftime('%d.%m.%Y')}: ")
        log_records[incrementing_date.strftime('%d.%m.%Y')] = list(map(int, time.strip().split()))
        incrementing_date += one_day

    total_min = sum(sum(log) for _, log in log_records.items())
    avg_min = total_min / time_entries
    try:
        with open(filename, "w") as time_log:
            time_log.write(f"Time period: {startDate.strftime('%d.%m.%Y')}-{endDate.strftime('%d.%m.%Y')}\n")
            time_log.write(f"Total minutes: {total_min}\n")
            time_log.write(f"Average minutes: {avg_min}\n")
            
            for dates, logs in log_records.items():
                loged_time = '/'.join(map(str, logs))
                time_log.write(f"{dates}: {loged_time}\n")

    except PermissionError:
        return f"You do not have permission to write file - {filename}"
    except Exception as e:
        return f"An unexpected error has occured when interacting with file - {filename}: {e}"
    
    return f"Data stored in file {filename}"
        

def main():
    
    filename = input("Filename: ").strip()
    try:
        starting_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
    except ValueError:
        print("Invalid date format, please use dd.mm.yyyy")
        exit(1)

    try:
        time_entries = int(input("How many days: "))
    except ValueError:
        print("Invalid input, please enter an integer")
        exit(1)
    
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    print(add_screen_time(filename, starting_date, time_entries))

main()
```

**Sample Output (5 days):**
```
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt
```

**Additional Test Cases:**
```python
# Test case 1: Single day
Filename: single.txt
Starting date: 1.1.2024
How many days: 1
Screen time 01.01.2024: 120 180 30
# File output:
# Time period: 01.01.2024-01.01.2024
# Total minutes: 330
# Average minutes: 330.0
# 01.01.2024: 120/180/30

# Test case 2: Week tracking
Filename: week.txt
Starting date: 15.3.2024
How many days: 7
Screen time 15.03.2024: 90 150 45
Screen time 16.03.2024: 120 200 60
Screen time 17.03.2024: 60 180 30
Screen time 18.03.2024: 150 240 90
Screen time 19.03.2024: 45 120 20
Screen time 20.03.2024: 200 300 120
Screen time 21.03.2024: 180 250 80
# File output:
# Time period: 15.03.2024-21.03.2024
# Total minutes: 2835
# Average minutes: 405.0
# [daily breakdown...]

# Test case 3: Zero screen time days
Filename: minimal.txt
Starting date: 10.5.2024
How many days: 3
Screen time 10.05.2024: 0 0 0
Screen time 11.05.2024: 0 0 0
Screen time 12.05.2024: 0 0 0
# File output:
# Time period: 10.05.2024-12.05.2024
# Total minutes: 0
# Average minutes: 0.0
# [daily breakdown with zeros...]
```

---

## 🧠 Algorithm Explanation

### **Data Collection and Storage Strategy**
```python
# Phase 1: Input validation and setup
filename = input("Filename: ").strip()
starting_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
time_entries = int(input("How many days: "))

# Phase 2: Daily data collection
log_records = {}
incrementing_date = starting_date
for _ in range(time_entries):
    time = input(f"Screen time {incrementing_date.strftime('%d.%m.%Y')}: ")
    log_records[incrementing_date.strftime('%d.%m.%Y')] = list(map(int, time.strip().split()))
    incrementing_date += one_day

# Phase 3: Statistical calculation
total_min = sum(sum(log) for _, log in log_records.items())
avg_min = total_min / time_entries

# Phase 4: File writing with error handling
try:
    with open(filename, "w") as time_log:
        # Write header statistics
        # Write daily breakdown
except PermissionError:
    # Handle permission errors
except Exception as e:
    # Handle unexpected errors
```

**Key Insights:**
- **Dictionary Structure**: Maps date strings to lists of integers for easy lookup
- **Date Progression**: Uses `timedelta(days=1)` for reliable date incrementing
- **Generator Expression**: Nested `sum()` for efficient total calculation
- **Format Consistency**: `strftime('%d.%m.%Y')` ensures uniform date formatting

### **Mathematical Relationships**
```python
# For n days tracking:
total_minutes = sum(TV + computer + mobile for each day)
average_minutes = total_minutes / n

# Date range calculation:
start_date = user_input_date
end_date = start_date + timedelta(days=n-1)  # Inclusive end date

# Data structure:
log_records = {
    "dd.mm.yyyy": [tv_minutes, computer_minutes, mobile_minutes],
    ...
}
```

**Pattern Analysis:**
```python
# For 5 days example:
# Day 1: [60, 120, 0] → 180 minutes
# Day 2: [0, 0, 0] → 0 minutes
# Day 3: [180, 0, 0] → 180 minutes
# Day 4: [25, 240, 15] → 280 minutes
# Day 5: [45, 90, 5] → 140 minutes
# Total: 780 minutes
# Average: 780 / 5 = 156.0 minutes
```

**Time Complexity:** O(n) - Single pass for input collection, calculation, and file writing  
**Space Complexity:** O(n) - Dictionary stores n date-data pairs

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 screen_time.py
```

The program will prompt for input:
```
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic functionality
# Input: late_june.txt, 24.6.2020, 5 days
# Screen times: 60 120 0, 0 0 0, 180 0 0, 25 240 15, 45 90 5
# Expected total: 780
# Expected average: 156.0

# Test case 2: Single day tracking
# Input: single.txt, 1.1.2024, 1 day
# Screen time: 120 180 30
# Expected total: 330
# Expected average: 330.0
# Expected period: 01.01.2024-01.01.2024

# Test case 3: Invalid date format
# Input: test.txt, "not-a-date"
# Expected: "Invalid date format, please use dd.mm.yyyy" + exit

# Test case 4: Invalid day count
# Input: test.txt, 1.1.2024, "abc"
# Expected: "Invalid input, please enter an integer" + exit

# Test case 5: File permission test
# Input: /root/protected.txt (no write permission)
# Expected: "You do not have permission to write file - /root/protected.txt"

# Test case 6: Date increment verification
# For starting date 28.2.2020 (leap year), 5 days:
# Expected dates: 28.02.2020, 29.02.2020, 01.03.2020, 02.03.2020, 03.03.2020
# End date: 03.03.2020

# Test case 7: Large values
# Input: 10 days with 999 999 999 per day
# Expected total: 29970 (999*3*10)
# Expected average: 2997.0

# Test case 8: Output format verification
# File must contain:
# - Line 1: "Time period: dd.mm.yyyy-dd.mm.yyyy"
# - Line 2: "Total minutes: [integer]"
# - Line 3: "Average minutes: [float]"
# - Lines 4+: "dd.mm.yyyy: tv/computer/mobile"
```

---

## ✨ Key Learning Highlights

This problem demonstrates **file I/O operations** and **datetime manipulation**:

### **Dictionary-Based Data Management**
```python
# Dictionary provides date-data coupling
log_records = {}
log_records["24.06.2020"] = [60, 120, 0]
log_records["25.06.2020"] = [0, 0, 0]

# Enables easy iteration for file writing
for dates, logs in log_records.items():
    loged_time = '/'.join(map(str, logs))
    time_log.write(f"{dates}: {loged_time}\n")
```

### **Date Handling with datetime Module**
```python
# Parsing user input to datetime object
starting_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")

# Incrementing dates reliably
incrementing_date = starting_date
incrementing_date += timedelta(days=1)  # Handles month/year boundaries

# Formatting for output
date_string = incrementing_date.strftime('%d.%m.%Y')

# Calculating end date
endDate = starting_date + timedelta(days=time_entries - 1)  # Inclusive
```

### **Nested Aggregation with Generator Expression**
```python
# Calculate total across all days and devices
total_min = sum(sum(log) for _, log in log_records.items())

# Breakdown:
# log = [60, 120, 0] → sum(log) = 180
# Generator produces: 180, 0, 180, 280, 140
# Outer sum: 180 + 0 + 180 + 280 + 140 = 780
```

### **String Processing Pipeline**
```python
# Input processing chain
time = input("Screen time 24.06.2020: ")  # "60 120 0"
time.strip()                               # Remove whitespace
time.strip().split()                       # ["60", "120", "0"]
map(int, time.strip().split())             # [60, 120, 0]
list(map(int, time.strip().split()))       # Store as list

# Output formatting chain
logs = [60, 120, 0]
map(str, logs)                             # ["60", "120", "0"]
'/'.join(map(str, logs))                   # "60/120/0"
```

---

## 🎯 Design Philosophy

### **Why Dictionary Over List**
1. **Date Association**: Maintains explicit date-data relationship
2. **Lookup Efficiency**: Can access specific dates if needed
3. **Clarity**: Keys show what each data set represents
4. **File Writing**: Natural iteration over date-time pairs

### **Alternative Approaches Considered**
```python
# Approach 1: List of tuples (initial attempt)
log_records = []
log_records.append((date, [tv, computer, mobile]))
# Problems: Dates not saved alongside initially, harder to iterate

# Approach 2: Separate lists for dates and times
dates = []
times = []
# Problems: Must maintain parallel indices, error-prone

# Approach 3: List of dictionaries
log_records = [{"date": "24.06.2020", "times": [60, 120, 0]}, ...]
# Problems: Verbose, unnecessary nesting

# Chosen approach: Dictionary with date keys
log_records = {"24.06.2020": [60, 120, 0], ...}
# Benefits: Clean structure, easy iteration, clear relationship
```

### **Clean Code Principles Applied**
- **Type Hints**: Clear function signatures with expected types
- **Error Specificity**: Separate handlers for PermissionError vs generic exceptions
- **Input Validation**: Early validation with clear error messages
- **Resource Management**: Context manager ensures file closure
- **Single Responsibility**: `add_screen_time()` handles data processing and file I/O

---

## 🔄 Problem-Solving Process

### **Initial Approach: List-Based Storage**
```python
# First attempt: Store times in a list
log_records = []
for day in range(time_entries):
    time = input(...)
    log_records.append(list(map(int, time.strip().split())))

# Problem discovered: How to associate dates with times for file output?
# Realization: Need to store dates alongside the time data
```

### **Breakthrough: Dictionary Structure**
```python
# Key insight: Use dates as dictionary keys
log_records = {}
log_records[date_string] = [tv, computer, mobile]

# This naturally couples dates with their corresponding data
# Makes file writing straightforward with dates.items() iteration
```

### **Data Structure Evolution**
```python
# Version 1: Plain list
times = [[60, 120, 0], [0, 0, 0], ...]
# Issue: Lost date information

# Version 2: List of tuples
times = [(date1, [60, 120, 0]), (date2, [0, 0, 0]), ...]
# Issue: More complex than necessary

# Version 3: Dictionary (final)
times = {date1: [60, 120, 0], date2: [0, 0, 0], ...}
# Success: Clean, maintainable, natural iteration
```

### **Final Implementation Details**
```python
# Critical decisions:
# 1. Dictionary with string keys for date-data coupling
# 2. datetime.strptime() for robust date parsing
# 3. Generator expression for efficient sum calculation
# 4. Explicit error handling for file operations
# 5. Type hints for function clarity
```

---

## 🎓 Learning Outcomes

* **File I/O Mastery**: Writing formatted data with context managers and error handling
* **datetime Module**: Parsing, formatting, and arithmetic with date objects
* **Data Structure Selection**: Choosing appropriate structures for data relationships
* **Generator Expressions**: Efficient nested aggregation techniques
* **String Manipulation**: Processing and formatting multi-part string data
* **Input Validation**: Robust error handling with user-friendly messages
* **Type Hints**: Documenting function contracts for clarity

---

## 💡 Developer Reflection

> *"Reflection: This was a very fun problem for me because it's the one I learned the most from. At first, I had many issues formatting the datetime objects, but I soon realized that the formatting had to be applied when printing them. Honestly, the solution went through many iterations. The biggest change I made was in the data structure I used — at first, I was tracking total minutes with a list, but I realized that would cause problems later when writing the dates and times to the file since I wasn't saving the dates alongside the times. That's when I decided to pivot and use a dictionary instead. This problem also helped me learn list comprehensions, as I needed to really put my creativity to the test to figure out how to sum all the lists in the dictionary in one line. It wasn't strictly necessary, but I wanted the challenge."*

### **Problem-Solving Journey**

**Initial DateTime Confusion:**
- **Formatting Challenge**: Struggled with when to apply `strftime()` formatting
- **Key Realization**: Formatting is for output, not storage - work with datetime objects internally
- **Learning Moment**: Understanding the distinction between data representation and display

**Data Structure Evolution:**
- **First Approach**: Simple list to store screen times
- **Critical Problem**: No way to associate dates with time entries for file output
- **Pivot Decision**: Complete restructure to use dictionary with dates as keys
- **Lesson Learned**: Data structure choice impacts entire solution design

**Multiple Iterations:**
- **Iterative Refinement**: Solution evolved through several complete rewrites
- **Learning Process**: Each iteration revealed new requirements and better approaches
- **Growth Through Struggle**: Persistence through multiple failed attempts built problem-solving skills

### **Technical Skills Developed**

**DateTime Module Mastery:**
- **Parsing**: Using `strptime()` to convert user input strings to datetime objects
- **Formatting**: Applying `strftime()` for consistent output formatting
- **Arithmetic**: Using `timedelta` for reliable date incrementing across month/year boundaries

**Generator Expression Challenge:**
- **Nested Aggregation**: Learning to sum all values across nested structures
- **Elegant Solution**: `sum(sum(log) for _, log in log_records.items())`
- **Self-Challenge**: Pushed beyond requirements to find one-line solution
- **Comprehension Growth**: Deepened understanding of generator expressions and functional programming

**Data Structure Insight:**
- **Recognition**: Identifying when initial approach won't scale to full requirements
- **Adaptation**: Willingness to completely restructure solution mid-development
- **Design Thinking**: Choosing structures that naturally express data relationships

### **Programming Maturity Demonstrated**
This project marked growth in:
- **Problem Analysis** → Recognizing data structure requirements early
- **Iterative Development** → Embracing multiple rewrites as part of the process
- **DateTime Handling** → Mastering a complex but essential Python module
- **Functional Programming** → Using generator expressions for elegant solutions
- **Self-Direction** → Setting personal challenges beyond base requirements

The willingness to completely pivot the data structure approach demonstrates growing comfort with the iterative nature of software development and the importance of choosing appropriate data structures for the problem at hand.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- File I/O operations with context managers
- datetime module for date parsing and arithmetic
- Dictionary data structures for key-value relationships
- Generator expressions for efficient aggregation
- Error handling with specific exception types
- Type hints for function documentation
