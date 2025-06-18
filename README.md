# Tetris 2048 Game (Python)

This project implements a hybrid **Tetris + 2048** game using Python. It combines the falling block mechanics of **Tetris** with the number-merging logic of **2048**, resulting in a strategic and interactive game experience. The game is built with **object-oriented design** and leverages the `stddraw` library for graphical rendering.

---

## 🎮 Gameplay Summary

- **Tetrominoes** are made of tiles with numeric values (2 or 4).
- Tiles fall, move, rotate, and hard-drop like traditional Tetris.
- When two tiles with the same value collide, they merge into one tile of **double** the value.
- Full lines are cleared as in Tetris.
- After each lock, the grid applies gravity and merges tiles as in 2048.
- The game continues until tiles reach the top row.

---

## 🔧 Technical Features

- **Tetromino Mechanics**:
  - Random generation of one of 7 shapes
  - Move left, right, down, and hard-drop
  - Rotate 90° if no collision
  - Grid updating after lock
  - Shows "Next Tetromino" preview

- **2048 Mechanics**:
  - Merging adjacent identical tiles
  - Chain merging (e.g., 2→4→8) during gravity
  - Score updates after each merge
  - Floating tiles removed if unsupported

- **Core Components**:
  - `Tile` class: represents an individual tile with value, color, and position
  - `Point` class: handles 2D coordinate movement
  - `Tetromino` classes: manage different shapes and movement rules
  - `GameGrid` class: board logic, collision, merges, score, display
  - `Tetris2048` class: main loop and game state control

- **Additional Features**:
  - Pause/resume with "P" key
  - Light/dark themes
  - Background music support with `playsound` in a daemon thread
  - Game menu for difficulty and theme selection
  - Game over screen with score display

---

## 🧱 Object-Oriented Design

This project demonstrates modular and object-oriented design principles. Each component is separated logically, making it easier to extend, maintain, or test.

---

## 🧪 Educational Purpose

The project is designed for educational purposes, helping students and learners understand:

- Object-oriented programming in Python
- Grid-based games
- GUI using `stddraw`
- Combining multiple game rules into one seamless system
- Using classes, inheritance, and modular game loops

---

## 📦 Requirements

- Python 3.10 or later
- `stddraw` library (Standard Draw for Python)
- `playsound` for optional background music
- All files in the same directory for proper execution

---

## 📜 License

This project may be licensed under the MIT License. Feel free to explore, fork, and modify it for learning or development purposes.

---

Author: [kayipbaliknepo](https://github.com/kayipbaliknepo)
