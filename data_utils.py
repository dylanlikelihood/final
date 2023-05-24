#! /usr/bin/env python3

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
        # User input
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")
        print()
        if studentID == 'exit':                 # Exit Login
          print("\nSession ended.\n")
          break
        elif studentID == 'add':                # Add student name
            fristName = addNewStudent(studentID)
            print(f"Good morning {fristName}, what would you like to do today?\n")
            break
        elif studentID in readStudentFile():
            studentsFirstName = students[studentID]['firstname'] # Get first name from dictionary
            print(f"Welcome {studentsFirstName}, what would you like to do today?") # print first name
            break
        else:
            print("You're in info")
