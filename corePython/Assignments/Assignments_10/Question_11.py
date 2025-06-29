"""
    Write a program to print all numbers which are divisible by m and n in the
    list.
"""
li = [10,2,30,4,5,40]
m = int(input("enter the number:-"))
n = int(input("enter the number:-"))
for i in li:
    if i%m==0 and i%n==0:
        print(i,end=' ')

