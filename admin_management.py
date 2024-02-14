import os
def admin_employe_choices():
       # FUNCTION TO PROVIDE CHOICES TO ADMIN IN MANAGEMENT SYSTEM.
        print("\t\t Welcome To Management Area")
        print("\t1.See The Task Details Of Employee")
        print("\t2.Assign Tasks To  Employee")
        print("\t3.update Task For Employee")
        print("\t4.Delete Assigned Task Of The Employee")
        print("\t5.Make The Annoucement For That Employe")
        print("\t6.Exit From Management Area.")    
        print()
        print()
def annoucement(admin_notific):
    """
    Function to make announcements for all employees.

    This function allows the admin to enter a specified number of announcements and writes them
    to the admin notification file, which is intended to be accessible to all employees.

    Parameters:
    - admin_notific (str): The file path of the admin notification file.

    Returns:
    - None

    The function prompts the admin to input the number of announcements they want to make. If the
    admin inputs '0', the function returns without making any announcements. Otherwise, it prompts
    the admin to enter each announcement one by one and writes them to the admin notification file.

    """
    
    while True:
         try:
            quantity=int(input("Enter How many Annoucement You Want To Set (enter 0 to back):"))
            if quantity=="0":
                return
            for i in range(1,quantity+1):
                notification=input(f"Enter {i} Notification for Employees:")
                with open(admin_notific,"a+") as admin:
                    admin.write(f"* {notification}\n")
            print()
            print("Annoucement Has Been Successfully Uploaded To All Employees Portal")
            print()
            break
         except ValueError:
            print("Please Write In Digits.")



def annoucement_specific(directory_notify,username):
    """
    Function to make announcements for a specific employee.

    Parameters:
        directory_notify (str): The directory where notifications will be stored.
        username (str): The username of the employee for whom the announcements are intended.

    Returns:
        None

    This function prompts the admin to input the number of announcements they want to set
    and then allows them to input each announcement individually. The announcements are
    then written to the specific employee's notification file.
    """
    user_file = os.path.join(directory_notify, f"{username}.txt")   
    while True:
        try:
            quantity = input("Enter how many announcements you want to set: ")
            quantity = int(quantity)  
            with open(user_file, "a+") as user_notification_file:
                for i in range(1, quantity + 1):
                    notification = input(f"Enter {i} Notification for Employee {username}: ")
                    user_notification_file.write(f"* {notification}\n")
            
            print()
            print("Announcements have been successfully uploaded to the specific employee's portal.")
            print()
            break
        except ValueError:
            print("Please Write In digits.")
