# Movie Database

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function for managing a movie database using list and dictionary data structures. This solution demonstrates fundamental concepts of data organization, object creation, and database-like operations using built-in Python collections.

---

## 📖 Problem Description

Write a function named `add_movie(database: list, name: str, director: str, year: int, runtime: int)` that adds a new movie object to a movie database. The database is implemented as a list of dictionaries, where each dictionary represents a movie with standardized keys.

### Requirements
- **Database Structure**: List containing movie dictionaries
- **Movie Object**: Dictionary with specific keys: name, director, year, runtime
- **Function Parameters**: Accept all movie details as separate arguments
- **In-place Addition**: Modify the existing database list directly
- **Consistent Schema**: All movies must follow the same dictionary structure

### Example Usage
```python
database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)
```

**Sample Output:**
```
[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, 
 {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
```

**Key Concepts:**
- List as database container
- Dictionary as record structure
- Function-based data manipulation

---

## 💻 Code Implementation

```python
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)
    
if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
```

**Sample Output:**
```
[{'name': 'Gone with the Python', 'director': 'Victor Pything', 'year': 2017, 'runtime': 116}, 
 {'name': 'Pythons on a Plane', 'director': 'Renny Pytholin', 'year': 2001, 'runtime': 94}]
```

**Extended Usage Examples:**
```python
# Building a larger database
database = []
add_movie(database, "The Pythonic Express", "Django Reinhardt", 2019, 128)
add_movie(database, "Life of Pi(thon)", "Guido van Director", 2020, 105)
add_movie(database, "Monty Python's Search for the Holy Code", "Terry Gilliam", 1975, 91)

# Accessing movie data
print(f"First movie: {database[0]['name']}")
print(f"Total movies: {len(database)}")
print(f"Runtime of second movie: {database[1]['runtime']} minutes")
```

---

## 🧠 Algorithm Explanation

### **Dictionary Creation and List Append Pattern**
```python
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Step 1: Create movie dictionary with required schema
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    
    # Step 2: Add movie to database list
    database.append(movie)
```

**Key Insights:**
- **Schema Consistency**: Every movie dictionary has identical key structure
- **Parameter Mapping**: Function arguments directly map to dictionary keys
- **In-place Modification**: Database list is modified directly, not replaced
- **Object Construction**: Dictionary creation encapsulates movie data

**Data Structure Evolution:**
```python
# Empty database
database = []

# After first movie
database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}]

# After second movie  
database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}
]
```

**Time Complexity:** O(1) - Dictionary creation and list append are constant time operations  
**Space Complexity:** O(1) per movie - Each movie requires fixed space regardless of database size

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 movie_database.py
```

Or use the function in your own code:

```python
from movie_database import add_movie

my_database = []
add_movie(my_database, "Your Movie Title", "Director Name", 2023, 120)
print(f"Database now contains {len(my_database)} movies")
```

---

## 🧪 Test Cases

```python
# Test case 1: Single movie addition
database = []
add_movie(database, "Test Movie", "Test Director", 2023, 90)
assert len(database) == 1
assert database[0]["name"] == "Test Movie"
assert database[0]["director"] == "Test Director"
assert database[0]["year"] == 2023
assert database[0]["runtime"] == 90

# Test case 2: Multiple movie additions
database = []
add_movie(database, "Movie 1", "Director 1", 2020, 100)
add_movie(database, "Movie 2", "Director 2", 2021, 110)
add_movie(database, "Movie 3", "Director 3", 2022, 120)
assert len(database) == 3
assert database[2]["name"] == "Movie 3"

# Test case 3: Dictionary key validation
database = []
add_movie(database, "Key Test", "Key Director", 2023, 95)
required_keys = {"name", "director", "year", "runtime"}
assert set(database[0].keys()) == required_keys

# Test case 4: Data type validation
database = []
add_movie(database, "Type Test", "Type Director", 2023, 105)
movie = database[0]
assert isinstance(movie["name"], str)
assert isinstance(movie["director"], str)  
assert isinstance(movie["year"], int)
assert isinstance(movie["runtime"], int)

# Test case 5: Empty string handling
database = []
add_movie(database, "", "", 0, 0)
assert len(database) == 1
assert database[0]["name"] == ""
assert database[0]["director"] == ""

# Test case 6: Database persistence
database = []
add_movie(database, "Persistent Movie", "Persistent Director", 2023, 88)
original_reference = database
add_movie(database, "Second Movie", "Second Director", 2024, 92)
assert original_reference is database  # Same object reference
assert len(original_reference) == 2

# Test case 7: Large database performance
database = []
for i in range(1000):
    add_movie(database, f"Movie {i}", f"Director {i}", 2000 + i % 25, 90 + i % 60)
assert len(database) == 1000
assert database[999]["name"] == "Movie 999"
```

---

## ✨ Key Learning Highlights

This problem demonstrates **fundamental data organization** and **function-based data manipulation**:

### **List-Dictionary Combination Pattern**
```python
# Database structure: List of uniform dictionaries
database = [
    {"name": "Movie 1", "director": "Director 1", "year": 2020, "runtime": 100},
    {"name": "Movie 2", "director": "Director 2", "year": 2021, "runtime": 110},
    {"name": "Movie 3", "director": "Director 3", "year": 2022, "runtime": 120}
]
```

### **Schema Consistency Importance**
```python
# Every movie follows identical structure
movie_schema = {
    "name": str,      # Movie title
    "director": str,  # Director name  
    "year": int,      # Release year
    "runtime": int    # Duration in minutes
}
```

### **In-place Modification vs Return Values**
```python
# This approach: Modifies existing list
def add_movie(database: list, ...):
    database.append(movie)  # Modifies original list

