"""
File: yahtzee.py
Name: TODO
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * None
    TODO - Populate this list if you significantly use a reference
"""
import random


def rollDice() -> list:
    """Simulates a yahtzee roll by returning a list of 5 ints, where numbers are randomly uniformly chosen from [1,6]"""
    roll = []
    for dieNumber in range(5):
        thisDie = random.randint(1, 6)
        roll.append(thisDie)
    return roll


"""
3a) A function `isYahtzee(dice: list) -> bool` that returns `True` if all five dice are the same value and 
`False` otherwise.
"""

# TODO


"""
3b) A function `isHighStraight(dice: list) -> bool` that returns `True` if all five dice can be ordered such that 
they are consecutively ascending and `False` otherwise.
"""

# TODO


"""
3c) A function `isLowStraight(dice: list) -> bool` that returns `True` if four of the five dice can be ordered such 
that they are consecutively ascending and `False` otherwise.
"""

# TODO


"""
3d) A function `isFullHouse(dice: list) -> bool` that returns `True` if three dice are the same value AND two dice 
are the same value and `False` otherwise.
"""

# TODO


"""
3e) A function `isFourKind(dice: list) -> bool` that returns `True` if four dice are the same value and 
`False` otherwise.
"""

# TODO


"""
3f) A function `isThreeKind(dice: list) -> bool` that returns `True` if three dice are the same value and 
`False` otherwise.
"""

# TODO


"""
3g) A function `playYahtzee(numRolls: int) -> dict` that randomly rolls the dice `numRolls` amount of times and 
computes the number of `Yahtzee`, `HighStraight`, `LowStraight`, `FullHouse`, `FourKind`, `ThreeKind`, and 
`NoneOfTheAbove`, earned in that number of rolls. Return a dictionary with keys for the type of roll and values for 
that roll's count (i.e. after zero rolls, the dictionary is `dict = {"Yahtzee" : 0, "HighStraight" : 0, 
"LowStraight" : 0, "FullHouse" : 0, "FourKind" : 0, "ThreeKind" : 0, "NoneOfTheAbove" : 0}`
"""

# TODO


"""
3h) From the returned dictionary, print the total number of rolls, the total number of each type of roll, 
and the percentage of each type of roll.
"""

# TODO


"""
3i) Finally, write a script/main function that prompts the user how many times they'd like to play yahtzee and then
passes the user's input into the `playYahtzee(numRolls: int) -> None` function and then prints the output from 3h.
"""

# TODO

# Use this starting code to test your functions
testRoll = rollDice()
print(testRoll)
