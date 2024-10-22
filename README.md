# Rule Engine with AST

## Overview
This project implements a rule engine using an Abstract Syntax Tree (AST) to evaluate conditions based on user attributes. The engine supports dynamic rule creation, modification, and evaluation using a database for storage.

## Features
- Build and evaluate rules based on conditions like `age > 30 AND department = 'Sales'`.
- Combine and modify rules dynamically.
- Store rules and their AST representations in a database (SQLite).
- Test cases to verify rule creation and evaluation.

## Requirements
- Python 3.x
- SQLite3

## Setup Instructions
1. Clone the repository or download the project files.
2. Install dependencies (optional):
   ```bash
   pip install sqlite3
