"""
    Write a program to create a duplicate of an existing list. It should not point to
    same list.
"""
li = [1,2,3,4]
copy_li = li.copy()

print("list:",li)
print("copy list:",copy_li)
print("both list not same address")