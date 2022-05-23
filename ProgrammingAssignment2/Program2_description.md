# Programming Assignment #2

### Instructions:

Please complete the questions/problems described here by creating the necessary `.py` files. Once completed,
submit the individual files of this directory to the Programming Assignment #2 submission box on
[Gradescope](https://www.gradescope.com/).

## Question #1 [20 Points]: Create a file `Course.py` that defines an object of the Course class, including:

**1a) A constructor that can be called as `Course(courseID: str, courseName: str, creditHours: float, period: int)`.
In the constructor, you should assign each input argument to an instance attribute of the same name.**

**1b) An instance method that can be called as `course.printCourseInfo()`, which prints all the instance attributes
for the course.**

**1c) A small amount of testing code at the end of the file that allows you to instantiate the `Course` class and
call the `printCourseInfo()` method on a test course object.**

## Question #2 [20 Points]: Create a file `Student.py` that defines an object of the Student class, including:

**2a) A constructor that can be called as `Student(studentID: str, studentName: str)`. In the constructor,
you should assign each input argument to an instance attribute of the same name. You should also declare an
instance attribute `courseGrades`, assign it an empty list and the data type `list[tuple[str, float]]`.**

**2b) An instance method that can be called as `student.printStudentInfo()`, which prints the student's ID and name
to the console.**

**2c) An instance method that can be called as `student.assignCourseGrade(courseID: str, grade: float)`, where the
`courseID` is a string that maps to a course object's `courseID` and the grade is a float on the range of 0 - 100.
The method should package the two values as the tuple `(courseID, grade)` and append the tuple to the instance
attribute `student.courseGrades`.**

**2d) A small amount of testing code at the end of the file that allows you to instantiate the `Student` class and
call the `printStudentInfo()` and `assignCourseGrade(courseID, grade)` methods on a test student object.**

## Question #3 [20 Points]: Create a file `Database.py` that defines an object of the Database class, including:

**3a) A constructor that can be called as `Database()`. In the constructor, you should declare two instance attributes.
The first, `students`, should be assigned an empty dictionary and have the data type `dict[str, Student]`, and the
second, `courses`, should be assigned an empty dictionary and have the data type `dict[str, Course]`.**

**3b) An instance method that can be called as `addCourse(courseID: str, courseName: str, creditHours: float,
period: int)`. This method should instantiate a new `Course` object and add it to the instance attribute `self.courses`
dictionary with the key `courseID` and the value of the new `Course` object.**

**3c) An instance method that can be called as `addStudent(studentID: str, studentName: str))`. This method should
instantiate a new `Student` object and add it to the instance attribute `self.students` dictionary with the key
`studentID` and the value of the new `Student` object.**

**3d) An instance method that can be called as `assignCourseGradeToStudent(studentID: str, courseID: str,
grade: float)`. This method should get the correct `Student` object out of the `self.students` dictionary and then call
the method `assignCourseGrade(courseID, grade)` on that student.**

**3e) Two instance methods that can be called as `database.printAllCourses()` and `database.printAllStudents()`, which
iterates through the `self.courses` and `self.students` dictionary, calling the `printCourseInfo()` and
`printStudentInfo()` methods on each object, respectively.**

**3f) A small amount of testing code at the end of the file that allows you to instantiate the `Database`, `Course` and
`Student` class and call these database methods on a test database object.**

## Question #4 [20 Points]: Add to your `Database.py` class the following methods:

**4a) An instance method that can be called as `printStudentsSchedule(studentID: str)`, which should get the student
and print all their assigned courses in order of ascending periods. Note that this requires some sorting of the courses
by their period. You may assume that all courses will have unique periods. The sorted schedule should be printed to the
console.**

**4b) An instance method that can be called as `calculateGradePointAverage(studentID: str)`, which should get the
student and compute their grade point average (GPA). Note that GPA is calculated as the sum of
(grade * (courseCredits/totalCredits)) for all courses in the student's schedule. The calculated GPA should be printed
to the console.**

**4c) A small amount of testing code at the end of the file that allows you to instantiate the `Database`, `Course` and
`Student` class and call these database methods on a test database object.**

## Question #5 [10 Points]: Create a file `user_interface.py` that runs a REPL UI with the functionality proposed in the following `printMenu()` function:

`def printMenu() -> None:`      
`"""Prints the REPL UI menu"""`   
`print("======== REPL UI MENU ========")`   
`print("'c' - Adds new course")`   
`print("'s' - Adds new student")`   
`print("'g' - Assigns a course and grade to a student")`   
`print("'p' - Prints a student's schedule in order of periods")`   
`print("'a' - Calculates the student's grade point average")`
`print("'D' - Prints the entire database")`   
`print("'?' - Prints this menu again")`   
`print("'x' - Exits the database")`

## Question #6 [10 Points]: Add to your REPL UI program in `user_interface.py` the ability to save and load a Database object from disc.

**These abilities should be communicated clearly to the user. You may use the `jsonpickle` and `os` libraries to
streamline this process.**