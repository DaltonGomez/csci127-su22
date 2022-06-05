"""
File: Course.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * TODO - Populate this list if you significantly use a reference
"""


class Course:
    """Class that defines a Course object"""

    def __init__(self, courseID: str, courseName: str, creditHours: float, period: int):
        """Constructor of a Course instance"""
        self.courseID = courseID
        self.courseName = courseName
        self.creditHours = creditHours
        self.period = period

    def printCourseInfo(self) -> None:
        """Prints the course info to the console"""
        print("-------- COURSE --------")
        print("Course ID: " + self.courseID)
        print("Course Name: " + self.courseName)
        print("Credits Hours: " + str(self.creditHours))
        print("Period: " + str(self.period))
