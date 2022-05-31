"""
File: gettin_listy_with_it.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * None
"""
import sys

"""
2a) In the console, take integers from the user indefinitely, appending each number to a previously declared empty 
list. Write the loop such that the input 'x' will break the loop, allowing the program to advance.
"""

myList = []
userInput = input("\nGive a number to add to the list or 'x' to stop adding numbers...\n-> ")
while userInput != "x":
    myList.append(int(userInput))
    userInput = input("Give a number to add to the list or 'x' to stop adding numbers...\n-> ")

"""
2b) Print the list back to the user.
"""

print("\nMy List:")
print(myList)

"""
2c) Print the data type of the list to the user.
"""

print("Data type of 'myList':")
print(type(myList))

"""
2d) Print the length of the list to the user.
"""

length = 0
for number in myList:
    length = length + 1
# OR SIMPLY: length = len(myList)
print("\nList Length:")
print(length)

"""
2e) Print the smallest item in the list to the user. Then print the largest item in the list.
"""

minNum = sys.maxsize
maxNum = -sys.maxsize
for number in myList:
    if number < minNum:
        minNum = number
    if number > maxNum:
        maxNum = number
# OR SIMPLY: minNum = min(myList)
# AND SIMPLY: maxNum = max(myList)
print("\nMin Number:")
print(minNum)
print("\nMax Number:")
print(maxNum)

"""
2f) Print the sum of all the items in the list.
"""

listSum = 0
for number in myList:
    listSum = listSum + number
# OR SIMPLY: listSum = sum(myList)
print("\nList Sum:")
print(minNum)

"""
2g) Print the average of all the items in the list.
"""

listAvg = listSum / length
# OR SIMPLY: listAvg = sum(myList) / len(myList)
print("\nList Avg:")
print(listAvg)

"""
2h) Prompt the user for a number. Check if the number is in the list or not. If it is, print `True`. If it's not, 
print `False`.
"""

checkNum = input("\nGive a number to check if it's in the list...\n-> ")
isPresent = False
for number in myList:
    if number == int(checkNum):
        isPresent = True
# OF SIMPLY: isPresent = checkNum in myList
print(isPresent)

"""
2i) Sort the list, and then print the sorted list.
"""

myList.sort()
print("\nSorted List:")
print(myList)

"""
2j) Check if the values in the sorted list increase one at a time. If every value is one larger than the previous, 
print `True`. Else, print `False`.
"""

isIncreasingByOne = True
for i in range(length - 1):
    if myList[i] + 1 != myList[i + 1]:
        isIncreasingByOne = False
print("\nIs Increasing By One:")
print(isIncreasingByOne)

"""
2k) Declare an empty dictionary, then iterate over your list. For each number, check if the number is already in the 
dictionary as a key. If it is, increment its value by 1. If it is not, add it to the dictionary with a value of 1.
With that, you just counted the frequency of each number in the list! Print the entire dictionary, and print the type 
of the dictionary.
"""

freqDict = {}
for number in myList:
    if number not in freqDict.keys():
        freqDict[number] = 1
    elif number in freqDict.keys():
        freqDict[number] += 1
print("\nFrequency Dict:")
print(freqDict)
print("Data type of 'freqDict':")
print(type(freqDict))
