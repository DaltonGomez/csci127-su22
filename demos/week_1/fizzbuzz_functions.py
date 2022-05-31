def isFizzBuzz(n: int) -> bool:
    """Checks if n divisible by 3 and 5"""
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False


def isFizz(n: int) -> bool:
    """Checks if n divisible by 3"""
    return n % 3 == 0


def isBuzz(n: int) -> bool:
    """Checks if n divisible by 5"""
    return n % 5 == 0


def incrementFizzBuzzDict(key: str, fizzBuzzDict: dict) -> None:
    """Add/increment the key in the dictionary"""
    if key not in fizzBuzzDict.keys():
        fizzBuzzDict[key] = 1
    else:
        fizzBuzzDict[key] += 1


def playFizzBuzz(num: int) -> dict:
    """Plays fizz buzz up to n"""
    fizzBuzzDict = {}
    for n in range(1, num):
        if isFizzBuzz(n) is True:
            print(str(n) + "\t fizzBuzz")
            incrementFizzBuzzDict("fizzBuzz", fizzBuzzDict)
        elif isFizz(n) is True:
            print(str(n) + "\t fizz")
            incrementFizzBuzzDict("fizz", fizzBuzzDict)
        elif isBuzz(n) is True:
            print(str(n) + "\t buzz")
            incrementFizzBuzzDict("buzz", fizzBuzzDict)
        else:
            print(str(n) + "\t neither")
            incrementFizzBuzzDict("neither", fizzBuzzDict)
    # print(fizzBuzzDict)
    return fizzBuzzDict


def printResults(num: int, resultsDict: dict) -> None:
    """Print the results of fizz buzz"""
    print("======= Fizz Buzz Results ========")
    print("High Number: " + str(num))
    # print(resultsDict)
    for key in resultsDict.keys():
        print(key + ": " + str(resultsDict[key]) + "\t(" + str(round((resultsDict[key] / num) * 100, 2)) + "%)")


if __name__ == "__main__":
    highNum = input("Give me a number to count to?\n-> ")
    outcomes = playFizzBuzz(int(highNum))
    # print(outcomes)
    printResults(int(highNum), outcomes)
