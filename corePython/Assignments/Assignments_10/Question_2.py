"""
    Write a program to find maximum and minimum element in a list.
"""
li = [3,56,32,51,45,22,1]
maxi = li[0]
for i in li:
    if i > maxi:
        maxi = i

print(maxi)
mini = li[0]
for i in li:
    if i < mini:
        mini = i

print(mini)