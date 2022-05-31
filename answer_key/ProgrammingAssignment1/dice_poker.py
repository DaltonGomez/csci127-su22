"""
File: dice_poker.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * None
"""
import random


def rollDice() -> list:
    """Simulates a dice poker roll by returning a list of 5 ints, where each is randomly uniformly chosen from [1,6]"""
    dice = []
    for dieNumber in range(5):
        thisDie = random.randint(1, 6)
        dice.append(thisDie)
    return dice


def countFrequencies(dice: list) -> dict:
    """Counts the frequencies of each value in a roll"""
    freqDict = {}
    for dieValue in dice:
        if dieValue not in freqDict.keys():
            freqDict[dieValue] = 1
        elif dieValue in freqDict.keys():
            freqDict[dieValue] += 1
    return freqDict


def isFiveKind(dice: list) -> bool:
    """Checks if the dice in a roll are a five of a kind"""
    freqDict = countFrequencies(dice)
    if 5 in freqDict.values():
        return True
    else:
        return False


def isFourKind(dice: list) -> bool:
    """Checks if the dice in a roll are a four of a kind"""
    freqDict = countFrequencies(dice)
    if 4 in freqDict.values():
        return True
    else:
        return False


def isFullHouse(dice: list) -> bool:
    """Checks if the dice in a roll are a full house"""
    freqDict = countFrequencies(dice)
    if 3 in freqDict.values() and 2 in freqDict.values():
        return True
    else:
        return False


def isStraight(dice: list) -> bool:
    """Checks if the dice in a roll are a straight"""
    isIncreasingByOne = True
    dice.sort()
    for i in range(len(dice) - 1):
        if dice[i] + 1 != dice[i + 1]:
            isIncreasingByOne = False
    return isIncreasingByOne


def isThreeKind(dice: list) -> bool:
    """Checks if the dice in a roll are a three of a kind"""
    freqDict = countFrequencies(dice)
    if 3 in freqDict.values():
        return True
    else:
        return False


def isTwoPair(dice: list) -> bool:
    """Checks if the dice in a roll are a two pair"""
    freqDict = countFrequencies(dice)
    firstPair = False
    for count in freqDict.values():
        if count == 2 and firstPair is False:
            firstPair = True
        elif count == 2 and firstPair is True:
            return True
    return False


def isPair(dice: list) -> bool:
    """Checks if the dice in a roll are a pair"""
    freqDict = countFrequencies(dice)
    if 2 in freqDict.values():
        return True
    else:
        return False


def playDicePoker(numRolls: int) -> dict:
    """Rolls the dice 'numRolls' amount of times and scores and counts each roll"""
    handsWon = {"fiveKind": 0, "fourKind": 0, "fullHouse": 0, "straight": 0, "threeKind": 0,
                "twoPair": 0, "pair": 0, "bust": 0}
    for rollNumber in range(numRolls):
        dice = rollDice()
        if isFiveKind(dice) is True:
            handsWon["fiveKind"] += 1
        elif isFourKind(dice) is True:
            handsWon["fourKind"] += 1
        elif isFullHouse(dice) is True:
            handsWon["fullHouse"] += 1
        elif isStraight(dice) is True:
            handsWon["straight"] += 1
        elif isThreeKind(dice) is True:
            handsWon["threeKind"] += 1
        elif isTwoPair(dice) is True:
            handsWon["twoPair"] += 1
        elif isPair(dice) is True:
            handsWon["pair"] += 1
        else:
            handsWon["bust"] += 1
    return handsWon


def printResults(numRolls: int, handsWon: dict) -> None:
    """Prints the results of playing dice poker"""
    print("Total Number of Rolls: " + str(numRolls))
    for hand in handsWon.keys():
        percent = (handsWon[hand] / numRolls) * 100
        print(hand + ": " + str(handsWon[hand]) + "\t(" + str(round(percent, 2)) + "%)")


if __name__ == "__main__":
    rolls = int(input("\nHow many times would you like to play dice poker?\n-> "))
    hands = playDicePoker(rolls)
    printResults(rolls, hands)
