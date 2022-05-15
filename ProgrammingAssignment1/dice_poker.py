"""
File: dice_poker.py
Name: TODO
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * TODO - Populate this list if you significantly use a reference
"""
import random


def rollDice() -> list:
    """Simulates a dice poker roll by returning a list of 5 ints, where each is randomly uniformly chosen from [1,6]"""
    roll = []
    for dieNumber in range(5):
        thisDie = random.randint(1, 6)
        roll.append(thisDie)
    return roll


"""
Question #3: You have a function above, called `rollDice()`, which returns a list of 5 random ints between 
1 and 6, inclusive. Write a program with the following:

3a) A function `isFiveKind(dice: list) -> bool` that returns `True` if all five dice are the same value and
`False` otherwise.
"""

# TODO


"""
3b) A function `isFourKind(dice: list) -> bool` that returns `True` if four dice are the same value and 
`False` otherwise.
"""

# TODO


"""
3c) A function `isFullHouse(dice: list) -> bool` that returns `True` if three dice are the same value AND two dice 
are the same value and `False` otherwise.
"""

# TODO


"""
3d) A function `isStraight(dice: list) -> bool` that returns `True` if all five dice can be ordered such that 
they are consecutively ascending and `False` otherwise.
"""

# TODO


"""
3e) A function `isThreeKind(dice: list) -> bool` that returns `True` if three dice are the same value and 
`False` otherwise.
"""

# TODO


"""
3f) A function `isTwoPair(dice: list) -> bool` that returns `True` if there are two values that each appear twice and 
`False` otherwise.
"""

# TODO


"""
3g) A function `isPair(dice: list) -> bool` that returns `True` if two dice are the same value and
`False` otherwise.
"""

# TODO


"""
3h) A function `playDicePoker(numRolls: int) -> dict` that rolls the dice `numRolls` amount of times and 
computes the number of `fiveKind`, `fourKind`, `fullHouse`, `straight`, `threeKind`, `twoPair`, `pair` and `bust` 
(i.e. none of the above), earned in that number of rolls. Return a dictionary with keys for the type of roll and 
values for that roll's count (i.e. after zero rolls, the dictionary is `dict = {"fiveKind" : 0, "fourKind" : 0, 
"fullHouse" : 0, "straight" : 0, "threeKind" : 0, "twoPair" : 0, "pair" : 0, "bust" : 0}`). NOTE: Each roll should 
only be counted once. That is to say a `fullHouse` is a just a `fullHouse`, and not also a `threeKind` and `pair`. 
This means the sum of all entries in the dictionary should total to `numRolls`.
"""

# TODO


"""
3i) From the returned dictionary, a function `printResults(results: dict) -> None` that prints the total number
of rolls, the total number of each type of roll, and the percentage observed of each type of roll.

HINT: If you enter a very large `numRolls` into the console (like >10,000), then, by the law of large numbers,
you should see probabilities that very closely match the probability distribution published on: 
https://en.wikipedia.org/wiki/Poker_dice.
"""

# TODO


"""
3j) Finally, write a script/main function that prompts the user how many times they'd like to play dice poker, passes
the user's input into the `playDicePoker(numRolls: int) -> dict` function, and finally passes the returned dictionary
into `printResults(results: dict) -> None`.
"""

# TODO


# Use this starting code to test your functions
testRoll = rollDice()
print(testRoll)
