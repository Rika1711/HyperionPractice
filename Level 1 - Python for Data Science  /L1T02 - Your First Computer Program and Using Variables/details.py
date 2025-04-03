# Compulsory Task 2

# request user information:
#    name
#    age
#    house number
#    street name
# print out information in one sentence

name = input("What is your name? ")
age = input("How old are you? ")
house_no = input("What is your house number? ")
street_name = input("In which street do you live? ")
print("Say hello to {}. They are {} years old and live at house number {} on {}." .format(name, age, house_no, street_name))