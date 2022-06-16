import keyboard

count = 0
while True:
    userInput = keyboard.read_event(suppress=False)

    """print(userInput.name)
    print(type(userInput.name))
    print(userInput.event_type)
    print(type(userInput.event_type))"""

    if userInput.name == "left" and userInput.event_type == "down":
        count += 1
    elif userInput.name == "right" and userInput.event_type == "up":
        print("RIGHT")
    else:
        print("BAD KEY")
