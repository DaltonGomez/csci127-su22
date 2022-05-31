from Database import Database


def printMenu() -> None:
    """Prints the REPL UI menu"""
    print("======== REPL UI MENU ========")
    print("'j' - Adds new job")
    print("'e' - Adds new employee")
    print("'r' - Assigns a job and responsibility to an employee")
    print("'p' - Prints a employee's jobs in order of priority")
    print("'?' - Prints this menu again")
    print("'x' - Exits the database")


if __name__ == "__main__":
    print("Hello to the database...")
    db = Database()
    printMenu()
    userInput = input("Give me a command please?\n-> ")
    while userInput != "x":
        if userInput == "j":
            jobCode = input("Job Code?\n-> ")
            jobName = input("Job Name?\n-> ")
            cost = input("Cost?\n-> ")
            priority = input("Priority?\n-> ")
            db.addJob(jobCode, jobName, float(cost), int(priority))
        elif userInput == "e":
            employeeID = input("Employee ID?\n-> ")
            employeeName = input("Employee Name?\n-> ")
            db.addEmployee(employeeID, employeeName)
        elif userInput == "r":
            employeeID = input("Employee ID?\n-> ")
            jobCode = input("Job Code?\n-> ")
            responsibility = input("Responsibility?\n-> ")
            db.assignJobToEmployee(employeeID, jobCode, float(responsibility))
        elif userInput == "p":
            employeeID = input("Employee ID?\n-> ")
            db.sortEmployeesJobs(employeeID)
        elif userInput == "?":
            printMenu()
        else:
            print("Invalid input... Press '?' for menu!")
        userInput = input("Give me a command please?\n-> ")
