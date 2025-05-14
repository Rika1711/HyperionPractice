# Python: `task_manager.py`

This program is designed to help a small business manage tasks assigned to team members. It allows users to log in, register new users (admin only), add tasks, and view tasks.

## Project Structure

The program works with two provided text files:

* `user.txt`: Stores usernames and passwords for users who can access the program. Each line contains a username, a comma, a space, and the corresponding password (e.g., "admin, adm1n").
* `tasks.txt`: Stores information about each task. Each line contains the following task data, separated by commas: username of assignee, task title, task description, assignment date, due date, and completion status ("Yes" or "No").

## Compulsory Task Part 1

The program allows users to do the following:

* **Login:**
    * Prompts the user to enter a username and password.
    * Reads valid usernames and passwords from `user.txt`.
    * Displays an error message if the entered username is not found in `user.txt` or if the password does not match the stored password for the given username.
    * Repeatedly asks for login credentials until valid credentials are provided.
    * Displays a menu upon successful login.
* **Register a User (Admin Only - Part 2):**
    * If the user chooses 'r' (and is the admin in Part 2), the program prompts for a new username and password.
    * Prompts the user to confirm the password.
    * If the password and confirmation match, the username and password are written to `user.txt` in the specified format.
* **Add a Task:**
    * If the user chooses 'a', the program prompts for the following task details:
        * Username of the person the task is assigned to.
        * Title of the task.
        * Description of the task.
        * Due date of the task.
    * The current date is used as the assignment date.
    * The task's completion status defaults to "No".
    * The task data is written to `tasks.txt` in the specified format.
* **View All Tasks:**
    * If the user chooses 'va', the program displays all tasks from `tasks.txt` in a user-friendly format.
* **View My Tasks:**
    * If the user chooses 'vm', the program displays only the tasks from `tasks.txt` that are assigned to the currently logged-in user, in a user-friendly format.

## Compulsory Task Part 2

This part adds the following functionality:

* **Admin-Only User Registration:** Only the user with the username "admin" is allowed to register new users. The 'r' option in the menu is only available to the admin user.
* **Statistics Menu Option (Admin Only):**
    * A new menu option is added for the "admin" user.
    * When selected, the program displays:
        * The total number of tasks in `tasks.txt`.
        * The total number of users in `user.txt`.

## How to Run the Program

1.  Ensure you have Python installed.
2.  Save the Python code as `task_manager.py`.
3.  Create the text files `user.txt` and `tasks.txt` in the same directory as `task_manager.py`.
4.  Populate `user.txt` with at least one user (e.g., "admin, adm1n"). The program assumes this file exists and is correctly formatted.
5.  Populate `tasks.txt` with task data, or the program will create the file if it doesn't exist.
6.  Open a command prompt or terminal.
7.  Navigate to the directory where you saved the files using the `cd` command.
8.  Run the program using the command: `python task_manager.py`
