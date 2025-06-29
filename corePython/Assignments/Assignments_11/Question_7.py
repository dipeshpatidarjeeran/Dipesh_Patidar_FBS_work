# Python Program to Find the Intersection of Two Lists
li1 = [1,2,5,3,4]
li2 = [3,4,5,6]
li3 = []
for i in li2:
    if i in li1:
        li3.append(i)

print("Find the Intersection of two lists:",li3)