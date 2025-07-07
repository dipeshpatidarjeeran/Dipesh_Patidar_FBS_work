# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
s1 = {5,4,23,15,78,65}
li = list(s1)

li.sort()
print(li)

pro1 = li[-1]*li[-2]   # max number
pro2 = li[0]*li[1]     # min number

if pro1 > pro2:
    print(f"Product is {pro1}, pair is {li[-1], li[-2]}")
else:
    print(f"Product is {pro2}, pair is {li[0], li[1]}")
