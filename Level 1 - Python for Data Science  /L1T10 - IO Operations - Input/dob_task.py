# Compulsory Task
#
# Write a program that reads data from DOB.txt.
# Print out data in two different sections, as below:
#   Name
#   Orville Wright
#   Rogelio Holloway
#   etc
#
#   Birthdate
#   21 July 1988
#   13 September 1988
#   etc

with open('DOB.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print("\033[1mName\033[0m") # I am printing the headline bold to make it stand out.

    for line in lines:
        content = line.split()
        name = content[0:2]
        print(" ".join(name))

    print("\n\033[1mBirthdate\033[0m")

    for line in lines:
        content = line.split()
        birthdate = content[2:]
        print(" ".join(birthdate))
