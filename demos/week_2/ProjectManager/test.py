from Employee import Employee
from Job import Job

paintingHouse = Job("paint", "Paint the Smith's House", 1023.75, 2)
print(type(paintingHouse))
paintingHouse.printJobDetails()

bob = Employee("23", "Bob Raymond")
print(bob)
bob.printEmployeeDetails()

# bob.assignEmployeeJob(paintingHouse.jobCode, 1000)
bob.assignEmployeeJob("paint", 1000)
print(bob.employeeJobs)
