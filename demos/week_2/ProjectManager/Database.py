from Employee import Employee
from Job import Job


class Database:

    def __init__(self):
        """Constructor of the database objects"""
        self.employees = {}  # type: dict[str, Employee]
        self.jobs = {}  # type: dict[str, Job]

    def addJob(self, jobCode: str, jobName: str, cost: float, priority: int) -> None:
        """TODO"""
        thisJob = Job(jobCode, jobName, cost, priority)
        self.jobs[jobCode] = thisJob

    def addEmployee(self, employeeID: str, name: str) -> None:
        """TODO"""
        thisEmployee = Employee(employeeID, name)
        self.employees[employeeID] = thisEmployee

    def assignJobToEmployee(self, employeeID: str, jobID: str, responsibility: float):
        """TODO"""
        thisEmployee = self.employees[employeeID]
        thisEmployee.assignEmployeeJob(jobID, responsibility)

    def sortEmployeesJobs(self, employeeID: str):
        """Sorts all the jobs associated to an employee by their priority"""
        thisEmployee = self.employees[employeeID]
        jobsWithPriorities = []
        for jobTuple in thisEmployee.employeeJobs:
            jobCode = jobTuple[0]
            thisJob = self.jobs[jobCode]
            jobPriorityTuple = (thisJob, thisJob.priority)
            jobsWithPriorities.append(jobPriorityTuple)
        jobsWithPriorities.sort(key=lambda x: x[1])
        for jobTuple in jobsWithPriorities:
            jobTuple[0].printJobDetails()
            print("\n")


# TESTING SCRIPT
db = Database()
db.addJob("f", "Install Floors", 800, 3)
db.addJob("r", "Repair Roof", 1000, 1)
db.addJob("p", "Paint House", 200, 5)
db.addEmployee("b", "Bob")
for job in db.jobs.values():
    job.printJobDetails()
for employee in db.employees.values():
    employee.printEmployeeDetails()

print("\n\n\n")

db.assignJobToEmployee("b", "f", 800)
db.assignJobToEmployee("b", "p", 200)
db.assignJobToEmployee("b", "r", 1000)

db.sortEmployeesJobs("b")
