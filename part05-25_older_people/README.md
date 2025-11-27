# Older People

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen) ![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)  

A Python function to find all people born before a specified year from a list of tuples. This solution demonstrates **filtering a list of tuples** and extracting specific elements based on a condition.  

---

## 📖 Problem Description

Write a function named `older_people(people: list, year: int)` that takes:

1. A list of tuples, where each tuple contains:
   - Name of a person  
   - Year of birth  
2. A target year  

The function should return a **list of names** of all people born **before** the given year.  

### Requirements
- Input: List of tuples `(name, year_of_birth)` and an integer `year`  
- Output: List of names of people born before `year`  
- Must handle any number of people in the list  

### Example Usage
```python
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)
````

**Sample Output:**

```
['Adam', 'Mary']
```

---

## 💻 Code Implementation

```python
# Write your solution here
def older_people(people: list, year: int):
    older = []

    for person in people:
        if person[1] < year:
            older.append(person[0])
    
    return older

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    
    older = older_people(people, 1979)
    print(older)
```

**Sample Output:**

```
['Adam', 'Mary']
```

---

## 🧠 Algorithm Explanation

### **Filtering Older People**

```python
older = []
for person in people:
    if person[1] < year:
        older.append(person[0])
return older
```

**Key Insights:**

* Iterates through each tuple in the list
* Compares the birth year to the target year
* Appends the name of people born earlier than `year`
* Returns a new list of names

**Time Complexity:** O(n) — where *n* is the number of people
**Space Complexity:** O(k) — where *k* is the number of people who meet the condition

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 older_people.py
```

Or import the function into your project:

```python
from older_people import older_people

people = [("Alice", 1990), ("Bob", 1980), ("Charlie", 2000)]
older = older_people(people, 1990)
print(older)  # Output: ['Bob']
```

---

## 🧪 Test Cases

```python
# Test case 1: Standard list
people = [("Adam", 1977), ("Ellen", 1985), ("Mary", 1953), ("Ernest", 1997)]
assert older_people(people, 1979) == ['Adam', 'Mary']

# Test case 2: All people younger
people = [("Alice", 1990), ("Bob", 1995)]
assert older_people(people, 1980) == []

# Test case 3: All people older
people = [("Tom", 1960), ("Jerry", 1950)]
assert older_people(people, 1970) == ['Tom', 'Jerry']

# Test case 4: Mixed ages
people = [("Anna", 1985), ("Brian", 1975), ("Cathy", 1990)]
assert older_people(people, 1980) == ['Brian']
```

---

## ✨ Key Learning Highlights

* Filtering lists based on a **condition**
* Accessing elements of **tuples by index**
* Returning a **new list** without modifying the original data
* Reinforced **handling lists of tuples** from previous problems

---

## 🎯 Design Philosophy

1. **Simplicity**: Linear iteration and conditional check
2. **Clarity**: Easy-to-read loop and append pattern
3. **Reusability**: Works for any list of `(name, year)` tuples
4. **Efficiency**: Single pass through the list

---

## 🔄 Problem-Solving Process

* Identified need to filter based on birth year
* Iterated through list of tuples, checking each year
* Collected names of matching people in a new list
* Returned the filtered list

---

## 🎓 Learning Outcomes

* Practiced **list filtering with tuples**
* Learned **conditional extraction** of tuple elements
* Built on knowledge from **Oldest Person problem**
* Understood how to **return new data structures** based on conditions

---

## 💡 Developer Reflection

> *"No reflection, this was more of the same as the previous problem, reinforcing working with lists of tuples."*
