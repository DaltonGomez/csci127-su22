import threading
import time


class ClockUI:

    def __init__(self):
        self.clockThread = None
        self.userInputThread = None
        self.clock = -1

    def startUserInputThreads(self):
        self.clockThread = threading.Thread(target=self.runClock, args=())
        self.clockThread.start()
        self.userInputThread = threading.Thread(target=self.getUserInput, args=())
        self.userInputThread.start()

    def getUserInput(self):
        userInput = input()
        while userInput != "x":
            userInput = input()
        print(self.clock)

    def runClock(self):
        self.clock = 0
        while True:
            minutes, seconds = divmod(self.clock, 60)
            timeFormat = "{:02d}:{:02d}".format(minutes, seconds)
            print(timeFormat, end="\r")
            time.sleep(1)
            self.clock += 1


clockUI = ClockUI()
clockUI.startUserInputThreads()
