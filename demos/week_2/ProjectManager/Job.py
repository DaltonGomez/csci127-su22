class Job:

    def __init__(self, jobCode: str, jobName: str, cost: float, priority: int):
        """Constructor of Job Object, obviously!"""
        self.jobCode = jobCode
        self.jobName = jobName
        self.cost = cost
        self.priority = priority

    def printJobDetails(self) -> None:
        """Prints attributes of a job object"""
        print("Job Code: " + self.jobCode)
        print("Job Name: " + self.jobName)
        print("Cost: " + str(self.cost))
        print("Priority: " + str(self.priority))
