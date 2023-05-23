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

# Student Validation Function
def validStudent(student_id):
    for student in student_data:
        if student_id == student[0]:
            return True
    return False

# Rest of the code...

# Add a check to see if the file opened
readStudentFile(FILENAME)

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
    if studentID == "add":
      students = ""
      last_name = input("Enter the student's last name: ").lower()
      first_name = input("Enter the student's first name: ").lower()

    # Generate student ID
    numeric_value = 0
    student_id = f"{first_name[0]}{last_name}{numeric_value}"
    while validStudent(student_id):
        numeric_value += 1
        student_id = f"{first_name[0]}{last_name}{numeric_value}"
    print(f"Student {student_id} has been added.\n")
    print(f"Good morning {first_name}, what would you like to do today?\n")

      
    while True:
          displayMenu()
          selection = input("Enter selection: ")
          if selection.lower() == "info":
            print("You're in info")
            # student information
          elif selection.lower() == "list":
            print("you're in list")
            # course listing
          elif selection.lower() == "detail":
             print("You're in detail")
             # Course detail
          elif selection.lower() == "register":
            print("You'r'e in register")
            # register for a class
          elif selection.lower() == "drop":
            print("You're in drop")
            # drop class
          elif selection.lower() == "menu":
             print("You're in menu")
             # menu
          else: 
            print("Exit")
            break


# Login Function
def login():
    while True:
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")

        if studentID == 'exit':
            print("\nSession ended.\n")
            exit()

        if validStudent(studentID):
            break
        addNewStudent(studentID)
        return studentID
