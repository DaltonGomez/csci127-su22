# Programming Assignment #1

### Instructions:
Please complete the questions/problems described here in each of their respective .py files 
inside this directory. Once completed, submit the individual files of this directory to the Programming Assignment #1
submission box at [Gradescope](https://www.gradescope.com/).

## Question #1 [25 Points]: In the file `console_interview.py`, write lines of code to do the following:

**1a) Prompt the user to give their first name. Assign their input to a variable, and print the first name back. 
Also, print the data type of their first name.**

**1b) Prompt the user to give their last name. Print back exactly the following, where `first` is the first name 
and `last` is the last name:** 

>"Your name is `first` `last`!"

**1c) Prompt the user for their age. Print back:**

>"You are `age` years old..."

**1d) Multiply (`age` * 365 * 24 * 60 * 60). Print back the following, where `product` is the output of the 
multiplication problem. Also, print the data type of `product`.**

>"Which means you're at least `product` seconds old..."

**1e) Ask the user for the value of pi. Then ask the user to give you the radius of any sized circle, and compute 
the area of the circle given input pi and radius. Print back the following, as well as the data type of `area`.**

>"Given that a circle has radius = `radius` and pi = `pi`, then the circle's area = `area`." 

*(Hint: pi = 3.14, area = pi * r^2, and circles are those round things. So if you enter 2 for the radius, 
you should get 12.56 for the area.)*

**1f) Ask the user for a one sentence story. Then print the following, where `size` is the total 
number of characters, `first` is the first character in the sentence, `second` is the second character, and `last` is
the last character. Also, print the data types of `size` and `second`.** 

>"Cool story bro! It's got `size` number of characters, the first one is a `first`, 
> the second one is a `second` and the last one is a `last`.", 

## Question #2 [25 Points]: In the file `gettin_listy_with_it.py`, write lines of code to do the following:

**2a) In the console, take integers from the user indefinitely, appending each number to a previously declared empty 
list. Write the loop such that the input *'x'* will break the loop, allowing the program to advance.**

**2b) Print the list back to the user.**

**2c) Print the data type of the list to the user.**

**2d) Print the length of the list to the user.**

**2e) Print the smallest item in the list to the user. Then print the largest item in the list.**

**2f) Print the sum of all the items in the list.**

**2g) Print the average of all the items in the list.**

**2h) Prompt the user for a new number. Check if the number is in the list or not. If it is, print `True`. If it's not, 
print `False`.** 

**2i) Sort the list, and then print the sorted list.**

**2j) Check if the values in the sorted list increase one at a time. If every value is one larger than the previous, 
print `True`. Else, print `False`.**

**2k) Declare an empty dictionary, then iterate over your list. For each number, check if the number is already in the 
dictionary. If it is, increment its value by 1. If it is not, add it to the dictionary with a value of 1.
With that, you just counted the frequency of each number in the list! Print the entire dictionary, and print the type 
of the dictionary.**

## Question #3 [50 Points]: In the file `yahtzee.py`, you have a function `rollDice()`, which returns a list of 5 random ints between 1 and 6, inclusive. Write a program with the following:

**3a) A function `isYahtzee(dice: list) -> bool` that returns `True` if all five dice are the same value and 
`False` otherwise.**

**3b) A function `isHighStraight(dice: list) -> bool` that returns `True` if all five dice can be ordered such that 
they are consecutively ascending and `False` otherwise.**

**3c) A function `isLowStraight(dice: list) -> bool` that returns `True` if four of the five dice can be ordered such 
that they are consecutively ascending and `False` otherwise.**

**3d) A function `isFullHouse(dice: list) -> bool` that returns `True` if three dice are the same value AND two dice 
are the same value and `False` otherwise.**

**3e) A function `isFourKind(dice: list) -> bool` that returns `True` if four dice are the same value and 
`False` otherwise.**

**3f) A function `isThreeKind(dice: list) -> bool` that returns `True` if three dice are the same value and 
`False` otherwise.**

**3g) A function `playYahtzee(numRolls: int) -> dict` that randomly rolls the dice `numRolls` amount of times and 
computes the number of `yahtzee`, `highStraight`, `lowStraight`, `fullHouse`, `fourKind`, `threeKind`, and 
`noneOfTheAbove`, earned in that number of rolls. Return a dictionary with keys for the type of roll and values for 
that roll's count (i.e. after zero rolls, the dictionary is `dict = {yahtzee : 0, highStraight : 0, 
lowStraight : 0, fullHouse : 0, fourKind : 0, threeKind : 0, noneOfTheAbove : 0}`**

**3h) From the returned dictionary, a function that prints the total number of rolls, the total number of 
each type of roll, and the percentage of each type of roll.**

**3i) Finally, write a script/main function that prompts the user how many times they'd like to play yahtzee and then
passes the user's input into the `playYahtzee(numRolls: int) -> None` function and then prints the output from 3h.**


