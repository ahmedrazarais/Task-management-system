import os
task_list=[]                          # LIST TO GET TASKS FROM FILE OF USER
def view_tasks(user_file, task_list):
    x = "#@!%^"    # Separator to split on
    task_list.clear()   
    with open(user_file) as contents:
        contents.seek(0)
        for line in contents:
            data = line.strip().split(f"{x}")    # Making a dictionary
            if len(data) >= 5:  # Check if data contains at least 5 elements
                user_task_dict = {"taskcode": data[0], "taskname": data[1], "description": data[2], "deadline": data[3], "level": data[4]}
                task_list.append(user_task_dict)   # append in list
            else:
                print("Incomplete task data:", data)  # Print incomplete data for debugging

    if not task_list:     # if there is no task added
        print()
        print("It Seems There is no task added to your list. Add Some Tasks and Come Back.")
        print()
    else:
        # Main heading with inverted commas and centered
        main_heading = "\"Task Overview\""
        print(main_heading.center(100))
        print()  # Add a gap after the main heading

        # Divider line after main heading
        print('-' * 100)
        # Subheadings with first letters capitalized and task numbers
        print("{:<10} {:<20} {:<40} {:<20} {:<15}".format("Task Code", "Task Name", "Description", "Deadline", "Priority Level"))
        # Divider lines between subheadings
        print('-' * 100)

        for i, task in enumerate(task_list, 1):
            # Adjusting spacing based on the length of the data in each column
            description = task['description'][:37] + '...' if len(task['description']) > 40 else task['description']
            print("{:<10} {:<20} {:<40} {:<20} {:<15}".format(task['taskcode'], task['taskname'].capitalize(), description, task['deadline'], task['level'].capitalize().strip()))
            if i < len(task_list):  # Add a line after each task except the last one
                print('-' * 100)
            print()  # Add a gap after each task


def options_update():
    print()
    print("\t\tWelcome To Update Section")
    print("1.Update Task name")
    print("2.Update Task Description")
    print("3.Update Task Deadline")
    print("4.Update Task Priority Level")
    print("5.Back From This Section")
    print()
def update_tasks(user_file, task_list):
    x = "#@!%^"
    view_tasks(user_file, task_list)
    
    while True:  # Main loop to keep the user in the update options until they decide to exit
        if task_list:  # Checking if there is something in the task list
            taskcode = input("Enter The Task Code Of Task You Want To Update (enter 0 to exit): ")
            if taskcode == "0":  # If the user chooses to exit
                break

            for check in task_list:  # Iterating over tasks in the list
                if taskcode == check["taskcode"]:  # If task code is found
                    while True:
                        options_update()
                        choice = input("Enter Your Choice:")

                        if choice == "1":  # Update Task name
                            while True:  # TAKING TASK NAME INPUT
                                print()
                                task_name = input("Enter Task Name (enter 0 to back):").strip().lower()
                                if task_name == "0":  # checking return condition
                                    break  # Exit to the outer loop
                                # Checking if task name is not empty
                                if task_name != "":
                                    if all(word.isalpha() or word.isspace() for word in task_name):
                                        check["taskname"] = task_name     # updating key value
                                        break
                                    else:  # if conditions not match
                                        print("Task name should contain only alphabets and spaces.")
                                else:
                                    print("Task name is mandatory.")

                            break

                        elif choice == "2":  # Update Task Description
                            while True:
                                print()
                                description = input("Write Description Of That Task (Must Contain 10 Letters at least):")
                                if description == "0":
                                    break  # Exit to the outer loop
                                # Checking length of description
                                if len(description) >= 10:
                                    # Checking if description contains at least one alphabet
                                    if any(char.isalpha() for char in description):
                                        check["description"] = description    # updating key value
                                        break
                                    else:
                                        print("Please Write something In description.")
                                        print()
                                else:  # printing message
                                    print("Description should contain at least 10 letters and must include alphabets.")

                            break

                        elif choice == "3":  # Update Task Deadline
                            while True:  # taking deadline input
                                print()
                                deadline = input("Set The Deadline Of This Task:")
                                if deadline == "0":
                                    break  # Exit to the outer loop
                                if deadline != "":
                                    if all(word.isdigit() or word.isspace() for word in deadline):
                                        check["deadline"] = deadline     # updating key value
                                        break
                                    else:
                                        print("Only Digits and Spaces are allowed")
                                else:  # if not matches
                                    print("Setting Deadline is Compulsory")

                            break

                        elif choice == "4":  # Update Task Priority Level
                            while True:  # taking priority level input
                                print()
                                level = input("Enter Priority Level Of This Task (low/high/medium): ").lower()
                                if level == "0":
                                    break  # Exit to the outer loop
                                # if input not receive according to choices
                                if level not in ["low", "high", "medium"]:
                                    print()
                                    print("Must Select From These Three (low/high/medium)")
                                    print()
                                else:
                                    check["level"] = level  # updating key value
                                    break

                            break

                        elif choice == "5":  # Back From This Section
                            print()
                            print("Back From This Section")
                            print()
                            break  # Exit to the outer loop

                        else:
                            print()
                            print("Invalid Choice")
                            print()

                    # Update the task in the file
                    with open(user_file, "w") as file:
                        for content in task_list:
                            file.write(f"{content['taskcode']}{x}{content['taskname']}{x}{content['description']}{x}{content['deadline']}{x}{content['level']}\n")
                    print()
                    print("Update Has Been Done")
                    print()
                    view_tasks(user_file, task_list)   # updated version
                    break

            else:    # If wrong Task Code Enters
                print("Sorry, no task found with the provided task code. Please enter a valid task code or enter '0' to go back.")
                print()
        else:
            print("No tasks in the list.")     # If There is no task
            print()
            break

