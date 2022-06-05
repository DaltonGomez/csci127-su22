"""
File: Student.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * TODO - Populate this list if you significantly use a reference
"""


class Student:
    """Class that defines a Student object"""

    def __init__(self, studentID: str, studentName: str):
        """Constructor of a Student instance"""
        self.studentID = studentID
        self.studentName = studentName
        self.courseGrades = []  # type: list[tuple[str, float]]

    def assignCourseGrade(self, courseID: str, grade: float) -> None:
        """Gives the student a course and grade tuple into the students courseGrades list"""
        courseGradeTuple = (courseID, grade)
        self.courseGrades.append(courseGradeTuple)

    def printStudentInfo(self) -> None:
        """Prints the student's info to the console"""
        print("======== STUDENT ========")
        print("Student ID: " + self.studentID)
        print("Student Name: " + self.studentName)

    def printStudentCourseGrades(self) -> None:
        """Prints all the student's course grades"""
        if len(self.courseGrades) == 0:
            print("NO COURSE GRADES LOGGED!")
        else:
            print("Course Grades: ")
            for courseGrade in self.courseGrades:
                print(courseGrade)
