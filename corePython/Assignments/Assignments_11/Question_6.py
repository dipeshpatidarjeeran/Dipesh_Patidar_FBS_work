# Python Program to Find the Union of two Lists
li1 = [1,2,3,4]
li2 = [3,4,5,6]
for i in li2:
    if i not in li1:
        li1.append(i)

print('find the union of list:',li1)