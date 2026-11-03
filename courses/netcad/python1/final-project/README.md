# Tic-Tac-Toe

A command-line Tic-Tac-Toe game built with Python as part of the **Cisco Networking Academy – Python Essentials 1** course.

The game allows a human player to compete against the computer on a 3×3 board.

## Features

- Interactive command-line gameplay.
- Human player uses `O`.
- Computer uses `X`.
- Computer makes its first move in the centre of the board.
- Random computer moves selected from available positions.
- Input validation to prevent invalid moves.
- Prevents players from selecting occupied cells.
- Detects horizontal, vertical, and diagonal victories.
- Detects draws when the board is full without a winner.

## Requirements

- Python 3.11 or later
- No external dependencies.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project directory

```bash
cd tic-tac-toe
```

### 3. Run the game

```bash
python main.py
```

## How to Play

The game displays a numbered 3×3 board.

```text
+-------+-------+-------+
|   1   |   2   |   3   |
+-------+-------+-------+
|   4   |   5   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+
```

- The computer (`X`) makes the first move in the centre.
- The human player (`O`) selects a position by entering a number between 1 and 9.
- The computer selects randomly from the remaining available positions.
- Players take turns until someone wins or the board is full.

A player wins by placing three matching symbols horizontally, vertically, or diagonally.

## Implementation

The project is organized around five main functions:

| Function | Responsibility |
|---|---|
| `display_board()` | Displays the current board. |
| `enter_move()` | Accepts and validates the human player's move. |
| `make_list_of_free_fields()` | Returns the coordinates of unoccupied positions. |
| `victory_for()` | Checks whether a player has won. |
| `draw_move()` | Selects an available position and makes the computer's move. |

The `main()` function coordinates the game flow, manages turns, and determines when the game ends.

## Python Concepts Practised

- Variables and data types
- Lists and nested lists
- Tuples and tuple unpacking
- Functions and return values
- Conditional statements
- `for` and `while` loops
- `break` and `continue`
- Exception handling (`try` / `except`)
- Random number generation
- Input validation
- Function reuse and decomposition

## Learning Objective

This project demonstrates the application of fundamental Python programming concepts to build a small, interactive application. It focuses on problem-solving, logical thinking, data structures, and breaking a program into reusable functions.

---

**Course:** Cisco Networking Academy – Python Essentials 1  
**Project:** Tic-Tac-Toe Final Project  
**Language:** Python