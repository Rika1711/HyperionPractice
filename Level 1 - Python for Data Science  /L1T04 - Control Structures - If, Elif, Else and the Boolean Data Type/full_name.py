# CompulsoryTask1
#
# Request user name
# Perform validation check to see if user entered a full name
# Print error message if no full name:
#   if 0 input: “You haven’t entered anything. Please enter your full name.”
#   if no space included - not at least two names 
#   if < 4 letters: “You have entered less than 4 characters. Please make sure that you have entered your name and surname."
#   if > 25 letters: "You have entered more than 25 characters. Please make sure that you have only entered your full name."
#   else: "Thank you for entering your name."

full_name = input("Hello. Please enter your full name. \n")

while True: # I am addind a while loop to continuusly ask for a full name until all conditions are met
    if len(full_name) < 1:
        full_name = input("You haven’t entered anything. Please enter your full name. \n") 
    elif not " " in full_name:
        full_name = input("You don't seem to have entered more than one name. Please make sure you have entered your name and surname. \n")
    elif len(full_name) < 4:
        full_name = input("You have entered less than 4 characters. Please make sure that you have entered your name and surname. \n")
    elif len(full_name) > 25:
        full_name = input("You have entered more than 25 characters. Please make sure that you have only entered your full name. \n")
    else:
        print("Thank you for entering your name.")
        break