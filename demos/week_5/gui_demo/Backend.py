class Backend:

    def __init__(self):
        self.thisString = ""

    def setString(self, thisString: str) -> None:
        self.thisString = thisString
        print("Setting new string to: " + self.thisString)

    def getString(self) -> str:
        print("Retuning string: " + self.thisString)
        return self.thisString

    def calculateStringLength(self) -> int:
        print("Returning string length: " + str(len(self.thisString)))
        return len(self.thisString)
