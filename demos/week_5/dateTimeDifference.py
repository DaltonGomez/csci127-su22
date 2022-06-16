from datetime import datetime


def startGame():
    userKeyStroke = input("Press first key to start clock:\n-> ")
    usersInputString = userKeyStroke
    startTime = datetime.now()
    while userKeyStroke != "x":
        userKeyStroke = input("Next key:\n-> ")
        usersInputString += userKeyStroke
    finishTime = datetime.now()
    print("\n\n")
    print(usersInputString)
    print("Start Time: " + str(startTime))
    print("Finish Time: " + str(finishTime))
    timeElapsed = finishTime - startTime
    print("Microseconds Elapsed: " + str(timeElapsed.microseconds))


startGame()
