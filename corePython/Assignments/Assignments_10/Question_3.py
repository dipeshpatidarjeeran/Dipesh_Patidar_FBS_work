"""
    Write a program to find the second largest element in the list.
"""
li = [12,33,43,66,4,68,6]
maxi = li[0]
for i in li:
    if maxi < i:
        second = maxi
        maxi = i

print(f"{li} in Second largest element is:-",second)