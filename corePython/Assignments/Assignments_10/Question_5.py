"""
    Accept a number from user and check if this element is present in the list or
    not. Also tell how many times it is present in the list.
"""
li = [10,20,30,10,40,50,10]
num = int(input("Please enter the element:-"))
count = 0
for i in li:
    if num == i:
        count += 1

if count == 0:
    print(f"{num} is not present in the list")
else:
    print(f"{num} is present in the list")
    print(f"{count} times present in the list")

