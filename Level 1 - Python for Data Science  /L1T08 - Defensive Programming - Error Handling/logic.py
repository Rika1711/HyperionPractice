# Initials
#
# Take user name and make sure that the following conditions are met:
#   User has input anything at all.
#   User has input at least two names (first name and surname).
#   Only latin characters are used.
#   Each name at least 2 characters long.
# Find and output the initials of the user name.

full_name = input("Enter all of your full name (first name, middle name, surname)\n")

name_entered = False
name_alphabetical = False
name_and_surname = False
name_length = False

# Make sure that the conditions for a valid name are met.

if len(full_name) >= 1:
    name_entered = True
else:
    print("It does not seem like you entered anything.")

if len(full_name.split()) > 1:
    name_and_surname = True
elif name_entered is not False:
    print("It does not seem like you entered a full name.")

for name in full_name.split():
    if name.isalpha() is True:
        name_alphabetical = True
    else:
        print("You entered a character that is not a latin letter.")
        name_alphabetical = False
        break

for name in full_name.split():
    if len(name) >= 2:
        name_length = True
    else:
        print("At least one name you entered is shorter than expected.")
        name_length = False
        break

# Find and print the first letter of each name.

if name_entered is True and name_alphabetical is True and \
    name_and_surname is True and name_length is True:

    full_name = full_name.upper()
    print("Your initials are:", end=" ")

    for name in full_name.split():
        print(name[1], end="")
else:
    print("Please start over.")

# The logical error is that I printed the letter at position 1 instead of 0.
# Why did it not turn into a Runtime error?
#   Program will run but result will be incorrect.
#   Condition for a valid name 'name_length' has to be True.
#   That condition made sure that letter at position 1 has to exist.
