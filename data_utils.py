#! /usr/bin/env python3
"""
    Title: data_utils.py
    Author: Dylan Armbruster
    Data: 5/24/2023
"""

import csv
import datetime

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
def readCoursesFile():
    courses = {}
    file = open("courses.csv")
    reader = csv.reader(file)

    for row in reader:
        course_code = row[0]
        courses[course_code] = {
            'ticket': row[0],
            'code': row[1],
            'course name': row[2],
            'units': row[3],
            'day': row[4],
            'time': row[5],
            'instructor': row[6]
        }

    file.close()

    return courses

# Read Registrations
def readRegistrationsFile():
    registrations = {}
    file = open("registration.csv")
    reader = csv.reader(file)

    for row in reader:
        studentID = row[0]
        course_code = row[1]

        if studentID in registrations:
            registrations[studentID].append(course_code)
        else:
            registrations[studentID] = [course_code]

    file.close()

    return registrations

# Greeting Student Function
def greet_student(student_id):
    students = readStudentFile()
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 0 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    if student_id in students:
        student = students[student_id]
        first_name = student['firstname']
        print(f"\n{greeting}, {first_name}, what would you like to do today?")


# Drop Course Function
def dropCourse(studentID):
    registered_courses = readRegistrationsFile()

    # Retrieve the registered courses for the student
    student_registrations = registered_courses.get(studentID, [])

    if not student_registrations:
        print("You are not registered for any courses.")
        return

    courseTicket = input("Enter the course ticket number to drop: ")

    if courseTicket not in student_registrations:
        print("You are not registered for the specified course.")
        return

    student_registrations.remove(courseTicket)
    registered_courses[studentID] = student_registrations

    # Save the updated registrations to the file
    with open("registration.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for studentID, courses in registered_courses.items():
            for course in courses:
                writer.writerow([studentID, course])

    print("Course dropped successfully.")

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

# Student Information Function:
def showStudentInformation(studentID):
    students = readStudentFile()
    courses = readCoursesFile()
    registered_courses = readRegistrationsFile()

    if studentID in students:
        student = students[studentID]
        last_name = student['lastname']
        first_name = student['firstname']

        # Retrieve the registered courses for the student
        student_registrations = registered_courses.get(studentID, [])  # Retrieve registered courses for student

        # Print student information
        print("Student id:", studentID)
        print("Last Name:", last_name)
        print("First Name:", first_name)

        # Print registered courses
        print("Registered Courses:")
        print("Ticket Code   Course Name                          Units Day    Time          Instructor")
        print("========================================================================================")
        for course_code in student_registrations:
            course_details = courses.get(course_code, {})
            print(f"{course_code:12} {course_details.get('course name', '')[:38]:38} {course_details.get('units', ''):5} {course_details.get('day', ''):5} {course_details.get('time', ''):13} {course_details.get('instructor', '')}")
        print()
        print()

        # Print total line
        num_courses = len(student_registrations)
        total_units = sum(float(courses.get(course_code, {}).get('units', 0)) for course_code in student_registrations)
        print(f"{num_courses} Course(s) Registered                                    Units: {total_units}")
    

def menuSelection(studentID):
    while True:
        print()
        displayMenu()
        selection = input("Enter selection: ")
        if selection.lower() == "info":
            showStudentInformation(studentID)
        elif selection.lower() == "list":
            # Call the function for listing courses
            listCourses()
        elif selection.lower() == "detail":
            # Call the function for course details
            showCourseDetails()
        elif selection.lower() == "register":
            # Call the function for registering a course
            registerCourse(studentID)
        elif selection.lower() == "drop":
            # Call the function for dropping a course
            dropCourse(studentID)
        elif selection.lower() == "menu":
            # Show the menu options again
            continue
        elif selection.lower() == "exit":
            print("End session.\n")
            break
        else:
            print("Invalid selection. Please try again.\n")
   
# Generate Unique Student ID
def generateUniqueStudentID(first_name, last_name, students):
    fl = first_name[0]
    student_id = f"{fl}{last_name}"
    index = 0

    while f'{student_id}{index}' in students:
        index += 1

    return f"{student_id}{index}"


# Add New Student Function
def addNewStudent():
    students = readStudentFile()

    while True:
        last_name = input("Enter your last name: ").lower()
        if last_name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid last name.")

    while True:
        first_name = input("Enter your first name: ").lower()
        if first_name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid first name.")

    student_id = generateUniqueStudentID(first_name, last_name, students)
    students[student_id] = {'lastname': last_name, 'firstname': first_name}

    # Save the updated students dictionary to the file
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for student_id, student in students.items():
            writer.writerow([student_id, student['lastname'], student['firstname']])

    print(f"Student {student_id} has been added.")
    return student_id

# Register for a Course Function:
def registerCourse(student_id):
    students = readStudentFile()
    courses = readCoursesFile()
    registrations = readRegistrationsFile()

    # Check if student has reached the maximum unit limit
    student_registrations = registrations.get(student_id, [])
    total_units = sum(float(courses.get(course_code, {}).get('units', 0)) for course_code in student_registrations)
    if total_units >= 12:
        print("Maximum unit limit (12) reached. Cannot register for more courses.\n")
        return

    course_ticket = input("Enter the course ticket number to register: ")
    course = courses.get(course_ticket)
    if course:
        # Check if student is already registered for the course
        if course_ticket in student_registrations:
            print("You are already registered for this course.\n")
            return

        # Check if course has reached the maximum enrollment
        registered_students = registrations.get(course_ticket, [])
        if len(registered_students) >= 15:
            print("Course has reached maximum enrollment. Cannot register for the course.\n")
            return

        # Register the student for the course
        registrations[student_id] = student_registrations + [course_ticket]
        registered_students.append(student_id)

        # Save the updated registrations to the file
        with open("registration.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for student_id, registered_courses in registrations.items():
                writer.writerow([student_id] + registered_courses)

        print(f"{student_id} added to the {course_ticket}.\n")
    else:
        print("Course not found.\n")


# Course Listing Function:
def listCourses():
    courses = readCoursesFile()
    print("Course Listing:")

    choice = input("List by Course Ticket or Course Code? (t/c): ")

    if choice.lower() == "t":
        sorted_courses = sorted(courses.items(), key=lambda x: x[1]['ticket'])
    elif choice.lower() == "c":
        sorted_courses = sorted(courses.items(), key=lambda x: x[1]['code'])
    else:
        print("Invalid choice.")
        return

    # Display the table header
    print("Ticket Code   Course Name                          Units Day    Time          Instructor")
    print("========================================================================================")

    # Iterate through each course and display its details
    for course_code, course_details in sorted_courses:
        course_info = []
        course_info.append(course_details['ticket'])
        course_info.append(course_details['code'])
        course_info.append(course_details['course name'])
        course_info.append(course_details['units'])
        course_info.append(course_details['day'])
        course_info.append(course_details['time'])
        course_info.append(course_details['instructor'])

        if course_info[4].lower() == "online":
            course_info[4] = "Online"
            course_info[5] = ""  # Blank out the time for online courses

        # Print the course information
        print("{:<12} {:<10} {:<38} {:<5} {:<5} {:<13} {}".format(*course_info))

    print()


# Function to sort courses by ticket
def sort_by_ticket(course):
    return course[1]['ticket']

# Function to sort courses by code
def sort_by_code(course):
    return course[1]['code']



# Course Detail Function:
def showCourseDetails(): 
    courses = readCoursesFile()

    # Prompt the user to enter the course ticket number
    course_ticket = input("Enter the course ticket number: ")
    course = courses.get(course_ticket)
    if course:
        print("Code:", course['code'])
        print("Course Name: ", course['course name'])
        print("Units:", course['units'])
        print("Day:", course['day'])
        print("Time:", course['time'])
        print("Instructor:", course['instructor'])
        print()

        # Retrieve registered students for the course
        registrations = readRegistrationsFile()
        registered_students = []
        for student_id, registered_courses in registrations.items():
            if course_ticket in registered_courses:
                student = readStudentFile().get(student_id)
                registered_students.append((student_id, student['lastname'], student['firstname']))

        # Print registered students
        print("Registered Students:")
        print("Student ID  Last Name   First Name")
        print("==================================")
        for student in registered_students:
            print(f"{student[0]:11} {student[1]:11} {student[2]}")
        print()

        print(f"Total students registered: {len(registered_students)}")
    else:
        print("Course not found.\n")

# Login Function
def login():
    students = readStudentFile()
    while True:
        # User input
        studentID = input("\nEnter Student Id (or 'add' to add a new student, or 'exit' to exit the application): ")
        print()
        if studentID == 'exit':
            print("\nSession ended.\n")
            break
        elif studentID == 'add':
            firstName = addNewStudent()
            greet_student(studentID)
            menuSelection(studentID)
        elif studentID in students:  # Check if the student ID is present in the dictionary
            studentFirstName = students[studentID]['firstname']
            greet_student(studentID)
            menuSelection(studentID)
            break
        else:
            print("Invalid ID, please try again")
