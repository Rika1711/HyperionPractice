# Compulsory Task 3
#
# Request 3 different integers from user
# Print
#   Sum of all numbers
#   First number minus second number
#   Third number times first number
#   Of all numbers divided by third number 

num1 = int(input("Please enter 3 different whole numbers. Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

equ1 = num1 + num2 + num3
equ2 = num1 - num2
equ3 = num3 * num1
equ4 = equ1 / num3

print(f"The sum of all these numbers is {equ1}.") # I have added these sentences, because I wanted to practice f-strings
print(f"The first number minus the second number equals {equ2}.")
print(f"The third number multiplied by the first number is {equ3}.")
print(f"The sum of all numbers devided by the third number equals {equ4}.")