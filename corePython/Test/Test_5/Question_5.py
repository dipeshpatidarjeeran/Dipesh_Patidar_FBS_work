# Python Program to Find the Union of two Lists without
# using set concept.

li1 = [1,2,4,5]
li2 = [2,3,5,6]

for i in li2:
    if i not in li1:
        li1.append(i)

print(li1)