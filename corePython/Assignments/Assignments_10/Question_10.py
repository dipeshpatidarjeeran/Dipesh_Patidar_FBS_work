"""
    Write a program to remove all occurrences of a given element in the list.
"""
li = [1,2,3,4,5,2,3,2,5]
ele = int(input("enter the element to remove:-"))
for i in li:
    if ele == i:
        li.remove(i)

print(f"List after removing all occurrences of {ele}",li)