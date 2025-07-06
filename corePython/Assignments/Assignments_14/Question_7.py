# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1.difference(s2))
print(s2.difference(s1))
