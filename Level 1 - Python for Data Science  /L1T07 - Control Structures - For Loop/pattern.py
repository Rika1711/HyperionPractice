# Compulsory Task 1
#
# Create program that creates the below pattern using if, else and a single for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
# Attempt 1 - As described in task

stars = "*"

for i in range(0, 9):
    if i < 5:
        print(stars)
        stars = stars + "*"
    else:
        index = 9 - i
        print(stars[:index])

# Attempt 2 - more refined
#
# I wanted to make the program more flexible by adding user input.
# For the output asked for in the example, please enter 5.

print("\nAdditional Attempt")

max_stars = int(input("How many stars to you want in the middle of the pattern? \n"))
max_num = max_stars*2 -1
stars = "*"

for i in range(0,max_num):
    if i < max_stars:
        print(stars)
        stars = stars + "*"
    else:
        index = max_num - i
        print(stars[:index])
