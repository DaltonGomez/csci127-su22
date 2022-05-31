def makeDinner():
    print("> make dinner")
    setTable()
    makeCodFennelStew()
    pourWine()


def setTable():
    print("\t> set table")


def makeCodFennelStew():
    print("\t> make cod fennel stew")
    prepareCodInTomatoes()
    cutFennel()
    simmer()


def prepareCodInTomatoes():
    print("\t\t> prepare cod in tomatoes")


def cutFennel():
    print("\t\t> cut fennel")
    watchFennelCuttingVideo()


def watchFennelCuttingVideo():
    print("\t\t\t> watch fennel cutting video")
    sharpenKnife()
    followVideo()


def sharpenKnife():
    print("\t\t\t\t> sharpen knife")
    print("OUCH!" + 3)


def followVideo():
    print("\t\t\t\t> follow video")


def simmer():
    print("\t\t> simmer")


def pourWine():
    print("\t> pour wine")


if __name__ == "__main__":
    makeDinner()
