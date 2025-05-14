# Python: `minesweeper.py`

This program takes a grid representing a minefield and returns a new grid where each mine-free spot is replaced by the number of adjacent mines.

## Code Description

1.  Creates a new Python file named `minesweeper.py`.
2.  Defines a function, likely named `calculate_adjacent_mines`, that takes a 2D list (the minefield grid) as input.
3.  The function initializes an empty list or creates a copy of the input grid to store the results.
4.  The function iterates through each cell in the input grid using nested loops.
5.  For each cell:
    * If the cell contains a mine (`#`), it is copied to the result grid as is.
    * If the cell is mine-free (`-`), the function counts the number of adjacent mines.
    * To count adjacent mines, the function checks the eight neighboring cells (North, Northeast, East, Southeast, South, Southwest, West, Northwest).
    * The function uses helper functions (as suggested in the prompt) to:
        * Check if a given row and column index is within the bounds of the grid.
        * Increment the mine count if a neighboring cell contains a mine.
    * The function converts the mine count to a string and places it in the result grid.
6.  The function returns the modified grid.

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `minesweeper.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python minesweeper.py`
