# This example program is meant to demonstrate errors.
#
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
print("Welcome to the error program")   # Syntax error. Python only prints what is within the (). Without it will cause the program to not execute at all.
print("\n")     # Syntax error. Python only prints what is within the (). Without it will cause the program to not execute at all. Program will not execute.
                # Syntax error. Wrong indentation. Program will not execute.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # Runtime error. When declaring a variable you must use '='. Program began executing, that's why it's runtime error.
# Syntax error. Wrong indentation.
age = int(age_str)      # Runtime error. Program started executing but ran into value error. Letters cannot be turned into integers. -> Only write "24" instead.
# Syntax error. Wrong indentation. Program will not execute.

print("I'm " + str(age) + " years old.")    # Runtime error. 'age' has to be cast to str(). Needed because the other arguments in print() are strings. Program will begin executing and then break.
# Syntax error. Wrong indentation. Program will not execute.

# Variables declaring additional years and printing the total years of age
years_from_now = 3      # Runtime error. If 3 is in "" it will become a string. Calculations with strings are not possible. Program will begin executing and then break.
# Syntax error. Wrong indentation. Program will not execute.
total_years = age + years_from_now
# Syntax error. Wrong indentation. Program will not execute.

print("The total number of years: " + str(total_years))     # Syntax error. The print function is missing '()'. Python only prints what is within the (). Without it will cause the program to not execute at all.
# also Logical error. Program will execute but just print "answer_years". Program will run but result will be incorrect.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6     # Runtime error. The program started executing and ran into Name Error. Variable 'total' does not exist. But 'total_years' does.
print(f"In 3 years and 6 months, I'll be {total_months} months old")    # Logical error. Print statement asks for age in 3 years and 6 months. Formula above only adds 3 years. Program will run but result will be incorrect.

#HINT, 330 months is the correct answer
