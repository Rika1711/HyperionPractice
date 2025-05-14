# Python: `student_register.py`

This program allows students to register for an exam venue by writing their student ID numbers to a text file.

## Code Description

1.  Creates a new Python file named `student_register.py`.
2.  Asks the user how many students are registering for the exam.
3.  Creates a `for` loop that runs for the specified number of students.
4.  Inside the loop:
    * Asks the user to enter the next student ID number.
    * Opens the "reg\_form.txt" file in append mode ("a").
    * Writes the student ID number to the file.
    * Writes a dotted line ("...") after the student ID.
5.  After the loop finishes, the program does not explicitly close the file, but it is good practice to do so with `outfile.close()`.

## File: `reg_form.txt`

The program creates a text file named "reg\_form.txt" in the same directory as "student\_register.py". This file will contain the student ID numbers, each followed by a dotted line, to be used as an attendance register.

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `student_register.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python student_register.py`
