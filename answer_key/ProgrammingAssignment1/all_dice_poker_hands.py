from dice_poker import *

if __name__ == "__main__":
    handsWon = {"fiveKind": 0, "fourKind": 0, "fullHouse": 0, "straight": 0, "threeKind": 0,
                "twoPair": 0, "pair": 0, "bust": 0}
    numRolls = 0
    for dieOne in range(1, 7):
        for dieTwo in range(1, 7):
            for dieThree in range(1, 7):
                for dieFour in range(1, 7):
                    for dieFive in range(1, 7):
                        dice = [dieOne, dieTwo, dieThree, dieFour, dieFive]
                        numRolls += 1
                        print(dice)
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
    printResults(numRolls, handsWon)
