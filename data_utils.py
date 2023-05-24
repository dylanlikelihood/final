#! /usr/bin/env python3
"""
    Title: data_utils.py
    Author: Dylan Armbruster
    Data: 5/24/2023
"""

import csv

# Read Student File
def readStudentFile():
    # students dictionary
    students = {}
    file = open("students.csv")
    reader = csv.reader(file)

    for row in reader:
        students[row[0]] = {'lastname': row[1], 'firstname': row[2]}

    file.close()

    return students  # Return the 'students' dictionary



# Read Courses
# def readCouresesFile():

    
# Student Validation Function
def studentIDValidation(studentID):
    students = readStudentFile()
    
    if studentID in students:
        return True
    else:
        return False


# Display menu
def displayMenu():
    print("info     - Student information")
    print("list     - Course listing")
    print("detail   - Course Detail")
    print("register - Register for a class")
    print("drop     - Drop class")
    print("menu     - Menu")
    print("exit     - End Session")
    print()

# Menu Selection
def menuSelection():
    # Display menu
    while True:
        displayMenu()
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

# # list
# def listSelection(studentID):
    

    
# Add New Student Function
def addNewStudent(studentID):
    # Variables
    students = readStudentFile()

    # Last Name User validation
    while True:
        last_name = input("Enter your last name: ").lower()
        if last_name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid last name.")
    # First Name User validation
    while True:
        first_name = input("Enter your first name: ").lower()
        if first_name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid first name.")
    
    fl = first_name[0]
    newStudentID = f"{fl}{last_name}"
    index = 0

    while f'{newStudentID}{index}' in students:
        index += 1
    
    newStudentID = f"{newStudentID}{index}"
    students[newStudentID] = [last_name, first_name]

    print(f"Greetings {newStudentID}, what would you like to do today?")
    menuSelection()


# Login Function
def login():
    students = readStudentFile()
    while True:
        # User input
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")
        print()
        if studentID == 'exit':                 # Exit Login
          print("\nSession ended.\n")
          break
        elif studentID == 'add':                # Add student name
            fristName = addNewStudent(studentID)
            print(f"Good morning {fristName}, what would you like to do today?\n")
        elif studentID in readStudentFile():
            studentsFirstName = students[studentID]['firstname'] # Get first name from dictionary
            print(f"Welcome {studentsFirstName}, what would you like to do today?") # print first name
            menuSelection()
        else:
            break
    
