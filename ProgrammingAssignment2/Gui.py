import tkinter as tk
from tkinter import *

from Database import Database


class Gui:
    """GUI class used to create a graphical user interface for the student database"""

    def __init__(self):
        """Constructor of Gui class"""
        ###################################
        #  General Instance Variables of the Gui object
        ###################################
        self.database = Database()

        ###################################
        #  GUI Setup
        ###################################
        # Initialize window
        self.window = tk.Tk()
        self.window.wm_title("Student Database")
        # Set up menu frame
        self.menuFrame = tk.Frame(master=self.window, width=200, height=600)
        self.menuTitle = tk.Label(master=self.menuFrame, text='Menu', font=('Arial', 14))
        self.menuTitle.pack(padx=1, pady=1, side='top')
        self.addNewStudentButton = tk.Button(master=self.menuFrame, text='Add New Student', font=('Arial', 10),
                                             command=self.addNewStudentUI, width=25, height=1, bg='pale green')
        self.addNewStudentButton.pack(padx=3, pady=3)
        self.addNewCourseButton = tk.Button(master=self.menuFrame, text='Add New Course', font=('Arial', 10),
                                            command=self.addNewCourseUI, width=25, height=1, bg='light blue')
        self.addNewCourseButton.pack(padx=3, pady=3)
        self.assignCourseToStudentButton = tk.Button(master=self.menuFrame, text='Assign Course To Student',
                                                     font=('Arial', 10),
                                                     command=self.assignCourseToStudentUI, width=25, height=1,
                                                     bg='light goldenrod')
        self.assignCourseToStudentButton.pack(padx=3, pady=3)
        self.calculateGpaButton = tk.Button(master=self.menuFrame, text='Calculate GPA', font=('Arial', 10),
                                            command=self.calculateGpaUI, width=25, height=1, bg='plum2')
        self.calculateGpaButton.pack(padx=3, pady=3)
        # Set up message frame
        self.messageFrame = tk.Frame(master=self.window, width=600, height=600, borderwidth=10)
        self.messageTitle = tk.Label(master=self.messageFrame, text='Messages:', font=('Arial', 14))
        self.messageTitle.pack(padx=5, pady=5)
        self.messageText = tk.StringVar(master=self.messageFrame, value='Welcome to Student Database... \n\n A basic '
                                                                        'DBMS for students and courses!')
        self.message = tk.Message(master=self.messageFrame, textvariable=self.messageText, relief=RAISED,
                                  justify=CENTER)
        self.message.pack(padx=10, pady=10)
        # Pack frames
        self.menuFrame.pack(padx=10, pady=5, side='left')
        self.messageFrame.pack(padx=10, pady=5)
        # Additional Instance Attributes- Instantiated by Control Actions
        self.newStudentWindow = None
        self.newStudentID = None
        self.newStudentName = None
        self.addStudentButton = None
        self.newCourseWindow = None
        self.newCourseID = None
        self.newCourseName = None
        self.addCourseButton = None
        self.newCourseCredits = None
        self.newCoursePeriod = None
        self.newAssignmentWindow = None
        self.assignmentStudentID = None
        self.assignmentCourseID = None
        self.assignmentGrade = None
        self.assignmentButton = None
        self.gpaWindow = None
        self.gpaStudentID = None
        self.gpaButton = None

    ###################################
    #  Control Actions
    ###################################
    def addNewStudentUI(self) -> None:
        """Creates popup window for adding a new student"""
        # New Student Popup Window
        self.newStudentWindow = tk.Tk()
        self.newStudentWindow.wm_title('Add a New Student...')
        # New Student Title Frame
        newStudentTitleFrame = tk.Frame(master=self.newStudentWindow, width=400, height=600)
        newStudentTitle = tk.Label(master=newStudentTitleFrame, text='Add New Student', font=('Arial', 12))
        newStudentTitle.pack(padx=5, pady=5, side='top')
        # New Student Frame
        newStudentFrame = tk.Frame(master=self.newStudentWindow, width=400, height=600)
        # Student ID Entry
        self.newStudentID = tk.StringVar(master=newStudentFrame, value='<StudentID>')
        studentIDFieldEntry = tk.Entry(master=newStudentFrame, textvariable=self.newStudentID)
        studentIDFieldEntry.pack(padx=5, pady=5, side='left')
        # Student Name Entry
        self.newStudentName = tk.StringVar(master=newStudentFrame, value='<Student Name>')
        studentNameFieldEntry = tk.Entry(master=newStudentFrame, textvariable=self.newStudentName)
        studentNameFieldEntry.pack(padx=5, pady=5, side='left')
        # Execute Add Student Button
        runAddStudentFrame = tk.Frame(master=self.newStudentWindow, width=400, height=600)
        self.addStudentButton = tk.Button(master=runAddStudentFrame, text='Add Student', font=('Arial', 10),
                                          command=self.addNewStudent, width=25, height=1, bg='salmon')
        self.addStudentButton.pack(padx=3, pady=3)
        newStudentTitleFrame.pack(padx=5, pady=10)
        newStudentFrame.pack(padx=5, pady=10)
        runAddStudentFrame.pack(padx=5, pady=10)

    def addNewStudent(self) -> None:
        """Calls the add new student method in the database object"""
        thisStudentID = self.newStudentID.get()
        thisStudentName = self.newStudentName.get()
        self.messageText.set("ADDING STUDENT\nStudent ID: " + thisStudentID + "\nStudent Name: " + thisStudentName)
        self.database.addStudent(thisStudentID, thisStudentName)
        self.message.pack(padx=10, pady=10)

    def addNewCourseUI(self) -> None:
        """Creates popup window for adding a new course"""
        # New Course Popup Window
        self.newCourseWindow = tk.Tk()
        self.newCourseWindow.wm_title('Add a New Course...')
        # New Course Title Frame
        newCourseTitleFrame = tk.Frame(master=self.newCourseWindow, width=400, height=600)
        newCourseTitle = tk.Label(master=newCourseTitleFrame, text='Add New Course', font=('Arial', 12))
        newCourseTitle.pack(padx=5, pady=5, side='top')
        # New Course Frame
        newCourseFrame = tk.Frame(master=self.newCourseWindow, width=400, height=600)
        # Course ID Entry
        self.newCourseID = tk.StringVar(master=newCourseFrame, value='<Course ID>')
        courseIDFieldEntry = tk.Entry(master=newCourseFrame, textvariable=self.newCourseID)
        courseIDFieldEntry.pack(padx=5, pady=5, side='left')
        # Course Name Entry
        self.newCourseName = tk.StringVar(master=newCourseFrame, value='<Course Name>')
        courseNameFieldEntry = tk.Entry(master=newCourseFrame, textvariable=self.newCourseName)
        courseNameFieldEntry.pack(padx=5, pady=5, side='left')
        # Course Credit Entry
        self.newCourseCredits = tk.StringVar(master=newCourseFrame, value='<Course Credits>')
        courseCreditFieldEntry = tk.Entry(master=newCourseFrame, textvariable=self.newCourseCredits)
        courseCreditFieldEntry.pack(padx=5, pady=5, side='left')
        # Course Period Entry
        self.newCoursePeriod = tk.StringVar(master=newCourseFrame, value='<Course Period>')
        coursePeriodFieldEntry = tk.Entry(master=newCourseFrame, textvariable=self.newCoursePeriod)
        coursePeriodFieldEntry.pack(padx=5, pady=5, side='left')
        # Execute Add Course Button
        runAddCourseFrame = tk.Frame(master=self.newCourseWindow, width=400, height=600)
        self.addCourseButton = tk.Button(master=runAddCourseFrame, text='Add Course', font=('Arial', 10),
                                         command=self.addNewCourse, width=25, height=1, bg='salmon')
        self.addCourseButton.pack(padx=3, pady=3)
        newCourseTitleFrame.pack(padx=5, pady=10)
        newCourseFrame.pack(padx=5, pady=10)
        runAddCourseFrame.pack(padx=5, pady=10)

    def addNewCourse(self) -> None:
        """Calls the add new course method in the database object"""
        thisCourseID = self.newCourseID.get()
        thisCourseName = self.newCourseName.get()
        thisCourseCredits = self.newCourseCredits.get()
        thisCoursePeriod = self.newCoursePeriod.get()
        self.messageText.set("ADDING COURSE\nCourse ID: " + thisCourseID + "\nCourse Name: " + thisCourseName +
                             "\nCourse Credits: " + thisCourseCredits + "\nCourse Period: " + thisCoursePeriod)
        self.database.addCourse(thisCourseID, thisCourseName, float(thisCourseCredits), int(thisCoursePeriod))
        self.message.pack(padx=10, pady=10)

    def assignCourseToStudentUI(self) -> None:
        """Creates popup window for assigning a course to a student"""
        # New Assignment Popup Window
        self.newAssignmentWindow = tk.Tk()
        self.newAssignmentWindow.wm_title('Assign a Course To a Student...')
        # New Assignment Title Frame
        newAssignmentTitleFrame = tk.Frame(master=self.newAssignmentWindow, width=400, height=600)
        newAssignmentTitle = tk.Label(master=newAssignmentTitleFrame, text='Assign Course To Student',
                                      font=('Arial', 12))
        newAssignmentTitle.pack(padx=5, pady=5, side='top')
        # New Assignment Frame
        newAssignmentFrame = tk.Frame(master=self.newAssignmentWindow, width=400, height=600)
        # Student ID Entry
        self.assignmentStudentID = tk.StringVar(master=newAssignmentFrame, value='<Student ID>')
        assignmentStudentIDFieldEntry = tk.Entry(master=newAssignmentFrame, textvariable=self.assignmentStudentID)
        assignmentStudentIDFieldEntry.pack(padx=5, pady=5, side='left')
        # Course ID Entry
        self.assignmentCourseID = tk.StringVar(master=newAssignmentFrame, value='<Course ID>')
        assignmentCourseIDFieldEntry = tk.Entry(master=newAssignmentFrame, textvariable=self.assignmentCourseID)
        assignmentCourseIDFieldEntry.pack(padx=5, pady=5, side='left')
        # Grade Entry
        self.assignmentGrade = tk.StringVar(master=newAssignmentFrame, value='<Grade>')
        assignmentGradeFieldEntry = tk.Entry(master=newAssignmentFrame, textvariable=self.assignmentGrade)
        assignmentGradeFieldEntry.pack(padx=5, pady=5, side='left')
        # Execute Add Assignment Button
        runAssignmentFrame = tk.Frame(master=self.newAssignmentWindow, width=400, height=600)
        self.assignmentButton = tk.Button(master=runAssignmentFrame, text='Add Course', font=('Arial', 10),
                                          command=self.assignCourseToStudent, width=25, height=1, bg='salmon')
        self.assignmentButton.pack(padx=3, pady=3)
        newAssignmentTitleFrame.pack(padx=5, pady=10)
        newAssignmentFrame.pack(padx=5, pady=10)
        runAssignmentFrame.pack(padx=5, pady=10)

    def assignCourseToStudent(self) -> None:
        """Calls the assign course to student button on the database object"""
        thisStudentID = self.assignmentStudentID.get()
        thisCourseID = self.assignmentCourseID.get()
        thisGrade = self.assignmentGrade.get()
        self.messageText.set("ASSIGNING COURSE TO STUDENT\nStudent ID: " + thisStudentID + "\nCourse ID: " +
                             thisCourseID + "\nGrade: " + thisGrade)
        self.database.assignCourseGradeToStudent(thisStudentID, thisCourseID, float(thisGrade))
        self.message.pack(padx=10, pady=10)

    def calculateGpaUI(self) -> None:
        """Creates popup window for calculating GPA"""
        # GPA Popup Window
        self.gpaWindow = tk.Tk()
        self.gpaWindow.wm_title("Calculate a Student's GPA...")
        # GPA Title Frame
        gpaTitleFrame = tk.Frame(master=self.gpaWindow, width=400, height=600)
        gpaTitle = tk.Label(master=gpaTitleFrame, text='Calculate Student GPA', font=('Arial', 12))
        gpaTitle.pack(padx=5, pady=5, side='top')
        # New Assignment Frame
        gpaFrame = tk.Frame(master=self.gpaWindow, width=400, height=600)
        # Student ID Entry
        self.gpaStudentID = tk.StringVar(master=gpaFrame, value='<Student ID>')
        gpaStudentIDFieldEntry = tk.Entry(master=gpaFrame, textvariable=self.gpaStudentID)
        gpaStudentIDFieldEntry.pack(padx=5, pady=5, side='left')
        # Execute Add Course Button
        runGpaFrame = tk.Frame(master=self.gpaWindow, width=400, height=600)
        self.gpaButton = tk.Button(master=runGpaFrame, text='Calculate GPA', font=('Arial', 10),
                                   command=self.calculateGpa, width=25, height=1, bg='salmon')
        self.gpaButton.pack(padx=3, pady=3)
        gpaTitleFrame.pack(padx=5, pady=10)
        gpaFrame.pack(padx=5, pady=10)
        runGpaFrame.pack(padx=5, pady=10)

    def calculateGpa(self) -> None:
        """Calls the assign course to student button on the database object"""
        thisStudentID = self.gpaStudentID.get()
        gpa = self.database.calculateGradePointAverage(thisStudentID)
        self.messageText.set("STUDENT GPA\nStudent ID: " + thisStudentID + "\nGPA: " + str(gpa))
        self.message.pack(padx=10, pady=10)


if __name__ == '__main__':
    gui = Gui()
    tk.mainloop()
