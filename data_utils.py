#! /usr/bin/env python3

import csv



# Read File
def readStudentFile():
  file = open("students.csv", "r")
  students = list(csv.reader(file, delimiter=","))
  print()
  file.close()
  return students

# Read Courses
# def readCouresesFile():

    
# Student Validation Function
def studentIDValidation(studentID):
    students = readStudentFile()
    for studentID in students:
        if studentID == students[0]:
          return False
        return True


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

# # list
# def listSelection():

    
# Add New Student Function
def addNewStudent(studentID):
    # Variables
    first_name = []
    last_name = []

    # Get student's last name
    for _ in range(3):  # Allow a maximum of 3 attempts
        last_name_input = input("Enter the student's last name: ")
        # Input validation
        if last_name_input.isalpha() and last_name_input.strip() != "":
            last_name = list(last_name_input)
            break
        else:
            print("Invalid input. Please enter a valid last name.")

    # Get student's first name
    for _ in range(3):  # Allow a maximum of 3 attempts
        first_name_input = input("Enter the student's first name: ")
        # Input validation
        if first_name_input.isalpha() and first_name_input.strip() != "":
            first_name = list(first_name_input)
            break
        else:
            print("Invalid input. Please enter a valid first name.")

    # Generate student ID
    student_id = f"{first_name[0].lower()}{last_name[0].lower()}"
    index = 0

    # while f'{student_id}{index}' in [student[0] for student in student_data]:
    #     index += 1

    # student_id = f"{student_id}{index}"
    # student_data.append([student_id, last_name, first_name])
    # print(f"Student {student_id} has been added.\n")
    return ''.join(first_name)  # Join the first name characters into a string




# Login Function
def login():
    students = readStudentFile()
    while True:
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")
        print()
        # Input validation
        studentIDValidation(studentID)

        # Exit Login
        if studentID == 'exit':
          print("\nSession ended.\n")
          break

        # Add student name
        if studentID == 'add':
            fristName = addNewStudent(studentID)
            print(f"Good morning {fristName}, what would you like to do today?\n")
            continue
            

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
