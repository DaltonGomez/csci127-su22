myNumbers = []
userInput = input("Give me a number\n ->")
while userInput != "x":
    myNumbers.append(int(userInput))
    userInput = input("Give me a number\n ->")

print(myNumbers)
