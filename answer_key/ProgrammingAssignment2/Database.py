"""
File: Database.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * TODO - Populate this list if you significantly use a reference
"""
from Course import Course
from Student import Student


class Database:
    """Class that defines a Database object"""

    def __init__(self):
        """Constructor of a Database instance"""
        self.courses = {}  # type: dict[str, Course]
        self.students = {}  # type: dict[str, Student]

    def addCourse(self, courseID: str, courseName: str, creditHours: float, period: int) -> None:
        """Adds a new course to the database"""
        newCourse = Course(courseID, courseName, creditHours, period)
        self.courses[courseID] = newCourse

    def addStudent(self, studentID: str, studentName: str) -> None:
        """Adds a new student to the database"""
        newStudent = Student(studentID, studentName)
        self.students[studentID] = newStudent

    def assignCourseGradeToStudent(self, studentID: str, courseID: str, grade: float) -> None:
        """Assigns a course and grade to the student"""
        thisStudent = self.students[studentID]
        thisStudent.assignCourseGrade(courseID, grade)

    def printStudentsSchedule(self, studentID: str) -> None:
        """Prints the student's schedule in order of periods"""
        thisStudent = self.students[studentID]
        schedule = []
        for courseGrade in thisStudent.courseGrades:
            thisCourse = self.courses[courseGrade[0]]
            periodCourseIDTuple = (thisCourse.period, thisCourse.courseID)
            schedule.append(periodCourseIDTuple)
        schedule.sort(key=lambda x: x[0])
        thisStudent.printStudentInfo()
        for course in schedule:
            thisCourse = self.courses[course[1]]
            thisCourse.printCourseInfo()

    def calculateGradePointAverage(self, studentID: str) -> float:
        """Calculates the weighted average of the students' grades"""
        thisStudent = self.students[studentID]
        totalCredits = 0
        creditsGradeList = []
        for courseGradeTuple in thisStudent.courseGrades:
            thisCourseID = courseGradeTuple[0]
            thisGrade = courseGradeTuple[1]
            thisCourseObj = self.courses[thisCourseID]
            thisCredits = thisCourseObj.creditHours
            totalCredits += thisCredits
            creditGradeTuple = (thisCredits, thisGrade)
            creditsGradeList.append(creditGradeTuple)
        gpa = 0
        for creditGradeTuple in creditsGradeList:
            gpa += (creditGradeTuple[0] / totalCredits) * creditGradeTuple[1]
        print("Student ID: " + studentID)
        print("Student Name: " + thisStudent.studentName)
        print("Student GPA: " + str(gpa))
        return gpa

    def printAllCourses(self) -> None:
        """Prints all courses logged in the database"""
        if len(self.courses.keys()) == 0:
            print("NO LOGGED COURSES!")
        else:
            print("######## ALL COURSES ########")
            for courseID in self.courses.keys():
                thisCourse = self.courses[courseID]
                thisCourse.printCourseInfo()

    def printAllStudents(self) -> None:
        """Prints all students logged in the database"""
        if len(self.students.keys()) == 0:
            print("NO LOGGED STUDENTS!")
        else:
            print("######## ALL STUDENTS ########")
            for studentID in self.students.keys():
                thisStudent = self.students[studentID]
                thisStudent.printStudentInfo()
                thisStudent.printStudentCourseGrades()
