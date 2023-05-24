#! /usr/bin/env python3

import csv
import os

FILENAME = "students.csv"

student_data = []

# Read File
def readStudentFile(file_name):
    here = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(here, FILENAME)

    try:
        with open(my_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                student_data.append(row)
    except FileNotFoundError:
        print(f"File '{my_file}' not found.")
        exit()

# Add a check to see if the file opened
readStudentFile(FILENAME)

# Student Validation Function
def validStudent(student_id):
    for student in student_data:
        if student_id == student[0]:
            return True
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


# Add New Student Function
def addNewStudent(studentID):
    # Variables
    first_name = ""
    last_name = ""

    while True:
        # Get student's last name
        last_name = input("Enter the student's last name: ")
        # Input validation
        if last_name.isalpha() and last_name.strip() != "":
            break
        else:
            print("Student's last name can only contain alphabetic letters and cannot be left blank.")
      
        # Get student's first name
        first_name = input("Enter the student's first name: ")
        # Input validation
        if first_name.isalpha() and first_name.strip() != "":
            break
        else:
            print("Student's first name can only contain alphabetic letters and cannot be left blank.")

    # Generate student ID
    student_id = f"{first_name[0].lower()}{last_name.lower()}"
    index = 0
     
    while f'{student_id}{index}' in [student[0] for student in student_data]:
        index += 1
    
    student_id = f"{student_id}{index}"
    student_data.append([student_id, last_name, first_name])

    print(f"Student {student_id} has been added.\n")
    print(f"Good morning {first_name}, what would you like to do today?\n")

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


# Login Function
def login():
    while True:
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")
        addNewStudent(studentID)

        if studentID == 'exit':
            print("\nSession ended.\n")
