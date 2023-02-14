# It will make use of lists or dictionaries and functions to extend the functionality of the project.

# This program is designed for use in a small business.
# It works to manage tasks assigned to team members.
# for os function I used https://www.geeksforgeeks.org/os-module-python-examples/


from datetime import date
import os
import datetime
# _____________
# The function reg_user() is used to register a new user by asking for their username and password.
# When the function is called, it first initializes empty lists usernames_list and passwords_list to store the existing usernames and passwords of registered users
# Next step, creates an empty dictionary user_details to store the usernames and passwords of the newly registered user.
# Code reads the contents of a file named "user.txt", which is assumed to contain a list of already registered users, each on a new line in the format of username, password.
# The code uses the readlines() method to get a list of all the lines in the file and then uses a for loop to split each line into a username and password using the strip() and split(", ") methods
# Finally, the code appends the new user's details to the end of the "user.txt" file in the format new_user + ", " + new_password.


def reg_user():
    usernames_list = []
    passwords_list = []
    user_details = {}

    new_user = input("Enter a username: ")

    with open("user.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            username, password = line.strip().split(", ")
            usernames_list.append(username)
            passwords_list.append(password)

    while new_user in usernames_list:
        print("That username is already taken. Try another one.")
        new_user = input("Enter your username:  \n")

    if new_user not in usernames_list:
        usernames_list.append(new_user)

        user_details["usernames"] = usernames_list

        new_password = input("Enter your password:  \n")
        pass_confirm = input("Enter your password again:  \n")

        while new_password != pass_confirm:

            print("Passwords do not match. Try again.")
            new_password = input("Enter your password:  \n")
            pass_confirm = input("Enter your password again:  \n")

        if new_password == pass_confirm:
            passwords_list.append(new_password)
            user_details["passwords"] = passwords_list

            with open("user.txt", "a") as file:
                file.write('\n' + new_user + ", " + new_password)
                print("You have successfully registered!")


# _____________________________________________________________________________________
# Function add_task() is used to add a new task by asking for the details of the task such as the username of the person the task is assigned to, the title of the task
# It retrieves the current date using the datetime module's today() method and formats it using the strftime() method to store it in the date_assigned variable
# The code then opens a file named "tasks.txt" in append mode using the open()
# After writing the task details to the file, the code closes the file using the close()
# _______________________________________________________________________________


def add_task():
    username = input("Enter username of person task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Give a brief description of the task: ")
    DD = input("Enter the due date of the task: ")
    date_assigned = datetime.date.today()
    complete = "No"

    add_task = [username + "," + " " + title + "," + " " + description +
                "," + " " + str(date_assigned) + "," + " " + DD + "," + " " + complete]
    fo = open("tasks.txt", "a")
    for line in add_task:
        fo.write("\n" + add_task)
    fo.close()
    print("Task added successfully")
    print("\n")


# ~~~~~~~~~~~~~~~~~~~~~~~
# This code defines a function named "view_all" which opens the text file 'tasks.txt' in read mode ('r') and reads each line of the file.
# The function also includes an exception handling mechanism to catch the case where the number of elements in the list is not enough, which would cause an "IndexError".
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def view_all():
    with open('tasks.txt', 'r') as f:
        for line in f:
            contents = line
            contents_list = contents.split(", ")
            try:
                print(f"________________________________\n")
                print(f"Task:", "\t\t\t\t", contents_list[1])
                print(f"Assigned to:", "\t\t\t\t ", contents_list[0])
                print(f"Date assigned:", "\t\t\t\t", contents_list[3])
                print(f"Due date:", "\t\t\t\t", contents_list[4])
                print(f"Task complete?", "\t\t\t\t", contents_list[5])
                print(f"Task description:", "\t\t\t\t", contents_list[2])
                print(f"___________________________________\n")
                print(f"\n")
            except IndexError:
                print("Error: Not enough elements in the list.")

# ___________________________________________________________
# This code defines a function "view_mine()" which allows a user to view all the tasks assigned to them and perform certain actions such as editing and marking a task as complete.
# It filters the tasks to only show the ones assigned to the user, specified by the "username" variable
# If the user chooses to edit a task, the code updates the task information in the "tasks.txt" file. If the user chooses to mark a task as complete, the code updates the status of the task in the file to "YES".
# ________________________________________________________________


def view_mine():
    with open('tasks.txt', 'r') as f:
        contents = f.readlines()
        task_list = []
        other_tasks = []
        for line in contents:
            line = line.strip()
            task = line.split(',')
            if username == task[0]:
                task_list.append(task)
            else:
                other_tasks.append(line)

        if not task_list:
            print("There are no tasks assigned to you.")
            return

        for i, task in enumerate(task_list):
            print(f"{i+1}. Task: {task[1]}")

        task_num = int(
            input("Enter the task number to view (-1 to return to main menu): "))
        if task_num == -1:
            return
        task_num -= 1

        if task_list[task_num][5] == "NO":
            print(f"\nTask: {task_list[task_num][1]}\nAssigned to: {task_list[task_num][0]}\nDate assigned: {task_list[task_num][3]}\nDue date: {task_list[task_num][4]}\nTask complete?: {task_list[task_num][5]}\nTask description: {task_list[task_num][2]}")
        edit = input("\nDo you want to edit this task (y/n)? ").lower()
        if edit == 'y':
            task_list[task_num][1] = input("Enter new task: ")
            task_list[task_num][2] = input(
                "Enter new task description: ")
            task_list[task_num][4] = input(
                "Enter new due date (YYYY-MM-DD): ")
            with open('tasks.txt', 'w') as f:
                for task in task_list:
                    f.write(','.join(task) + '\n')
                for line in other_tasks:
                    f.write(line + '\n')

        else:
            print(f"\nTask: {task_list[task_num][1]}\nAssigned to: {task_list[task_num][0]}\nDate assigned: {task_list[task_num][3]}\nDue date: {task_list[task_num][4]}\nTask complete?: {task_list[task_num][5]}\nTask description: {task_list[task_num][2]}")
        complete = input(
            "\nDo you want to mark this task as complete (y/n)? ").lower()
        if complete == 'y':
            task_list[task_num][5] = "YES"
            with open('tasks.txt', 'w') as f:
                for task in task_list:
                    f.write(','.join(task) + '\n')
# ~~~~~


# --------------------------------------------------------------------
# This part of the code was very hard to figure
# This script generates two reports based on the data in the "tasks.txt" file.
# It counts the total number of tasks, the number of completed tasks, the number of uncompleted tasks, and the number of overdue tasks
# The first report, "task_overview.txt", provides an overview of the tasks and their completion status, including the total number of tasks, the total number of completed tasks, the total number of uncompleted tasks, the total number of overdue tasks, the percentage of uncompleted tasks, and the percentage of overdue tasks.
# The second report, "user_overview.txt", provides a summary of the tasks assigned to each user, including the total number of users, the total number of tasks, the total number of tasks assigned to each user, and the percentage of tasks assigned to each user.
# ________________________________________________________________


def generate_reports():
    tasks = {}
    with open("tasks.txt", "r") as f:
        for line in f:
            values = line.strip().split(", ")
            if len(values) != 6:
                continue
            user, title, description, date_assigned, due_date, completed = values
            tasks[title] = tasks.get(
                title, []) + [(user, description, date_assigned, due_date, completed)]
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    users = {}
    with open("tasks.txt", "r") as f:
        for line in f:
            values = line.strip().split(", ")
            if len(values) != 6:
                continue
            user, title, description, date_assigned, due_date, completed = values
            users[user] = users.get(user, [])
            users[user].append(
                (title, description, date_assigned, due_date, completed))
            total_tasks += 1

            if completed == "yes":
                completed_tasks += 1
            elif completed == "no":
                uncompleted_tasks += 1
                if due_date < datetime.today().strftime("%Y-%m-%d"):
                    overdue_tasks += 1

    with open("task_overview.txt", "w") as task_file:
        task_file.write("Task overview:\n")
        task_file.write(f"- Total number of tasks: {total_tasks}\n")
        task_file.write(
            f"- Total number of completed tasks: {completed_tasks}\n")
        task_file.write(
            f"- Total number of uncompleted tasks: {uncompleted_tasks}\n")
        task_file.write(f"- Total number of overdue tasks: {overdue_tasks}\n")
        if total_tasks != 0:
            task_file.write(
                f"- Percentage of uncompleted tasks: {uncompleted_tasks / total_tasks * 100:.2f}%\n")
            task_file.write(
                f"- Percentage of overdue tasks: {overdue_tasks / total_tasks * 100:.2f}%\n")
            print("Task overview file generated.")
        else:
            task_file.write("- Percentage of uncompleted tasks: 0.00%\n")

    total_users = len(users)
    with open("user_overview.txt", "w") as user_file:
        user_file.write("User overview:\n")
        user_file.write(f"- Total number of users: {total_users}\n")
        user_file.write(f"- Total number of tasks: {total_tasks}\n")
        for user, user_tasks in users.items():
            user_file.write(f"\nUser: {user}\n")
            user_task_count = len(user_tasks)
            user_file.write(
                f"- Total number of tasks assigned to {user}: {user_task_count}\n")

            user_file.write(
                f"- Percentage of tasks assigned to {user}: {user_task_count / total_tasks * 100:.2f}%\n")

    print("User overview file generated.")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The code defines a function statistics() that first checks if the task_overview.txt and user_overview.txt reports exist in the current directory. If they don't exist, the function calls the generate_reports() function to create them.

# Next, the code opens the task_overview.txt and user_overview.txt files and prints the contents of each file to the console.
# Then the code counts the number of lines in the user.txt file and prints the total number of users
# Then it counts the number of lines in the tasks.txt file and prints the total number of tasks. The final output shows the total number of users and tasks stored in the text files.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def statistics():
    if not (os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt")):
        print("Generating reports...")
        generate_reports()

    with open("task_overview.txt", "r") as task_file:
        task_data = task_file.read()
        print(task_data)

    with open("user_overview.txt", "r") as user_file:
        user_data = user_file.read()
        print(user_data)

    total_users = 0
    with open("user.txt", "r") as txt_user:
        for line in txt_user.readlines():
            total_users += 1
    print(f"The total number of users:", "\t\t\t\t", total_users)

    total_tasks = 0
    with open('tasks.txt', 'r') as f:
        for line in f:
            total_tasks += 1
    print(f"The total number of tasks:", "\t\t\t\t", total_tasks)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is a Python program names task_manager. It allows users to register new users, view and add tasks, and view statistics.
# This is the section where I imported libraries and opened the files
task_read = open("tasks.txt", "r+", encoding='utf-8')
reg_use = open("user.txt", "r+", encoding='utf-8')

# This is my Logging in section
# First, I read the contents of user.txt into memory
# Then I split the data into a list of username and password pairs

contents = reg_use.read()
lines = contents.split("\n")
user_passwords = {}
for line in lines:
    parts = line.split(", ")
    if len(parts) == 2:
        username, password = parts
        user_passwords[username] = password

# This is where the user is asked to enter their username and password
# I used a while loop with a counter to limit the number of attempts
# If the username and password combination is correct, the loop will exit
# Otherwise, the user will be asked to enter the correct information

attempts = 0
while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username in user_passwords and user_passwords[username] == password:
        print("You are successfully logged in")
        break
    else:
        print("Incorrect username or password.")
        attempts += 1

if attempts == 3:
    print("Too many attempts. Access denied.")


while True:
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
ds - Statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
ds - Statistics
e - Exit
: ''').lower()

    if menu == "r":
        if username == "admin":
            reg_user()

    elif menu == "a":
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == "gr":
        generate_reports()

    elif menu == "ds":
        statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

    reg_use.close()
    task_read.close()
