# This example program is meant to demonstrate errors.
#
# There are some errors in this program. 
# Run the program, look at the error messages, and find and fix the errors.


animal = "Lion"   # Runtime error. Program started executing but ran into Name error. When Lion not in "" Python thinks it's another variable. But that variable has never been declared. Needs to be in ""
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Logical error. Program executes fully but just prints '{animal}' instead of the saved string in the variable. f-strings needed.
# Logical error no. 2: animal_type and number_of_teeth have been swapped. Program executes fully but differently than expected.

print(full_spec)    # Syntax Error. print command needs (). Python will only print what is in (). Program will not execute.
