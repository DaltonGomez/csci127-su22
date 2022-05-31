# x = "cow"
# print(int(x))


x = "23"
y = None
try:
    int(x)
except ValueError:
    print("Please give me a number!")
else:
    y = int(x)
print(y)
print(type(y))
