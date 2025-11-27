# The Oldest Person

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen) ![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)  

A Python function to find the oldest person from a list of tuples containing names and birth years. This solution demonstrates working with **lists of tuples** and identifying elements based on specific criteria.  

---

## 📖 Problem Description

Write a function named `oldest_person(people: list)` that takes a list of tuples as input. Each tuple contains:

1. The name of a person  
2. The year of birth of that person  

The function should determine the **oldest person** in the list and return their name.  

### Requirements
- Input: List of tuples `(name, year_of_birth)`  
- Output: Name of the oldest person (earliest year of birth)  
- Must handle any number of people in the list  

### Example Usage
```python
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))
````

**Sample Output:**

```
Mary
```

---

## 💻 Code Implementation

```python
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
```

**Sample Output:**

```
Mary
```

---

## 🧠 Algorithm Explanation

### **Finding the Oldest Person**

```python
oldest = people[0]
for person in people:
    if person[1] < oldest[1]:
        oldest = person
return oldest[0]
```

**Key Insights:**

* Initialize with the first person as the oldest
* Compare birth years to find the smallest (earliest) year
* Return the name of the person with the earliest year
* Works for any size list

**Time Complexity:** O(n) — where *n* is the number of people
**Space Complexity:** O(1) — only a single tuple is stored as `oldest`

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 oldest_person.py
```

Or import the function into your own project:

```python
from oldest_person import oldest_person

people = [("Alice", 1990), ("Bob", 1980), ("Charlie", 2000)]
print(oldest_person(people))  # Output: Bob
```

---

## 🧪 Test Cases

```python
# Test case 1: Standard list
people = [("Adam", 1977), ("Ellen", 1985), ("Mary", 1953), ("Ernest", 1997)]
assert oldest_person(people) == "Mary"

# Test case 2: Single person
people = [("Alice", 1990)]
assert oldest_person(people) == "Alice"

# Test case 3: Multiple people same year
people = [("Tom", 1985), ("Jerry", 1985)]
assert oldest_person(people) == "Tom"

# Test case 4: Negative years (historic cases)
people = [("Pharaoh", -1300), ("King", 1500)]
assert oldest_person(people) == "Pharaoh"
```

---

## ✨ Key Learning Highlights

* Working with **lists of tuples**
* Accessing tuple elements by index
* Using comparison to determine **minimum value**
* Distinguishing between **list of tuples** and matrices

---

## 🎯 Design Philosophy

1. **Simplicity**: Straightforward linear search
2. **Clarity**: Each step clearly identifies the oldest person
3. **Reusability**: Works with any list of name-year tuples
4. **Efficiency**: Single pass through the list

---

## 🔄 Problem-Solving Process

* Identified the need to compare birth years
* Initialized a variable to store the current oldest
* Iterated through the list, updating the oldest as needed
* Returned the name of the oldest person

---

## 🎓 Learning Outcomes

* Learned how to **iterate over lists of tuples**
* Practiced **conditional comparison** of tuple elements
* Clarified the difference between **list of tuples** and **matrix/list of lists**
* Strengthened understanding of **linear search pattern**

---

## 💡 Developer Reflection

> *"This was a fairly simple problem with no real challenge, but it helped me understand how to work with a list of tuples and clarified the difference between a list of tuples and a matrix."*
