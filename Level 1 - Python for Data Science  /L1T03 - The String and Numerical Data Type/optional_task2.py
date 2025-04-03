# Optional Bonus Task 2
#
# request the name of the user's favourite restaurant and save as string_fav
# request the user's favourite number and save as an integer as int_fav
# print out both with different print statements - assignment is a bit unclear: I interpret it to mean "print both in the same line below the previous statement"
# try to cast string_fav as integer and describe findings in comment

string_fav = input("What is the name of your favourite restaurant? ")
int_fav = int(input("Please enter your favourite number. "))

print(string_fav, end= " ")
print(int_fav) # unsure if you meant to print both in one line under my statement to take in favourite number

int(string_fav) # the program is unable to perform this casting, the result is a ValueError 
                # a word cannot be turned into a whole number. 
                # here is the error code: "invalid literal for int() with base 10"