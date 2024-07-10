def welcome()->None:
    print("Welcome to the dealership database!")
    print("Note: Input the number shown in menu to execute what you want to do.")
    print()

def main_menu()->None:
    print("1. Add a new car brand on market")
    print("2. Add a new car model") #and the necessary data
    print("3. Edit specific information in the database")
    print("4. Delete a car model from database")
    print("5. Delete the whole stock of a car brand")
    print("6. Listing info about a car model")
    print("7. Listing all the info about a car brand")
    print("8. Listing the whole database in this application")
    print("9. Exporting all of the information as a .csv file")
    print("10. Engineering menu(programmers only)")
    print("11.Quit")

def Pass_request()->None:
    print("Engineering menu selected.")
    print("Please input the 25 characters long password to access it:")

def Pass_check(s:str)->bool: #gets a string, returns True or False
    passwords=[
        "y7LVFpbEAs6dwF5nrPPvG8Xt7",
        "eMVfWygRV5SR7CmVybwsknv4e",
        "mehPdUh5Pjq3np5XcG95LdmZ5",
        "eT8fpNYUEnht2jcgJM2nF8cU6",
        "yd9f728dHuUC4KsEa2XZBXQaY",
        "Wz8MJnHE6B7ejYa9GVkGYN6hq",
        "G7tpbea2bxGj3cPZNuR9WCASd",
        "CLzzfzSJCup9eWW886Xzf8B9j",
        "ueE2apZY25rUPRXXddDGLeYNz",
        "ExPDfETCnJ7AQMsmQMWnBGQCC"
    ]
    for key in passwords:
        if s==key:
            return True
    return False

def eng_menu():
    Pass_request()
    password=input() #the text asking to input the password is in Pass_request
    cnt=0 #counts the failed attempts to enter password
    while Pass_check(password)==False:
        cnt=cnt+1
        print("The password is not correct. Check it again or please ask for permission key before trying again.")
        if cnt%3==0:
            print("Seems like you have a few failed attempts in entering password...")
            print("Do you want to exit to main menu?")
            print("Use Y for Yes and N for No")
            n=input()
            if n=='Y':
                exit(0) 
        print("Please input the 25 characters long password:")    
        password=input()
    
    #the text menu
    print("Welcome! Here's what you can do:")
    print("1. Clear the whole database")
    print("2. Create a new json database")
    print("^^^ Only use it if there is no json file in the same directory as the executable")
    print("3. List the json database in dictionary format")
    print("4. List the csv file content")
    print("5. List the error log of the application")
    print("6. Go back to Main Menu")
    print("7. Quit")
    print("Please input the number coresponding to your option:")

def error_msg():
    print("Program error occured. Please check it in errors.txt")


