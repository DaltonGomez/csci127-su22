def countFrequencies(dice: list) -> dict:
    frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in dice:
        frequencies[die] += 1
    return frequencies


testRoll = [1, 1, 2, 2, 1]
print(testRoll)
freq = countFrequencies(testRoll)
print(freq)
