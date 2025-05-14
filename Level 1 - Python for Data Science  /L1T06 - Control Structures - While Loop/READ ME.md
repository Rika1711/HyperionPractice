# Python: `while.py`

This program repeatedly asks the user to enter a number. When the user enters -1, the program stops, calculates the average of the entered numbers (excluding -1), and prints the result.

## Code Description

1.  Creates a new Python file named `while.py`.
2.  Initializes variables `total` and `count` to 0.
3.  Enters a `while` loop that continues indefinitely (`while True`).
4.  Inside the loop:
    * Prompts the user to enter a number using the `input()` function.
    * Converts the input to a float.
    * If the number is -1:
        * Breaks out of the loop.
    * Otherwise:
        * Adds the number to `total`.
        * Increments `count` by 1.
5.  After the loop:
    * If `count` is 0 (meaning no numbers were entered before -1), prints "No numbers entered."
    * Otherwise:
        * Calculates the average by dividing `total` by `count`.
        * Prints the average.

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `while.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python while.py`
