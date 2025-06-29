"""
    Write a program to create a new list from existing list which contains cube of
    each number of list.
"""
li = [1,2,3,4]
li2 = []
for i in li:
    li2.append(i**3)

print("Cube of each numbers of list:-",li2)