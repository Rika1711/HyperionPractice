# Optional Bonus Task 1
#
# request user to enter length of 3 sides of triangle
# calculate and print area of triangle

import math

side1 = float(input("Please enter the length of all 3 sides of a triangle. Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

s = (side1 + side2 + side3) / 2
area = round(math.sqrt(s * (s - side1) * (s - side2) * (s - side3)), 3) # to improve readability I am rounding the result to 3 places after the decimal point

print(f"The area of your triangle is {area}.") # I am expressing the area in a sentence, because I wanted to practice f-strings