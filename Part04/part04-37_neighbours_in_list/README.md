# MOOC.fi Part 4 Exercise 37 — Longest Series of Neighbours  
**Solution by Esmerlyn Garabito**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Part%204-lightgrey)

---

## 📖 Challenge Description

Given a list of integers, two consecutive items in the list are considered **neighbours** if their difference is exactly 1. For example, the pairs (1, 2) and (56, 55) are neighbours.

Write a function named `longest_series_of_neighbours` that finds the longest consecutive series of neighbours in the list and returns its length.

### Example

For the list `[1, 2, 5, 4, 3, 4]`, the longest series of neighbours is `[5, 4, 3, 4]`, which has length 4.

Example usage:
```python
my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
```

---

## 🧩 Solution Overview

The function iterates through the list, comparing each pair of consecutive numbers to check if their difference is 1 (in either direction). It builds series of neighbours and keeps track of the longest such series encountered.

To handle edge cases, the implementation appends a number that breaks the neighbour pattern at the end of the list to ensure the final series is correctly evaluated.

---

## 💻 Code Implementation

```python
def longest_series_of_neighbours(my_list):
    longest_series = []
    series = []
    pair = my_list[0]
    my_list = my_list[1:]
    my_list.append(my_list[-1] + 2)  # Append break element to finalize last series

    for num in my_list:
        if abs(pair - num) == 1:
            series.append(pair)
        else:
            if len(longest_series) <= len(series):
                series.append(pair)
                longest_series = series
            series = []
        pair = num

    return len(longest_series)

if __name__ == "__main__":
    my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list))
```

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 longest_neighbours.py
```

Or import the function in your own code:

```python
from longest_neighbours import longest_series_of_neighbours

my_list = [1, 2, 5, 4, 3, 4]
result = longest_series_of_neighbours(my_list)
print(f"Longest series length: {result}")
```

---

## 🔍 Areas for Improvement

While the solution works correctly, I identified opportunities to improve the code quality and readability:

* **Simplify logic:** The current solution uses an appended break element to handle the last sequence. This can be avoided by more careful iteration or by using built-in functions like `abs()` earlier.
* **Reduce list manipulation:** Avoid slicing and modifying the input list when possible to improve efficiency and clarity.
* **Use clearer variable names and comments:** To make the code easier to maintain and understand.

In future iterations, I plan to refactor this function focusing on simplicity, better use of Python features, and improving overall maintainability.

---

## ✨ What I Learned

* **List traversal techniques:** Understanding how to efficiently iterate through lists while comparing adjacent elements
* **Edge case handling:** Learning to properly handle the end of sequences and boundary conditions
* **Algorithm optimization:** Recognizing areas where code can be simplified and made more readable
* **Problem decomposition:** Breaking down the neighbour detection logic into manageable steps

---

## 📚 Conclusion

This exercise helped me practice list traversal, conditional logic, and handling edge cases. It also highlighted the importance of writing clean and efficient code and reminded me to review and improve solutions continuously.

---

## 🎓 Course

This challenge was completed as part of **MOOC.fi Python Programming - Part 4**.
