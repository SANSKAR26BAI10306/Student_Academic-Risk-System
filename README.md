# Student Performance Assessment System

## Project Overview
The Student Performance Assessment System is a simple console-based Python application designed to evaluate a student's academic standing based on their attendance percentage and average marks.

## Objective
To help educational institutions quickly identify students who need academic intervention using fundamental logic and conditional evaluation.

## Features
- Interactive console input for student details.
- Evaluation of risk levels (High Risk, Medium Risk, Low Risk).
- Tailored academic recommendations based on risk factor.

## Project Structure
- `app.py`: Collects student details and coordinates the assessment.
- `assessment.py`: Evaluates attendance and marks using the risk rules.
- `report.py`: Prints the academic evaluation report.

## Technologies Used
- Python 3.x

## Python Concepts Used
- Basic Input/Output (`input()`, `print()`)
- Variables and Data Types (`str`, `float`)
- Type Casting (`float()`, `str()`)
- Conditional Statements (`if`, `elif`, `else`)
- Comparison Operators (`<`)
- String Concatenation (`+`)
- Functions, return values, and importing custom modules

## Risk Rules
- **Attendance < 75%**: High Risk (Attendance is low. Must attend classes regularly.)
- **Marks < 50%**: High Risk (Marks are low. Needs revision and practice.)
- **Marks < 60%**: Medium Risk (Improve marks through more practice.)
- **Otherwise**: Low Risk (Good performance. Keep it up.)

## How to Run
Open your terminal or command line and execute:
```bash
python app.py
```

No third-party packages are required.

## Example Output Screenshot
![Program Output](assets/screenshot.png)

## Viva Questions & Answers
1. **Q: Why do we use `float()` on the inputs?**
   *A:* `input()` returns data as a string (`str`). We convert it using `float()` so we can perform numerical comparisons like `< 75`.
2. **Q: Why does `attendance < 75` come first in the `if` statement?**
   *A:* Attendance is a priority threshold. If attendance is low, the program immediately assigns "High Risk" without checking marks.
3. **Q: What happens if attendance is 80 and marks are 55?**
   *A:* The first condition (`attendance < 75`) is false. The second condition (`marks < 50`) is false. The third condition (`marks < 60`) is true, so Risk Level becomes "Medium Risk".

## Future Scope
- Add support for multiple students using loops.
- Implement file handling to save results into a text file.
- Create a Graphical User Interface (GUI) using Tkinter.
