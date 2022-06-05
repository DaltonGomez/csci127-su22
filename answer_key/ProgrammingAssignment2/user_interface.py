"""
File: user_interface.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * TODO - Populate this list if you significantly use a reference
"""

import os

import jsonpickle

from Database import Database


def printMenu() -> None:
    """Prints the REPL UI menu"""
    print("======== REPL UI MENU ========")
    print("'c'  - Adds new course")
    print("'s'  - Adds new student")
    print("'g'  - Assigns a course and grade to a student")
    print("'p' - Prints a student's schedule in order of periods")
    print("'a'  - Calculates the student's grade point average")
    print("'b'  - Save a backup file of the database to disc")
    print("'D'  - Prints the entire database")
    print("'?'  - Prints this menu again")
    print("'x'  - Exits the database")


if __name__ == "__main__":
    # Greeting & Startup Prompt
    print("Hello! Welcome to the Student Database Software...")
    startupInput = input("Would you like to create a (n)ew database, or (l)oad an existing database?\n-> ")
    while startupInput != "n" and startupInput != "l":
        print("Your input was not recognized!")
        startupInput = input("Would you like to create a (n)ew database, or (l)oad an existing database?\n-> ")
    database = Database()
    if startupInput == "l":
        loadName = input("Please give the file name of the database to load?\n-> ")
        currDir = os.getcwd()
        catPath = os.path.join(currDir, "saved_files", loadName + ".txt")
        file = open(catPath, 'r')
        pickledDatabase = file.read()
        database = jsonpickle.decode(pickledDatabase)
        file.close()
    # Enters REPL UI Loop
    printMenu()
    userInput = ""
    while userInput != "x":
        userInput = input("\n\nWhat would you like to do?\n-> ")
        if userInput == "c":
            courseID = input("What's the course ID?\n-> ")
            courseName = input("What's the course name?\n-> ")
            creditHours = float(input("How many credit hours?\n-> "))
            period = int(input("What period does the course meet?\n-> "))
            database.addCourse(courseID, courseName, creditHours, period)
            print(courseName + " successfully added with ID " + courseID + ", and " + str(creditHours) +
                  " credits, meeting period " + str(period) + "!")
        elif userInput == "s":
            studentID = input("What's the student's ID?\n-> ")
            studentName = input("What's the student's name?\n-> ")
            database.addStudent(studentID, studentName)
            print(studentName + " successfully added with ID " + studentID + "!")
        elif userInput == "g":
            studentID = input("What's the student's ID you'd like to assign a course and grade to?\n-> ")
            courseID = input("What's the course's ID?\n-> ")
            grade = float(input("What is the student's grade (0-100)?\n-> "))
            database.assignCourseGradeToStudent(studentID, courseID, grade)
            print("Grade " + str(grade) + " in " + courseID + " successfully assigned to " + studentID + "!")
        elif userInput == "p":
            studentID = input("What's the student's ID whose schedule you'd like to print?\n-> ")
            database.printStudentsSchedule(studentID)
        elif userInput == "a":
            studentID = input("What's the student's ID you'd like to calculate a grade point average for?\n-> ")
            database.calculateGradePointAverage(studentID)
        elif userInput == "b":
            saveName = input("Please give a file name to save the database as?\n-> ")
            outputFile = jsonpickle.encode(database)
            currDir = os.getcwd()
            catPath = os.path.join(currDir, "saved_files", saveName + ".txt")
            file = open(catPath, 'w+')
            file.write(outputFile)
            file.close()
        elif userInput == "D":
            database.printAllCourses()
            database.printAllStudents()
        elif userInput == "?":
            printMenu()
        elif userInput == "x":
            print("Goodbye!")
        else:
            print("Your input was not recognized! Press '?' for the menu...")
