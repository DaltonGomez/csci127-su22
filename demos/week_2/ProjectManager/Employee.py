class Employee:

    def __init__(self, employeeID: str, employeeName: str):
        """Constructor of an Employee Object"""
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.employeeJobs = []  # type: list[tuple[str, float]]

    def printEmployeeDetails(self) -> None:
        print("Employee ID: " + self.employeeID)
        print("Employee Name: " + self.employeeName)

    def assignEmployeeJob(self, jobID: str, costResponsible: float) -> None:
        """Assigns a cost the employee is responsible for on a job"""
        thisAssignment = (jobID, costResponsible)
        self.employeeJobs.append(thisAssignment)
