# OOP-Application

A collection of custom classes built from scratch using OOP concepts in Python — no external libraries used.

---

## Projects

### 1. Matrix (`matrix.py`)
A custom Matrix class that supports basic matrix operations.

| Method | What it does |
|---|---|
| `+`, `-` | Add and subtract matrices |
| `*` | Matrix multiplication |
| `scale()` | Multiply every element by a number |
| `transpose()` | Flip rows and columns |
| `determinant()` | Calculate determinant (recursive) |
| `shape()` | Returns (rows, cols) |

---

### 2. Vector (`vector.py`)
Custom `Vector2D` and `Vector3D` classes for vector operations.

| Method | What it does |
|---|---|
| `+`, `-`, `*` | Add, subtract, scale vectors |
| `magnitude()` | Length of the vector |
| `dot()` | Dot product |
| `cross()` | Cross product |
| `angle_with()` | Angle between two vectors |
| `normalize()` | Unit vector |

---

### 3. ATM Simulator (`atm.py`)
A simple ATM machine simulator with PIN protection.

| Feature | What it does |
|---|---|
| Set PIN | Create a 4-digit PIN |
| Deposit | Add money to balance |
| Withdraw | Withdraw with PIN + balance check |
| Check Balance | View current balance |

---

## OOP Concepts Covered

- **Class & Object** — every project is a user-defined class
- **Constructor** (`__init__`) — initializes object data
- **Operator Overloading** — `+`, `-`, `*`, `==`, `print` work on custom objects
- **Encapsulation** — data and methods bundled inside the class
- **Recursion** — used in matrix determinant calculation

---
