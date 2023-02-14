# I used multiple sites to do this project, all of which are sited below.
# https://www.delftstack.com/howto/python/python-list-contains-string/
# https://www.journaldev.com/23759/python-find-string-in-list#:~:text=Python%20Find%20String%20in%20List%20using%20count(),'A'%20count%20%3D%20l1.
# https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/

# This is a Python program names task_manager. It allows users to register new users, view and add tasks, and view statistics.
# This is the section where I imported libraries and opened the files


from datetime import date
global task_read, reg_user
task_read = open("tasks.txt", "r+", encoding='utf-8')
reg_user = open("user.txt", "r+", encoding='utf-8')

# This is my Logging in section
# First, I extracted the date from user.txt. Then I added it to a list but first I had to split the data into its username and password using the For Loop

contents = ""
for line in reg_user:
    contents += line
list1 = contents.split()
list2 = []
for i in range(0, len(list1)):
    if i % 2 != 0:
        list2.append(list1[i])
    elif i % 2 == 0:
        list3 = list(list1[i])
        (list3).remove(",")
        list2.append(''.join(list3))

# This is where the user is asked to enter their username. I used an If statement and while loop to see if the username is valid(i.e. in the list)

username = input("Username: ")

if username in list2:
    print("Username is correct. Please enter password")
while username not in list2:
    print("Username is incorrect. Please enter username")
    username = input("Username: ")
    if username in list2:
        print("Username is correct. Please enter password")

# This is where I did the validation for the password. Also, using the If statement and while loop to see if the password is valid(i.e. in the list)

password = input("Password: ")
if password in list2:
    print("Password is correct. Logging in")
while password not in list2:
    print("Username valid, password is invalid. Please enter password")
    password = input("Password: ")
    if password in list2:
        print("Password is correct. Logging in")

# Below is the menu options that are shown on screen if the username is admin or if the username is something else.

while True:
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# If the user selects 'r' from the menu, the user is asked to enter a new username and password.
# Using the If Else statement and For loop to write and append the new username and password to the text file user.

    if menu == 'r':

        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        confirm_password = input("Please confirm your password: ")

        if new_password == confirm_password:
            new_user = [new_username + "," + " " + new_password]
            fi = open("user.txt", "a")
            for line in new_user:
                fi.write("\n" + line)
            fi.close()
            print("\n")
        else:
            print("Password does not match.")
            print("\n")

# If the user selects 'a', the user is asked to enter information for the task that they are adding.
# Using the For loop to append the information to the task.txt file.

    elif menu == 'a':

        username = input("Enter username of person task is assigned to: ")
        title = input("Enter the title of the task: ")
        description = input("Give a brief description of the task: ")
        DD = input("Enter the due date of the task: ")
        date_assigned = date.today().strftime("%d/%m/%Y")
        complete = "No"

        task = [username + "," + " " + title + "," + " " + description +
                "," + " " + date_assigned + "," + " " + DD + "," + " " + complete]
        fo = open("tasks.txt", "a")
        for line in task:
            fo.write("\n" + line)
        fo.close()
        print("\n")

# If the user enters 'va', the data from the task.txt file is extracted and displayed onto the screen.
# Done using the For loop.

    elif menu == 'va':
        with open('tasks.txt', 'r') as f:
            contents = " "

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

# If the user selects 'vm', the data from the task.txt file is extracted for that particular username.
# Using the For loop to extract the data and If statement to see if that username is in that line of the data extracted.

    elif menu == 'vm':
        with open('tasks.txt', 'r') as f:

            view_mine = ""
            for line in f:
                view_mine = line
                view_mine_list = view_mine.split(",")
                if username == view_mine_list[0]:
                    print(f"___________________________________________\n")
                    print(f"Task:", "\t\t\t\t", view_mine_list[1])
                    print(f"Assigned to:", "\t\t\t\t ", view_mine_list[0])
                    print(f"Date assigned:", "\t\t\t\t", view_mine_list[3])
                    print(f"Due date:", "\t\t\t\t", view_mine_list[4])
                    print(f"Task complete?", "\t\t\t\t", view_mine_list[5])
                    print(f"Task description:", "\t\t\t\t", view_mine_list[2])
                    print(f"___________________________________________\n")

                    print(f"\n")

# If the user selects 's' , the number of users is displayed using the count method with the for loop.
# and the number of tasks is also displayed using the len() function and readlines() function.

    elif menu == "s":

        count = 0
        with open("user.txt", "r") as reg_user:
            for line in reg_user.readlines():
                count += 1
            print(f"The total number of users:", "\t\t\t\t", count)

        with open('tasks.txt', 'r') as f:
            for line in f:
                count += 1
            print(f"The total number of tasks:", "\t\t\t\t", count)

# If the user selects 'e', the program is exited.

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

    reg_user.close()
    task_read.close()