def delete_task(user_file, task_list):
    
    x = "#@!%^"  # Separator
    view_tasks(user_file, task_list)  # Display users tasks
    if task_list:  # Checking if task list is not empty

        # Taking Input Of task code to delete data
        while True:
            taskcode = input("Enter The Task Code To delete That Task (enter 0 to back): ")
            if taskcode == "0":  # if 0 then return
                return
            for check in task_list:
                if taskcode == check["taskcode"]:  # if taskcode match with dictionary value
                    task_list.remove(check)  # removing the dictionary
                    print("Task deleted successfully.")
                    # after successful deletion
                    with open(user_file, "w") as file:
                        for index, content in enumerate(task_list, start=1):
                            content["taskcode"] = str(index)  # Update task codes sequentially
                            file.write(
                                f"{content['taskcode']}{x}{content['taskname']}{x}{content['description']}{x}{content['deadline']}{x}{content['level']}\n")
                    view_tasks(user_file, task_list)  # Display users tasks
                    return  # Exit function after successful deletion
            else:
                print()  # if not code match
                print("Sorry, no task found with the provided task code. Please enter a valid task code or enter '0' to go back.")
                print()
    else:
        print("Having Nothing To Delete")  # if no data in file
        print()






def add_tasks(user_file):
    x = "#@!%^"  # Separator
    task_list = []  # Initialize an empty list to store tasks

    # Load existing tasks from file, if any
    with open(user_file, "r") as file:
        for line in file:
            data = line.strip().split(x)
            if len(data) >= 5:
                user_task_dict = {"taskcode": data[0], "taskname": data[1], "description": data[2], "deadline": data[3], "level": data[4]}
                task_list.append(user_task_dict)

    all_done = False  # Flag to indicate if all inputs are done
    while True:
        print()
        task_name = input("Enter Task Name (enter 0 to go back):").strip().lower()
        if task_name == "0":
            return
        if task_name != "":
            if all(word.isalpha() or word.isspace() for word in task_name):
                break
            else:
                print("Task name should contain only alphabets and spaces.")
        else:
            print("Task name is mandatory.")

    while True:
        print()
        description = input("Write Description Of That Task (Must Contain 10 Letters at least):")
        if description == "0":
            return
        if len(description) >= 10:
            if any(char.isalpha() for char in description):
                break
            else:
                print("Please write something in the description.")
                print()
        else:
            print("Description should contain at least 10 letters and must include alphabets.")

    while True:
        print()
        deadline = input("Set The Deadline Of This Task:")
        if deadline == "0":
            return
        if deadline != "":
            if all(word.isdigit() or word.isspace() for word in deadline):
                break
            else:
                print("Only digits and spaces are allowed.")
        else:
            print("Setting the deadline is compulsory.")

    while True:
        print()
        level = input("Enter Priority Level Of This Task (low/high/medium): ").lower()
        if level == "0":
            return
        if level in ["low", "high", "medium"]:
            all_done = True
            print("Task has been successfully added to your list.")
            print()
            break
        else:
            print("Please select from these three options: low, high, medium.")

    if all_done:
        # Generate a unique task code
        if task_list:
            task_code = str(int(task_list[-1]["taskcode"]) + 1)
        else:
            task_code = "1"

        # Write the task details to the file
        with open(user_file, "a+") as file:
            file.write(f"{task_code}{x}{task_name}{x}{description}{x}{deadline}{x}{level}\n")

def view_specific_notifications(directory_notify, username):
    """
    Function to view notifications specific to a particular employee.

    Parameters:
        directory_notify (str): The directory where notification files are stored.
        username (str): The username of the employee whose notifications are to be viewed.

    Returns:
        None

    This function checks if a notification file exists for the specified username.
    If the file exists, it reads the notifications from the file and displays them.
    If there are no notifications, it prints a message indicating that there are no notifications available.
    If the notification file is not found, it prints a message indicating that the file does not exist.
    """
    user_file = os.path.join(directory_notify, f"{username}.txt")
    if os.path.exists(user_file):
        with open(user_file) as user_notification_file:
            notifications = user_notification_file.readlines()
            if notifications:
                print("Notifications:")
                for notification in notifications:
                    print(notification.strip())
            else:
                print("No notifications available for you.")
    else:
        print("No notifications available for you..")

def notification_read(admin_notific):
     """
    Function to read notifications generated by the admin for all employees.

    Parameters:
        admin_notific (str): The file containing notifications generated by the admin.

    Returns:
        None

    This function reads the contents of the specified file, which typically contains
    notifications generated by the admin for all employees. If there are notifications,
    it prints them to the user. If no notifications are found, it prints a message
    indicating that no announcements have been received yet.
    """
     with open(admin_notific) as reading:
                    contents=reading.read()
                    if contents:
                        print(contents)
                    else:
                        print()
                        print("Sorry ,No Annoucement Recieved Yet!")
