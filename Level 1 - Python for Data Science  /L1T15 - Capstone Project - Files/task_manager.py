# Create a program that manages tasks assigned to users.

#====Define Functions====
# These code blocks define functions, lists
# and dictionaries that will be needed throughout the code.
user_credentials = {}
task_lines = []


def access_user_credentials():
    with open("user.txt", "r+", encoding="utf-8") as user_file:
        for line in user_file:
            (user, password) =  line.split(",")
            user_credentials[user.strip()] = password.strip()


def access_tasks():
    with open("tasks.txt","r+", encoding="utf-8") as task_file:
        for lines in task_file:
            lines = lines.split(", ")
            task_lines.append(lines)


access_user_credentials()

#====Login Section====
# This block of code allows a user to login.
# It displays an error messages when the entered username is wrong
# or when the user name is correct but the password is wrong.

print("\n\033[1m##### Task Manager #####\033[0;0m\n")

while True:
    user_attempt = input("Enter your username: ")
    password_attempt = input("Enter your password: ")

    if user_attempt in user_credentials and\
    user_credentials[user_attempt] == password_attempt:
        print("You have successfully logged in.")
        user_name = user_attempt
        break
    elif user_attempt not in user_credentials:
        print('''Your entered username does not exist.
Try again.''')
    elif user_attempt in user_credentials and\
    user_credentials[user_attempt] != password_attempt:
        print('''Your entered username was correct, but the password was wrong.
Try again.''')
    else:
        print("Something went wrong.")

# This code presents the menu to the user
# and makes sure that the user input is converted to lower case.
while True:
    # This code offers a display menu choice to only the admin:
    # Display statistics.
    if user_name == "admin":
        menu = input('''\n\033[1mSelect one of the following options:\033[0;0m
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
u - all usernames
e - exit
: ''').lower()

    else:
        menu = input('''\n\033[1mSelect one of the following options:\033[0;0m
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # This code block will add a new user to the user.txt file.
    # This code should only run if the admin is logged in.
    # It asks the user confirm the password.
    # Additionally: The code only runs if the username is new.
    if menu == 'r':
        if user_name == "admin":
            new_user = input("Enter username: ")

            if new_user not in user_credentials:
                while True:
                    new_pass = input("Enter password: ")
                    new_pass_confirm  =  input("Confirm your password: ")

                    if new_pass == new_pass_confirm:
                        print("Success.")
                        with open("user.txt", "a+", encoding="utf-8") as new_user_file:
                            new_user_file.write("\n"+new_user+", "+new_pass)
                        access_user_credentials()
                        break
                    else:
                        print("These passwords did not match. Try again.")
            else:
                print("That username already exists.")
        else:
            print("You are not authorised to register new users.")

    # This code block allows a user to add a new task to task.txt file.
    elif menu == 'a':
        while True:
            task_user = input("Enter the username of the person whom the task is assigned to: ")
            if task_user in user_credentials:
                break
            else:
                print("This username does not exist. Try again.")

        task_title = input("Enter the name of the task: ")
        task_description = input("Enter the task description: ")
        task_due = input("When is the task due? ")
        current_date = input("Enter today's date: ")

        with open("tasks.txt", "a+", encoding="utf-8") as new_task_file:
            new_task_file.write("\n"+task_user+", "+task_title+", "+ \
            task_description+", "+current_date+", "+task_due+", No")
        print("Success.")

    # This code block reads the task from task.txt file
    # and prints to the console.
    elif menu == 'va':
        task_lines = []
        access_tasks()

        for task in task_lines:
            print("─" * 160)
            print("Task\t\t\t", task[1])
            print("Assigned to:\t\t", task[0])
            print("Date assigned:\t\t", task[3])
            print("Due date:\t\t", task[4])
            print("Task Complete?\t\t", task[5].strip())
            print("Task description:\t", task[2])
        print("─" * 160)

    # This code block reads the task from task.txt file
    # and prints only the current user's tasks to the console.
    elif menu == 'vm':
        task_lines = []
        access_tasks()

        for task in task_lines:
            task_user_name = task[0]

            if task_user_name == user_name:
                print("─" * 160)
                print("Task:\t\t\t", task[1])
                print("Assigned to:\t\t", task[0])
                print("Date assigned:\t\t", task[3])
                print("Due date:\t\t", task[4])
                print("Task Complete?\t\t", task[5].strip())
                print("Task description:\t", task[2])
        print("─" * 160)

    # This code block outputs user statistics to the admin only:
    # It contains the total number of tasks and total number of users.
    elif menu == 'ds':
        task_lines = []
        access_user_credentials()
        access_tasks()

        user_counter = len(user_credentials)
        task_counter = len(task_lines)

        print("─" * 160)
        print(f"User count:\t\t{user_counter}")
        print(f"Task count:\t\t{task_counter}")
        print("\n" + '─' * 160)

    # This code block prints all the usernames for the admin only.
    elif menu == 'u':
        print("─" * 160)
        print("Usernames:", end= "\t\t")

        for key in user_credentials:
            print(key, end="\n\t\t\t")
        print("\n" + '─' * 160)

    # This code ends the display menu.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # This code displays an error message if the input was invalid.
    else:
        print("You have entered an invalid input. Please try again")
