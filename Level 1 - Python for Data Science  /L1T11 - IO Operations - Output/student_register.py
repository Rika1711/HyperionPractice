# Compulsory Task 1
#
# Create program that lets students register for exam venue.
# Ask about how many students there will be in total.
# Create a For loop that runs for that number of students.
# Each time it should ask the user for the next student ID number.
# Write each student ID number to  a Text File reg_form.txt
# Include a dotted line after each student ID.

number_of_students = int(input("How many students are registering? "))
student_list = ""

for student in range(number_of_students):
    student_list += input("Enter student ID: ")
    student_list += "\t............\n"
    print(list)

with open('reg_form.txt', 'w', encoding='utf-8') as file:
    file.write(student_list)
