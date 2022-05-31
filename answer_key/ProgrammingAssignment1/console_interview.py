"""
File: console_interview.py
Name: ANSWER KEY
Course: MSU CSCI-127 Joy & Beauty of Data
Date: Summer 2022

References Used:
    * None
"""

"""
1a) Prompt the user to give their first name. Assign their input to a variable, and print the first name back.
Also, print the data type of their first name.
"""

first = input("\nWhat's your first name?\n-> ")
print(first)
print("Data type of 'first':")
print(type(first))

"""
1b) Prompt the user to give their last name. Print back exactly the following, where `first` is the first name
and `last` is the last name: "Your name is `first` `last`!"
"""

last = input("\nWhat's your last name?\n-> ")
print("Your name is " + first + " " + last + "!")

"""
1c) Prompt the user for their age. Print back: 

> "You are `age` years old..."
"""

age = input("\nHow old are you?\n-> ")
print("You are " + age + "years old...")

"""
1d) Multiply (`age` * 365 * 24 * 60 * 60). Print back the following, where `product` is the output of the
multiplication problem. Also, print the data type of `product`.

> "Which means you're at least `product` seconds old..."
"""

product = int(age) * 365 * 24 * 60 * 60
print("Which means you're at least " + str(product) + " seconds old...")
print("Data type of 'product':")
print(type(product))

"""
1e) Ask the user for the value of pi. Then ask the user to give you the radius of any sized circle, and compute
the area of the circle given input pi and radius. Print back the following, as well as the data type of `area`.

> "Given that a circle has radius = `radius` and pi = `pi`, then the circle's area = `area`."
"""

pi = input("\nWhat's the value of pi?\n-> ")
radius = input("Give me the radius of a circle?\n-> ")
area = float(pi) * float(radius) ** 2
print("Given that a circle has radius = " + radius + " and pi = " + pi + ", then the circle's area = " +
      str(area) + ".")
print("Data type of 'area':")
print(type(area))

"""
1f) Ask the user for a one sentence story. Then print the following, where `length` is the total
number of characters, `first` is the first character in the sentence, `second` is the second character, 
and `last` is the last character. Also, print the data types of `length` and `second`.

> "Cool story bro! It's got `length` characters, the first one is a `first`,
> the second one is a `second` and the last one is a `last`."
"""

story = input("Tell me a story?\n-> ")
print("Cool story bro! It's got " + str(len(story)) + " characters, the first one is a `" + story[0] +
      "`, the second one is a `" + story[1] + "` and the last one is a `" + story[-1] + "`.")
