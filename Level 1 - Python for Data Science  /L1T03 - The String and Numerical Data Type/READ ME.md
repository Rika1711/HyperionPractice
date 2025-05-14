# Python Compulsory Tasks 2

This project contains several Python programs that perform string manipulation, basic arithmetic operations, and more advanced calculations.

## Project Structure

* `replace.py`: Python program to replace characters in a string, convert it to uppercase, and reverse it.
* `manipulation.py`: Python program to manipulate a user-entered string, including finding its length, replacing characters, and extracting substrings.
* `numbers.py`: Python program to perform arithmetic operations on three user-entered integers.
* `optional_task1.py`: (Optional) Python program to calculate the area of a triangle given the lengths of its sides.
* `optional_task2.py`: (Optional) Python program to take a user's favorite restaurant and number as input, and demonstrates type casting.

## Compulsory Task 1: `replace.py`

This program manipulates a given string by replacing characters, converting it to uppercase, and reversing it.

###   Code Description

1.  Stores the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." in a string variable.
2.  Replaces all "!" characters with a blank space using the `replace()` method.
3.  Prints the modified sentence.
4.  Converts the modified sentence to uppercase using the `upper()` method.
5.  Prints the uppercase sentence.
6.  Reverses the original sentence using string slicing `[::-1]`.
7.  Prints the reversed sentence.

## Compulsory Task 2: `manipulation.py`

This program takes a sentence from the user and performs various string manipulations.

###   Code Description

1.  Prompts the user to enter a sentence using the `input()` function.
2.  Stores the sentence in a variable called `str_manip`.
3.  Calculates the length of `str_manip` using the `len()` function.
4.  Prints the length of the string.
5.  Finds the last letter of `str_manip`.
6.  Replaces all occurrences of the last letter in `str_manip` with "@" using the `replace()` method.
7.  Prints the modified string.
8.  Extracts the last three characters of `str_manip` using string slicing.
9.  Reverses the last three characters using string slicing.
10. Prints the reversed last three characters.
11. Creates a five-letter word by concatenating the first three characters and the last two characters of `str_manip`.
12. Prints the five-letter word.

## Compulsory Task 3: `numbers.py`

This program takes three integers from the user and performs several arithmetic operations.

###   Code Description

1.  Prompts the user to enter three different integers using the `input()` function.
2.  Converts the input strings to integers using the `int()` function.
3.  Calculates the sum of the three numbers.
4.  Calculates the difference between the first and second number.
5.  Calculates the product of the third and first number.
6.  Calculates the sum of all three numbers divided by the third number.
7.  Prints the results of each calculation.

## Optional Bonus Task 1: `optional_task1.py`

This program calculates the area of a triangle given the lengths of its three sides using Heron's formula.

###   Code Description

1.  Prompts the user to enter the lengths of the three sides of a triangle using the `input()` function.
2.  Converts the input strings to floats using the `float()` function.
3.  Calculates the semi-perimeter (s) of the triangle.
4.  Calculates the area of the triangle using Heron's formula.
5.  Prints the calculated area of the triangle.

### Libraries
* 'math'

## Optional Bonus Task 2: `optional_task2.py`

This program takes the user's favorite restaurant and number as input and demonstrates type casting.

### Code Description

1.  Prompts the user to enter their favorite restaurant and stores it in the `string_fav` variable.
2.  Prompts the user to enter their favorite number.
3.  Converts the input string to an integer using `int()` and stores it in the `int_fav` variable.
4.  Prints the user's favorite restaurant (`string_fav`).
5.  Prints the user's favorite number (`int_fav`).
6.  Includes a comment explaining what happens when you try to cast `string_fav` to an integer and why it occurs.  (e.g., A ValueError occurs because the restaurant name is not a valid integer.)

## How to Run the Programs

1.  Ensure you have Python installed.
2.  Save the Python files (`replace.py`, `manipulation.py`, `numbers.py`, `optional_task1.py`, `optional_task2.py`).
3.  Open a command prompt or terminal.
4.  Navigate to the directory where you saved the files using the `cd` command.
5.  Run each program using the `python` command:
    * For example: `python replace.py`
