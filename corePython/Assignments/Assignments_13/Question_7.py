# Python Program to Remove the Given Key from a Dictionary
dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
key = int(input(f"which key remove in the dict{dict1}:-"))
dict1.pop(key)

print(f"after deleting key dict is{dict1}")