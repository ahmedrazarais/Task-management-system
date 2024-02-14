import os

from employe_signup import sign_up
from files_path import file_accoutns,user_directory,admin_notific,directory_notify
from admin_management import admin_employe_choices,annoucement_specific,annoucement
from management_functions import add_tasks,delete_task,view_tasks,update_tasks
from admin_accounts import admin_choices,view_accounts,search_user,delete_account

accounts_users=[]                     # LIST TO GET ACCOUNTS DATA
account_sep="#@!%^"             # SEPERATOR
task_list=[]                          # LIST TO GET TASKS FROM FILE OF USER

def admin_login():
    """
    Function to handle the login process for an admin user and provide access to administrative features.
    """
    admin_user_name="ahmed"    # Setting admin username and password
    admin_pswd="1234"
    while True:     # taking username input
        user_name=input("Enter Admin username (enter 0 to return):")
        if user_name=="0":    # return on certain condition
            return
        if user_name==admin_user_name:    # if username matches
             print("Username found! Please proceed to enter your password to continue.")
             print()
             break
        else:
            print()
            print("Invalid Admin Username..")
    while True:   # Taking pssword input if username matches
             print()
             password=input("Enter Admin Password (enter 0 to return):")
             if password=="0":
                 return
             if password==admin_pswd:   # if both are correct
                 print("|Administration Login Successfull|")
                 print()
                 break
             else:
                 print()
                 print("Invalid Administration Password..")
                 print()

    while True:         # AFTER LOGIN SUCCESSSFULL
        
                     print()
                     print("\t\tWELCOME TO ADMINISTRATION AREA!!")
                     print("\t1.Manage Account Area Of Employees")
                     print("\t2.Access Task Management Area Of Employees")
                     print("\t3.Make Annoucement In Official Group For All Employees")
                     print("\t4.Complete Exit From Administration Area")
                     print()
                     # Taking input of choice to get enter in account or management area
                     option=input("Select Your Choice from (1/2/3/4):")                    
                     if option=="1":    # If option 1
                        # THIS IS ACCOUNT AREA
                         while True:
                             admin_choices()
                             access=input("Enter Your Choice In accounts area:")
                             if access=="1":
                                 view_accounts(accounts_users,file_accoutns)
                             elif access=="2":
                                 search_user(accounts_users,file_accoutns)
                             elif access=="3":
                                 delete_account(accounts_users,file_accoutns,user_directory)
                             elif access=="4":
                                 sign_up(accounts_users,user_directory)
                             elif access=="5":
                                 print("Back From Employees Accounts Area..")
                                 break
                             else:
                                 print()
                                 print("Invalid Choice.Please Select From Given Options")
                                 print()                            
                     # THIS IS TASK MANAGEMENT AREA 
                     elif option=="2":
                         while True:
                             print()
                             print("Enter User-Name Of Employee To Get Access Of Task Management System")
                             print()
                             view_accounts(accounts_users,file_accoutns)
                             print()
                             # TAKING INPUT OF USERNAME TO ENTER INTO SYSTEM OF THAT EMPLOYEE
                             username = input("Enter the username of the (employee enter 0 to back): ").strip()
                             if username=="0":
                                break
                             user_file = os.path.join(user_directory, f"{username}.txt")
                             # If FILE EXISTS
                             if os.path.exists(user_file):
                                    print()
                                    print(f"Accessing employee {username}'s task management system...")
                                    print()
                                    while True:
                                        admin_employe_choices()
                                        get=input("Enter Your Choice In Management System:")
                                        if get=="1":
                                           view_tasks(user_file,task_list)
                                        elif get=="2":
                                            add_tasks(user_file)
                                        elif get=="3":
                                           update_tasks(user_file, task_list)
                                        elif get=="4":
                                           delete_task(user_file, task_list)
                                        elif get=="5":
                                            annoucement_specific(directory_notify,username)
                                        elif get=="6":
                                            print("Back From Management area..")
                                            print()
                                            break
                                        else:
                                            print()
                                            print("Invalid Choice .Please Select From Given Choices.")
                                            print()
                             else:   # IF FILE NOT EXISTS
                                    print()
                                    print(f"The file for employee {username} does not exist.")
                     elif option=="3":
                         annoucement(admin_notific)                        
                     elif option=="4":
                         print("Exiting From Administration Area...")
                         break                 
                     else:
                         print("Invalid Choice Please Select Correct Option")
      