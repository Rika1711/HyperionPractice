# """Triathlon Award"""
#
# Request user input for times (min) of swimming, cycling, running events.
# Calculate and print total time of completion
# Determine award.
#   0-100 min: Provincial colours
#   101-105 min: Provincial half colours
#   106-110 min: Provincial scroll
#   111 + min: No award
# I am to use logical operators like "and" - THIS WAS NEVER MENTIONED IN THE TASK
# Output the award

print("Congratulations on completing a Triathlon. Please enter your times in minutes.")

while True:
    time_swi = input("Swimming time: ")
    time_cyc = input("Cycling time: ")
    time_run = input("Running time: ")
    if time_swi.isdigit() == False or time_cyc.isdigit() == False or time_run.isdigit() == False:
        print("Please only write the time in minutes. Please try again.")
    else:
        time_swi = int(time_swi)
        time_cyc = int(time_cyc)
        time_run = int(time_run)
        break
     
time_total = time_swi + time_cyc + time_run

print(f"Your total time taken for the triathlon is {time_total} minutes.")
award = " "

if time_total <= 100:
    award = "Provincial colours"
elif time_total > 100 and time_total <= 105:
    award = "Provincial half colours"
elif time_total > 105 and time_total <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print(f"Your award is: {award}")
