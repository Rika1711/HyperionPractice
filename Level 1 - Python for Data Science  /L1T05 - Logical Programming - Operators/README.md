# Python: `award.py`

This program determines the award a person competing in a triathlon will receive based on their total time to complete the three events.

## Code Description

1.  Creates a new Python file named `award.py`.
2.  Prompts the user to enter their times (in minutes) for the swimming, cycling, and running events using the `input()` function.
3.  Converts the input times to integers.
4.  Calculates the total time taken to complete the triathlon by summing the three event times.
5.  Determines the award based on the following criteria:
    * Within the qualifying time (0-100 minutes): "Provincial colours"
    * Five minutes off from the qualifying time (101-105 minutes): "Provincial half scroll"
    * 10 minutes off from the qualifying time (106-110 minutes): "Provincial scroll"
    * More than 10 minutes off from the qualifying time (111+ minutes): "No award"
6.  Prints the total time taken for the triathlon.
7.  Prints the award the participant will receive or "No award".

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python file as `award.py`.
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the file using the `cd` command.
5.  Run the program using the command: `python award.py`
