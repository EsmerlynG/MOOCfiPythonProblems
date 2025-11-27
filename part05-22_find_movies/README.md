# Find Movies

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen) ![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)  

A Python function for searching movies in a database by title. The solution demonstrates **case-insensitive string matching** and list filtering with dictionaries representing structured movie records.  

---

## 📖 Problem Description

Write a function named `find_movies(database: list, search_term: str)` which searches through a movie database and returns only the movies whose title contains the given search term. The search must be **case-insensitive**.  

### Requirements
- **Database Structure**: List of dictionaries, each dictionary representing a movie  
- **Search Behavior**: Matches any part of the movie title, ignoring capitalization  
- **Return Value**: A new list containing only the matched movie dictionaries  

### Example Usage
```python
database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
]

my_movies = find_movies(database, "python")
print(my_movies)
````

**Sample Output:**

```
[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
 {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
```

---

## 💻 Code Implementation

```python
# Write your solution here
def find_movies(database: list, search_term: str):
    found_movies = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            found_movies.append(movie)
    return found_movies     

if __name__ == "__main__":
    database = [
        {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
        {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
        {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
    ]
    my_movies = find_movies(database, "python")
    print(my_movies)
```

**Sample Output:**

```
[{'name': 'Gone with the Python', 'director': 'Victor Pything', 'year': 2017, 'runtime': 116}, 
 {'name': 'Pythons on a Plane', 'director': 'Renny Pytholin', 'year': 2001, 'runtime': 94}]
```

---

## 🧠 Algorithm Explanation

### **Case-Insensitive Search**

```python
if search_term.lower() in movie["name"].lower():
    found_movies.append(movie)
```

**Key Insights:**

* `.lower()` ensures both search term and movie title are compared in lowercase.
* Substring matching allows flexible searches (e.g., `"ana"` matches `"Anaconda"` and `"Management"`).
* New list `found_movies` stores results without modifying the original database.

**Time Complexity:** O(n) — where *n* is the number of movies
**Space Complexity:** O(k) — where *k* is the number of matches

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 find_movies.py
```

Or import the function into your own project:

```python
from find_movies import find_movies

results = find_movies(database, "python")
print(f"Found {len(results)} movies")
```

---

## 🧪 Test Cases

```python
# Test case 1: Case-insensitive search
database = [{"name": "Anaconda", "director": "Dir 1", "year": 1997, "runtime": 120}]
assert find_movies(database, "ana")[0]["name"] == "Anaconda"

# Test case 2: Partial matches
database = [{"name": "Management", "director": "Dir 2", "year": 2008, "runtime": 90}]
assert find_movies(database, "ana")[0]["name"] == "Management"

# Test case 3: No matches
database = [{"name": "Life of Pi", "director": "Dir 3", "year": 2012, "runtime": 127}]
assert find_movies(database, "python") == []

# Test case 4: Multiple matches
database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
]
matches = find_movies(database, "python")
assert len(matches) == 2
```

---

## ✨ Key Learning Highlights

* **String normalization** with `.lower()` for case-insensitive matching
* **Substring search** with `in` operator
* **List filtering pattern**: iterate, check condition, append to results
* **Immutability principle**: function returns a new list, leaving original untouched

---

## 🎯 Design Philosophy

1. **Simplicity**: Straightforward linear search with clear logic
2. **Reusability**: Works for any movie database list with `"name"` key
3. **Separation of Concerns**: Does not modify original data, only returns filtered results
4. **Scalability**: Can easily adapt to support advanced search (e.g., regex, multiple fields)

---

## 🔄 Problem-Solving Process

* Recognized requirement for **case-insensitive search**
* Decided to normalize strings with `.lower()`
* Used `in` operator for substring matching instead of exact equality
* Designed function to **return a new list** instead of modifying original database

---

## 🎓 Learning Outcomes

* Learned how to implement **case-insensitive substring search**
* Practiced **list filtering using conditions**
* Strengthened understanding of **immutable return values**
* Saw parallels to **real-world search features** in apps and databases

---

## 💡 Developer Reflection

> *"This problem showed me how powerful Python’s built-in string and list operations are. By just using `.lower()` and `in`, I could create a flexible search function. It taught me that sometimes the simplest approach is also the most effective."*
