# Compulsory Task 2
#
# Request a sentence form user and save as str_manip
# Calculate and print the length of str_manip
# Find last letter of str_manip and replace every occurance of that letter with "@" 
# Print last 3 characters in str_manip backwards
# Create 5 letter word that consists of
#   First 3 letters of str_manip
#   last 2 character of str_manip

str_manip = input("Please enter a sentence. ")
print(len(str_manip))

last_letter = str_manip[-1]
print(str_manip.replace(last_letter, "@"))

print(str_manip[-1:-4:-1])

new_word = str_manip[:3] + str_manip[-2:]
print(new_word)