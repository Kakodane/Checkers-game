# Checkers-game

A console checkers (draughts) game written in Python. You play against a computer opponent driven by the **minimax algorithm with alpha-beta pruning**.

## Features

- Play on an 8x8 board in the terminal
- Two game modes:
  1. **Mandatory capture** – if a capture is available, you must take it
  2. **Optional capture** – captures are allowed but not required
- Multiple (chain) jumps in a single move
- Kings (promotion on reaching the last row)
- AI opponent with a heuristic board evaluation
- Search depth increases automatically in the endgame

## Requirements

- Python 3.8 or newer
- No external dependencies (standard library only)

## How to run

```bash
python main.py
```

Choose the game mode (`1` or `2`) and the game starts.

## How to play

- You play as **`o`** (bottom of the board, moving up); the computer plays as **`x`**.
- Lowercase letters are regular pieces, uppercase letters (`O`, `X`) are kings.
- Rows are labeled `a`–`h` and columns `1`–`8`.
- Each turn is done in two steps:
  1. Pick the piece you want to move from the numbered list (e.g. `1. f-3`).
  2. Pick the destination from the numbered list of legal moves.
- The game ends when one side has no pieces or no legal moves left.

```
    1   2   3   4   5   6   7   8
  ---------------------------------
a |   | x |   | x |   | x |   | x |
  ---------------------------------
b | x |   | x |   | x |   | x |   |
  ---------------------------------
c |   | x |   | x |   | x |   | x |
  ---------------------------------
d |   |   |   |   |   |   |   |   |
  ---------------------------------
e |   |   |   |   |   |   |   |   |
  ---------------------------------
f | o |   | o |   | o |   | o |   |
  ---------------------------------
g |   | o |   | o |   | o |   | o |
  ---------------------------------
h | o |   | o |   | o |   | o |   |
  ---------------------------------
```

## Project structure

| File | Description |
|------|-------------|
| `main.py` | Entry point: mode selection and the main game loop (player turn, then computer turn) |
| `tabla.py` | Board setup and drawing, plus the player's move selection and execution |
| `kompjuter.py` | Move generation, board evaluation, and move simulation for the AI |
| `minimax.py` | Minimax search with alpha-beta pruning |

## How the AI works

- **Search:** minimax with alpha-beta pruning, default depth of 5. When 5 or fewer pieces remain on the board, the depth increases to 7.
- **Evaluation:** the score is the difference between the computer's and the player's position values. It takes into account:
  - piece count and value (kings are worth more than regular pieces)
  - advancement toward the promotion row
  - control of the center
  - edge pieces (safer) and corner pieces (penalized)
  - pieces protected by friendly neighbors
- A win is scored as `+inf`, a loss as `-inf`.
