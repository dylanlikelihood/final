#! /usr/bin/env python3

import data_utils




def main():
    # Main Prompt for user
    print("Saddleback Registration")
    studentID = data_utils.login()

        # Display menu
    while True:
        data_utils.displayMenu()
        selection = input("Enter selection: ")
        if selection.lower() == "info":
            print("You're in info")
            # Student information
        elif selection.lower() == "list":
            print("You're in list")
            # Course listing
        elif selection.lower() == "detail":
            print("You're in detail")
            # Course detail
        elif selection.lower() == "register":
            print("You're in register")
            # Register for a class
        elif selection.lower() == "drop":
            print("You're in drop")
            # Drop class
        elif selection.lower() == "menu":
            print("You're in menu")
            # Menu
        else: 
            print("Invalid selection. Please try again.\n")
    


    
            



if __name__ == "__main__":
    main()
