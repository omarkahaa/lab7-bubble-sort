# lab7-bubble-sort

A Python project for visualizing the Bubble Sort algorithm in the terminal.

## Features

- Bubble Sort implementation
- Terminal visualization with screen redraw
- Highlighted compared values
- Optional animation delay
- Type-hinted Python code

## Requirements

No external dependencies are required for the terminal visualization version.

- Python 3.10 or newer

## Run

### Prompted input

python3 main.py

### Command-line input

python3 main.py 14 1 7 13 12 2 8 10 6 5 0 3 11 9 4

### With a custom delay

python3 main.py 14 1 7 13 12 2 8 10 6 5 0 3 11 9 4 --delay 0.20

### Without terminal colors

python3 main.py 14 1 7 13 12 2 8 10 6 5 0 3 11 9 4 --no-color

## How it works

Bubble Sort repeatedly compares adjacent values and swaps them when they are in the wrong order.
This project redraws the terminal after each comparison to make the sorting process easier to follow.

## Project files

- `main.py` -> sorting logic and terminal visualization
- `JOURNAL.md` -> Copilot interaction log
- `REPORT.md` -> short reflection on the lab
- `.github/` -> instructions and journal agent
- `requirements.txt` -> project dependencies

## Notes

This version focuses on the required terminal-first visualization.
Pygame can be explored later as an optional graphics-based extension.
