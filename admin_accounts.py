import os
account_sep="#@!%^"             # SEPERATOR

def admin_choices():
    # FUCTION TO PROVIDE CHOICES TO ADMIN IN ACCOUNTS AREA
    
    print("\t\t Welcome To Accounts Area")
    print("\t1.See all Employees Accounts Details")
    print("\t2.Search any Employee For account Details")
    print("\t3.Delete any Employee account Details")
    print("\t4.Add any Employee account Details")
    print("\t5. Exit From THis Area")

def view_accounts(accounts_users, file_accoutns):
    """
    View details of all employee accounts.

    Parameters:
    - accounts_users (list): List of dictionaries containing employee account details.
    - file_accoutns (str): File path of the accounts file.

    Returns:
    - None
    """
    accounts_users.clear()
    with open(file_accoutns) as accounts:
        accounts.seek(0)  # seek cursor to zero
        # applying loop for taking linewise enteries
        for line in accounts:
            # making each line in file a list
            # using hardcode seperator
            data = line.strip().split(f"{account_sep}")
            # now appending in dictionary every user details
            user_accounts_dict = {"username": data[0], "password": data[1], "securityanswer": data[2]}
            # appending all dictionaries in list
            accounts_users.append(user_accounts_dict)
        # If there is data in accounts_users list
        if accounts_users:
            main_heading = "\"EMPLOYEES ACCOUNTS DETAILS\""
            print(main_heading.center(100))
            print()  # Add a gap after the main heading
            # Divider line after main heading
            print('-' * 100)
            # Subheadings with first letters capitalized and task numbers
            print("{:<5} {:<20} {:<20} {:<40}".format("S.No"," User-Names", "Employees Password", "Security Answers"))
            # Divider lines between subheadings
            print('-' * 100)
            for index, check in enumerate(accounts_users, 1):
                print("{:<5} {:<20} {:<20} {:<40}".format(index, check['username'], check['password'], check['securityanswer']))
        else:  # Else printing no data
            print()
            print("Sorry, no accounts of employees have been received yet.")
            print()

  
def search_user(accounts_users,file_accoutns):
     
     
     
     with open(file_accoutns) as accounts:
                accounts.seek(0)      # seek cursor to zero
                # applying loop for taking linewise enteries
                for line in accounts:
                    # making each line in file a list
                    # using hardcode seperator
                    data=line.strip().split(f"{account_sep}")
                    # now appending in dictionary every user details 
                    user_accounts_dict={"username":data[0],"password":data[1],"securityanswer":data[2]}
                    #appending all dictionaries in list
                    accounts_users.append(user_accounts_dict)
                if accounts_users:
                    user_name=input("Enter User Name Of Employee To Search Record:")
                    for check in accounts_users:
                        if user_name==check["username"]:
                            print("\tEmployee Details")
                            print()                           
                            print(f"1.Employe User Name: {check["username"]}")
                            print(f"2.Employee Password : {check["password"]}")
                            print(f"3.Employe's Security Answer : {check["securityanswer"]}")
                            print()
                            break
                    else:
                        print()
                        print(f"There is no Employee with that username {user_name}")
                
                else:   # Else printing no data
                    print()
                    print("Sorry , No accounts of employees have been received yet.")
                    print()


def delete_account(accounts_users, file_accounts, user_directory):
    """
    Function to delete an employee account and corresponding user file.

    This function takes in a list of employee accounts, the file path of the accounts file,
    and the directory containing user files. It prompts the admin to enter the username of the
    employee whose account they want to delete. If the username is found in the accounts list,
    the corresponding account is removed from the list and the user file is deleted. The accounts
    file is then updated with the new data. If no matching username is found, a message is displayed
    indicating that no employee was found with that username.

    Parameters:
    accounts_users (list): List containing dictionaries representing employee accounts.
    file_accounts (str): File path of the accounts file.
     user_directory (str): Directory containing user files.

    Returns:
     None

    """
    view_accounts(accounts_users, file_accounts)
    x = "#@!%^"  
    if accounts_users:  # Check if there are any accounts loaded
        while True:
            user_name = input("Enter User Name Of Employee To Delete Record (enter 0 to return): ")
            if user_name == "0":
                return  # Return if user wants to go back
            found = False  # Flag to track if user was found
            for check in accounts_users:
                if user_name == check["username"]:
                    # Remove user account
                    accounts_users.remove(check)
                    found = True  # Set flag to true if user was found
                    # Delete corresponding user file
                    user_file = os.path.join(user_directory, f"{user_name}.txt")
                    if os.path.exists(user_file):
                        os.remove(user_file)
            if found:
                # Rewrite the accounts file with updated data
                with open(file_accounts, "w") as account_file:
                    for check in accounts_users:
                        account_file.write(f"{check['username']}{x}{check['password']}{x}{check['securityanswer']}\n")
                print()
                print(f"Account for {user_name} has been deleted.")
                view_accounts(accounts_users, file_accounts)  # Show updated accounts
                return
            else:
                print()
                print(f"Sorry, No Employee Found With That Username: {user_name}")
    else:
        print("There are no employee accounts to delete.")
