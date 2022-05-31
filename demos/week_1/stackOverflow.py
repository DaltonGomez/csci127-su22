def fooOne(x: int) -> None:
    print("foo one: x = " + str(x))
    fooTwo(x + 1)


def fooTwo(x: int) -> None:
    print("foo two: x = " + str(x))
    fooOne(x - 1)


def infiniteLoop(x: int) -> None:
    flipperFlag = False
    while True:
        if flipperFlag is False:
            x = x + 1
            flipperFlag = True
        elif flipperFlag is True:
            x = x - 1
            flipperFlag = False
        print("looping: x = " + str(x))


def infiniteGrowth(x: int) -> None:
    while True:
        x = x * 2
        print("growing: x = " + str(x))


if __name__ == "__main__":
    fooOne(1)
    # infiniteLoop(1)
    # infiniteGrowth(2)
