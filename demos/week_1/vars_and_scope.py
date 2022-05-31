story = "Mountain biking is hard."

isFinished = False
while isFinished is False:
    length = 0
    for char in story:
        thisChar = char
        length += 1
        print(thisChar)
    print(length)
    print(len(story))
    isFinished = True


def squaredAddThree(x: float) -> float:
    """Squares a number and adds three to it,
    returning the input and the output as a tuple"""
    y = x ** 2 + 3
    print((x, y))
    return x


myNum = 12
myOutput = squaredAddThree(myNum)
print(myOutput)
