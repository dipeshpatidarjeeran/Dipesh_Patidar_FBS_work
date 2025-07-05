# Python Program to Sum All the Items in a Dictionary
dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
add = 0
for i in dict1.values():
    add += i

print("sum all the items in a dict",add)