# Optional Bonus Task
#
# BMI
#
# Take in the user measurments.
# Calculate and output the BMI using the formula:
#   weight / height**2

user_measurments = input"Enter your weight in kg and height in cm seperated by space ".split()    # Syntax error. Correct: input().split(). Program will not execute.

bmi = float(user_measurments[1])/float(user_measurments[2])**2    # Runtime error. Correct: user_measurments[0] and user_measurments[1]. Program will begin executing and then break.

    print("Your BMI is: ", str(bmi))    # Syntax error. Incorrect indentation. Program will not execute.
# Logical error: Program asked for height in cm rather than meter. The BMI will be incorrect. But, the program will be run completely.
