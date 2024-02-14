import os

from employe_signup import sign_up
from employe_login import login
from files_path import file_accoutns,user_directory,directory_notify,admin_notific
from management_functions import view_tasks,update_tasks,add_tasks,delete_task,view_specific_notifications,notification_read
from admin_login import admin_login

task_list=[]                          # LIST TO GET TASKS FROM FILE OF USER
accounts_users=[]                     # LIST TO GET ACCOUNTS DATA
# Providing user choices display
def main_choice():
    print("\t\tWelcome To Task Manager Hub")
    print("1.Signup As User")
    print("2.Login As User")
    print("3.Access Task Management System")
    print("4.Login As Admin")
    print("5.To Exit")
    print()
   
# giving user options in task management systems
def system_choices():
    print()
    print("\t\tWelcome To This Area")
    print("There Are Multiple Options For You To Perform.")
    print()
    print("1.See All Your Tasks Details")
    print("2.Add any Task To Your File.")
    print("3.Update Any specific Task.")
    print("4.Delete Any specific Task.")
    print("5.Check The Annoucement Make By Admin.")
    print("6.Check The Annoucement Official Group.")
    print("7.Exit From This Section")
    print()
    

while True:
    main_choice()
    choice=input("Enter Your Desired Options :")
    if choice=="1":
        sign_up(accounts_users,user_directory)
    elif choice=="2":
        login(file_accoutns,accounts_users,user_directory)
    elif choice == "3":
     # Taking Username input to check the file
     username = input("Enter your username to get access of the system:: ").strip()   
     user_file = os.path.join(user_directory, f"{username}.txt")
     if os.path.exists(user_file):       
        print()
        print(f"Accessing {username}'s Task Management System...")
        # Proceed with task management system logic
        while True:   # When user chooses to get acces of management system
            system_choices()
            choice=input("Enter Your Choice:")
            if choice=="1":
                view_tasks(user_file,task_list)
            elif choice=="2":
                add_tasks(user_file)
            elif choice=="3":
                update_tasks(user_file,task_list)
            elif choice=="4":
                delete_task(user_file,task_list)
            elif choice=="5":
               view_specific_notifications(directory_notify, username)
            elif choice=="6":
                notification_read(admin_notific)            
            elif choice=="7":
                print()
                print("Exiting Program...")
                break
            else:
                print("Invalid Choice")
                print("Please Select Correct Options")
                print()
     else:
        print("File not found. Please sign up first.")      
    elif choice=="4":
        admin_login()
    elif choice=="5":
        print()
        print("Exiting program...")
        break
    else:
        print("Invalid Choice")
        print("Please Select From (1/2/3/4/5)")
        print()
    
  
    
