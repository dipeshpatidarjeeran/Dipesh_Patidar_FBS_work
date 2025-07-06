# Write a Python program to remove the intersection of a second set with a first set.
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1.difference_update(s2)
print("remove the intersection of second set with a first se:",s1)