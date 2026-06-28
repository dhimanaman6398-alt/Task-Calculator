# Task-Calculator

# 🧮 Task-Calculator (Python Tkinter)

A sleek, responsive, and fully functional graphical user interface (GUI) calculator built using Python's native *Tkinter* library. 

This project demonstrates the use of Tkinter's grid layout, dynamic lambda expressions for event handling, and real-time expression evaluation.

---

## ✨ Features

- *Mathematical Operations:* Supports addition, subtraction, multiplication, and division.
- *Dynamic Display:* Real-time character insertion and display clearing.
- *Responsive Layout:* Grid layout configuration ensuring application elements resize gracefully.
- *Error Handling:* Built-in validation (try-except) block to capture and display mathematical formatting errors cleanly.
- *Clean UI:* Color-coded action buttons (e.g., Green for =, Tomato red for C) to enhance user experience.

---

## 🛠️ Code Architecture & Logic Explanation

The core logic of the application is broken down into structured functions and GUI setups:

### 1. Functional Logic (Functions)
- *click(value)*: Appends the text/number of the pressed button to the current input display string dynamically.
- *clear()*: Clears the entry widget completely by deleting characters from index 0 to tk.END.
- *calculate()*: Uses Python’s built-in eval() function to compute the arithmetic expression from the input field safely wrapped inside a try-except block to catch bad expressions and throw an "Error" string instead of crashing.

### 2. UI Layout Configuration
- *Button Matrix:* Implements a cleanly organized coordinate list [(text, row, col)] iterating programmatically to render each operational key inside a loop.
- *Lambda Bindings:* Uses command=lambda t=text: click(t) to dynamically bind individual button strings to a shared click-handler function.
- *Responsive Weights:* Employs rowconfigure() and columnconfigure() with weights to ensure the layout seamlessly stretches and adapts to custom grid scaling.

---

## 🚀 How to Run Locally

### Prerequisites
Make sure you have Python installed on your system (Python 3.x recommended). Tkinter comes pre-installed with standard Python distributions.


