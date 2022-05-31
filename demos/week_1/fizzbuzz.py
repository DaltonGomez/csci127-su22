fizzBuzzDict = {}
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(str(n) + "\t fizzBuzz")
        if "fizzBuzz" not in fizzBuzzDict.keys():
            fizzBuzzDict["fizzBuzz"] = 1
        else:
            fizzBuzzDict["fizzBuzz"] += 1
    elif n % 3 == 0:
        print(str(n) + "\t fizz")
        if "fizz" not in fizzBuzzDict.keys():
            fizzBuzzDict["fizz"] = 1
        else:
            fizzBuzzDict["fizz"] += 1
    elif n % 5 == 0:
        print(str(n) + "\t buzz")
        if "buzz" not in fizzBuzzDict.keys():
            fizzBuzzDict["buzz"] = 1
        else:
            fizzBuzzDict["buzz"] += 1
    else:
        print(str(n) + "\t neither")
        if "neither" not in fizzBuzzDict.keys():
            fizzBuzzDict["neither"] = 1
        else:
            fizzBuzzDict["neither"] += 1
print(fizzBuzzDict)
