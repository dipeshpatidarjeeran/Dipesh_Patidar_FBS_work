# Python Program to Multiply All the Items in a Dictionary
dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
mul = 1
for i in dict1.values():
    mul *= i

print("Multiply all the items in a dict",mul)