# Python: `dob_task.py`

This program reads data from the "DOB.txt" text file and prints the names and birthdates in a formatted output.

## Code Description

1.  Creates a new Python file named `dob_task.py`.
2.  Opens the "DOB.txt" file in read mode.
3.  Reads all lines from the file.
4.  Initializes two empty lists: `names` and `birthdates`.
5.  Iterates through each line of the file:
    * Splits each line into name and birthdate using a delimiter (e.g., comma or space, depending on the format of "DOB.txt").  The code will need to be adapted slightly depending on the exact delimiter used.
    * Appends the name to the `names` list and the birthdate to the `birthdates` list.
6.  Prints the header "Name".
7.  Prints each name in the `names` list.
8.  Prints the header "Birthdate".
9.  Prints each birthdate in the `birthdates` list.

##  File: DOB.txt

The "DOB.txt" file should be in the same directory as the "dob_task.py" file.  The file should contain name and birthdate information, formatted as follows (the program will need to be adapted slightly depending on the exact format):

Orville Wright, 21 July 1988Rogelio Holloway, 13 September 1988Marjorie Figueroa, 9 October 1988...etc
## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `dob_task.py`.
3.  Create a text file named `DOB.txt` in the same directory as `dob_task.py` and populate it with the data.
4.  Open a command prompt or terminal.
5.  Navigate to the directory where you saved the files using the `cd` command.
6.  Run the program using the command: `python dob_task.py`