# Alternative approach: Returns new list (not used here)
def add_movie(database: list, ...):
    return database + [movie]  # Creates new list
```

### **Function as Database Operation**
```python
# Function encapsulates database operation
add_movie(database, "Title", "Director", 2023, 120)

# Equivalent manual operation
movie = {"name": "Title", "director": "Director", "year": 2023, "runtime": 120}
database.append(movie)
```

---

## 🎯 Design Philosophy

### **Why This Approach Works**
1. **Simplicity**: Straightforward dictionary creation and list append
2. **Consistency**: Enforces uniform schema across all movie records
3. **Scalability**: Can handle any number of movies without structural changes
4. **Accessibility**: Easy to access individual movies by index or iterate through all

### **Database Design Principles Applied**
```python
# Consistent schema (like database table columns)
required_fields = ["name", "director", "year", "runtime"]

# Record-based storage (like database rows)
each_movie = single_dictionary_with_all_fields

# Collection management (like database table)
database = list_of_movie_records
```

### **Clean Code Principles Applied**
- **Single Responsibility**: Function does one thing - adds a movie
- **Clear Parameters**: Each movie attribute is explicit parameter
- **Consistent Naming**: Dictionary keys match conceptual movie attributes
- **Minimal Logic**: Simple create-and-append pattern

---

## 🔄 Problem-Solving Process

### **Understanding the Requirements**
```python
# Analysis of the problem:
# 1. Need a function that adds movies to a database
# 2. Database is a list (container)
# 3. Each movie is a dictionary (record)
# 4. Dictionary must have specific keys
# 5. Function parameters provide the values
```

### **Solution Strategy**
```python
# Direct approach:
# 1. Create dictionary with required keys
# 2. Map function parameters to dictionary values
# 3. Append dictionary to database list
```

### **Implementation Details**
```python
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Create movie record
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    
    # Add to database
    database.append(movie)
```

### **Alternative Approaches Considered**
```python
# Approach 1: Direct append (less readable)
def add_movie(database, name, director, year, runtime):
    database.append({"name": name, "director": director, "year": year, "runtime": runtime})

# Approach 2: Using constructor pattern (overkill for this problem)
class Movie:
    def __init__(self, name, director, year, runtime):
        self.name = name
        # ... etc

# Approach 3: Validation-enhanced version (beyond requirements)
def add_movie(database, name, director, year, runtime):
    if not isinstance(year, int) or year < 1900:
        raise ValueError("Invalid year")
    # ... validation logic
```

---

## 🎓 Learning Outcomes

* **Data Organization**: Using lists and dictionaries to model real-world entities
* **Schema Design**: Creating consistent data structures for record-based storage
* **Function Design**: Writing functions that modify mutable parameters
* **Database Concepts**: Understanding basic database operations through Python collections
* **Data Access Patterns**: How to structure data for easy retrieval and manipulation
* **Collection Management**: Adding elements to lists and maintaining data integrity
* **Parameter Mapping**: Converting function arguments into structured data

---

## 💡 Developer Reflection

> *"No reflection, all I did was create a dictionary with the keys corresponding to a movie database"*

### **Simplicity as Elegance**

**Direct Implementation:**
- **Straightforward Approach**: Sometimes the most obvious solution is the best solution
- **No Overengineering**: Resisted the temptation to add unnecessary complexity
- **Core Concepts**: Focused on fundamental dictionary creation and list manipulation

**Learning Through Simplicity:**
- **Foundation Building**: Simple problems teach essential patterns used in complex systems
- **Pattern Recognition**: The create-dictionary-append-to-list pattern appears frequently
- **Confidence Building**: Successfully implementing straightforward solutions builds coding confidence

### **Hidden Depth in Simple Solutions**

**What Seems Simple Actually Demonstrates:**
- **Data Modeling**: Representing real-world entities (movies) as data structures
- **Schema Design**: Choosing appropriate keys and value types for movie attributes  
- **Interface Design**: Creating clean function signatures that map to data structure
- **Memory Management**: Understanding how mutable parameters work in Python

**Fundamental Patterns Learned:**
- **Record Creation**: Building structured data objects from individual parameters
- **Collection Management**: Adding items to collections while maintaining structure
- **Data Access**: Setting up data for easy future retrieval and manipulation

### **Building Blocks for Complex Systems**
This simple pattern forms the foundation for:
- **Database Operations**: INSERT statements in SQL work similarly
- **API Design**: REST endpoints often follow create-and-store patterns
- **Data Processing**: ETL pipelines use similar record creation logic
- **Object-Oriented Design**: Constructor patterns mirror this parameter-to-attributes mapping

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.

**Related Concepts:**
- Dictionary creation and manipulation
- List operations and methods
- Function parameter handling
- Data structure design
- Database-like operations with Python collections
