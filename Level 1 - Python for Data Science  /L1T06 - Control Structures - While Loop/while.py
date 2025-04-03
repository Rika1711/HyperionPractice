#  Compulsory Task
#
#  Request number from user.
#  -1 will end the program.
#  When program has ended, calculate the average of the numbers entered, excluding -1.
#
num = int(input("Please enter a random number. You can enter -1 to end the program. \n"))
total = 0
i = 0
ave = 0

while num != -1:
    i += 1
    total += num
    num = int(input("Please enter another random number. You can enter -1 to end the program. \n"))
    if num == -1:
        ave = total / i
        break

print(f"The average of all your entered numbers is {ave}.")