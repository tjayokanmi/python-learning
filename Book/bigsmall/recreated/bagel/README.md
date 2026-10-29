# Bagels

A Python recreation of the **Bagels** logic game from *The Big Book of Small Python Projects* by Al Sweigart.

## About

I recreated this game from the original game's description and rules, but **implemented the program using my own approach and understanding rather than copying the original source code**.

The project was built as a hands-on Python learning exercise, with a focus on understanding program flow, functions, loops, input validation, and refactoring.

## How the Game Works

The computer generates a secret number with three unique digits.

You have **10 attempts** to guess the number.

After each guess, the game provides clues:

* **Fermi** — a digit is correct and in the correct position.
* **Pico** — a digit is correct but in the wrong position.
* **Bagels** — none of the guessed digits appear in the secret number.

After the game ends, you can choose to play again.

## What I Practiced

Through this project, I practiced:

* Functions and function decomposition
* `for` and `while` loops
* Nested loops
* `break` and `return`
* `for...else`
* Lists
* String manipulation
* `join()`
* Membership testing with `in`
* Input validation
* Random number generation
* Constants
* Refactoring
* Program control flow

## Project Structure

```text
bagels/
├── main.py
└── README.md
```

## Running the Game

Make sure Python 3 is installed, then run:

```bash
python main.py
```

Follow the prompts in the terminal to play.

## Learning Note

This project is part of my ongoing Python learning journey.

The goal was not simply to make the game work, but to understand **why the code works**, make implementation decisions independently, and improve the code through refactoring.

The original game concept and rules come from *The Big Book of Small Python Projects* by Al Sweigart. This repository contains my own implementation.
