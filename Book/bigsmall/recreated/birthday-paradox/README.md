# Birthday Paradox Simulation

A Python recreation of the Birthday Paradox Simulation from *The Big Book of Small Python Projects* by Al Sweigart.

This project uses random birthday generation and repeated Monte Carlo simulations to estimate the probability that at least two people in a group share the same birthday.

## About the Project

The Birthday Paradox demonstrates a surprising probability phenomenon: in a group of just 23 people, there is approximately a **50.73% chance** that at least two people share the same birthday.

This program explores that phenomenon experimentally by generating random birthdays and repeating the experiment 100,000 times.

Rather than relying on a direct mathematical calculation, it estimates the probability from the simulation results.

## Features

- Generates random birthdays for a user-defined group.
- Detects duplicate birthdays using Python sets.
- Runs 100,000 independent simulations.
- Estimates the probability of shared birthdays.
- Validates user input and handles invalid entries.
- Displays simulation results in the terminal.

## Technologies Used

- Python 3.11+
- `random` — random birthday generation.
- `datetime` — date and time calculations.
- Python sets — duplicate detection.

No external dependencies are required.

## Project Structure

```text
birthday-paradox/
└── main.py
```

## Getting Started

### Requirements

- Python 3.11 or later.

### Clone the Repository

```bash
git clone https://github.com/tjayokanmi/python-learning.git
```

### Navigate to the Project Directory

```bash
cd python-learning/Book/bigsmall/recreated/birthday-paradox
```

### Run the Program

```bash
python main.py
```

## How It Works

The program follows four main steps:

1. **Birthday Generation:** Generates random dates within a fixed 365-day year.
2. **Duplicate Detection:** Converts the birthday list into a set and compares the lengths to determine whether a duplicate exists.
3. **Simulation:** Repeats the experiment 100,000 times and counts how many experiments produce at least one shared birthday.
4. **Probability Estimation:** Divides the number of successful simulations by the total number of simulations and converts the result to a percentage.

The program uses 1991, a non-leap year, to represent the 365 possible birthdays.

## Example Output

```text
Please enter a number between 1 and 100
23

Number of birthdays: 23
Number of simulations: 100000
Number of successful simulations: 50675
Probability: 50.68%
```

*Note: Results vary slightly between executions because birthdays are generated randomly.*

## Sample Results

The following results were obtained during development:

| Group Size | Simulated Probability | Theoretical Probability |
|---:|---:|---:|
| 1 | 0.00% | 0.00% |
| 23 | 50.68% | 50.73% |
| 50 | 97.06% | 97.04% |

The results demonstrate how repeated random experiments can approximate theoretical probabilities.

## Concepts Practised

Building this project provided practical experience with:

- Functions and code decomposition.
- Lists and sets.
- Random number generation.
- Python's `datetime` and `timedelta`.
- Function arguments and return values.
- Loops and conditional statements.
- Exception handling with `try/except`.
- User input validation.
- Constants and variable scope.
- Python's `if __name__ == "__main__":` entry-point convention.
- Monte Carlo simulation and probability estimation.

## Possible Future Improvements

- Allow users to customise the number of simulations.
- Add automated tests with `pytest`.
- Compare simulated results with mathematically calculated probabilities.
- Explore the effect of different group sizes.

## Author

**Theophilus Jacob**

Python learner and aspiring software engineer.

This project is part of my ongoing journey to strengthen my Python programming skills through practical implementation, experimentation, and independent problem-solving.

**Project repository:** [Birthday Paradox Simulation](https://github.com/tjayokanmi/python-learning/tree/main/Book/bigsmall/recreated/birthday-paradox)