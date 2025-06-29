"""
    Write a program to remove duplicates from the list.
"""
li = [10,60,20,30,10,40,10,20,50,10]
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
            

print(li2)
