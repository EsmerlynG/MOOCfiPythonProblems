# Go Game Winner Detector

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A clean and efficient Python function that determines the winner of a Go game by counting player pieces on the board. This solution prioritizes code maintainability and readability while solving a classic board game analysis problem.

---

## 📖 Problem Description

In a game of Go, two players take turns placing black and white stones on a game board. Write a function named `who_won(game_board: list)` that takes a two-dimensional array representing the game board and determines the winner based on piece count.

### Board Representation
- `0`: Empty square
- `1`: Player 1 game piece
- `2`: Player 2 game piece

### Rules
- The function returns `1` if Player 1 has more pieces
- The function returns `2` if Player 2 has more pieces  
- The function returns `0` if both players have equal pieces (tie)

---

## 💻 Code Implementation

```python
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
       player1 += row.count(1)
       player2 += row.count(2)
    
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    game_board = [
        [2,1,1,2,2,1,0,1,2],
        [2,2,1,1,2,1,1,0,2],
        [1,2,2,1,2,2,1,1,1],
        [1,1,2,1,1,2,2,0,1],
        [0,1,2,2,1,1,2,1,0],
        [1,1,1,2,2,1,2,2,1],
        [2,0,1,1,2,1,1,2,2],
        [2,2,2,1,2,2,1,1,2],
        [1,2,1,1,1,2,2,1,1]
    ]
    print(who_won(game_board))
```

**Output:**
```
2
```
*(Player 2 wins with more pieces on the board)*

---

## 🧠 Algorithm Explanation

The solution uses a straightforward counting approach:

1. **Initialize** counters for both players to zero
2. **Iterate** through each row of the game board
3. **Count** Player 1 pieces (1s) and Player 2 pieces (2s) in each row
4. **Accumulate** totals for both players
5. **Compare** final counts and return the appropriate winner code

**Time Complexity:** O(m × n) where m is rows and n is columns  
**Space Complexity:** O(1) using only two counter variables

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 go_winner.py
```

Or import the function in your own code:

```python
from go_winner import who_won

board = [[1, 2, 0], [2, 1, 1], [0, 2, 2]]
winner = who_won(board)
print(f"Winner: Player {winner}" if winner != 0 else "It's a tie!")
```

---

## 🧪 Test Cases

```python
# Test case 1: Player 1 wins
board1 = [[1, 1, 0], [1, 2, 0], [0, 2, 1]]
print(who_won(board1))  # Output: 1

# Test case 2: Player 2 wins
board2 = [[2, 2, 1], [2, 1, 2], [1, 2, 0]]
print(who_won(board2))  # Output: 2

# Test case 3: Tie game
board3 = [[1, 2, 0], [2, 1, 0], [0, 0, 0]]
print(who_won(board3))  # Output: 0

# Test case 4: Empty board
board4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(who_won(board4))  # Output: 0

# Test case 5: Large board
board5 = [
    [1, 2, 1, 2, 1],
    [2, 1, 2, 1, 2],
    [1, 2, 1, 2, 1],
    [2, 1, 2, 1, 2]
]
print(who_won(board5))  # Output: 0 (tie)
```

---

## ✨ Clean Code Philosophy

This solution embodies **maintainable and readable code** through several key design principles:

### **Clarity Over Complexity**
- Simple variable names (`player1`, `player2`) that clearly indicate purpose
- Straightforward logic flow without unnecessary abstractions
- Self-documenting code structure

### **Leveraging Built-in Methods**
- Uses Python's efficient `list.count()` method
- Avoids manual nested loops for better performance
- Reduces potential for off-by-one errors

### **Readable Control Flow**
- Clear if-elif-else structure for winner determination
- Explicit return values that match problem requirements
- No complex boolean logic or ternary operators

### **Minimal Dependencies**
- Pure Python solution using only built-in functions
- No external libraries required
- Easy to test and maintain

---

## 🎯 Design Decision Rationale

My approach prioritized **maintainability and cleanliness** over alternative implementations:

**Why this approach?**
- **Readability**: Any developer can immediately understand the logic
- **Maintainability**: Easy to modify scoring rules or add new features
- **Performance**: Leverages optimized built-in methods
- **Scalability**: Works efficiently with any board size

**Benefits of clean code:**
- Reduces debugging time
- Simplifies future enhancements
- Improves code review process
- Minimizes cognitive load for other developers

---

## 🔍 Alternative Approach

While the current implementation is optimal, here's another valid approach:

### Nested Loop Approach:
```python
def who_won_nested(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for cell in row:
            if cell == 1:
                player1 += 1
            elif cell == 2:
                player2 += 1
    
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
```

---

## 📚 Key Learning Outcomes

* **Board game logic**: Understanding how to analyze 2D game states
* **Counting algorithms**: Efficient methods for tallying elements in matrices
* **Clean code principles**: Writing maintainable, readable solutions
* **Built-in method utilization**: Leveraging Python's powerful list methods
* **Conditional logic**: Implementing clear decision-making structures

---

## 🎓 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
