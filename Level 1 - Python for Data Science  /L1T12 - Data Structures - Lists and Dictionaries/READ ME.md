# Python: `cafe.py`

This program calculates the total stock worth of a cafe, using a menu list, a stock dictionary, and a price dictionary.

## Code Description

1.  Creates a new Python file named `cafe.py`.
2.  Creates a list called `menu` containing at least 4 items in the cafe.
3.  Creates a dictionary called `stock` where the keys are the items from the `menu` list and the values are the corresponding stock quantities.
4.  Creates a dictionary called `price` where the keys are the items from the `menu` list and the values are the corresponding prices.
5.  Initializes a variable `total_stock_worth` to 0.
6.  Iterates through the `menu` list.
7.  In each iteration:
    * Retrieves the stock value from the `stock` dictionary using the current menu item as the key.
    * Retrieves the price value from the `price` dictionary using the current menu item as the key.
    * Calculates the item value by multiplying the stock value by the price value.
    * Adds the item value to the `total_stock_worth`.
8.  Prints the `total_stock_worth`.

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `cafe.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python cafe.py`
