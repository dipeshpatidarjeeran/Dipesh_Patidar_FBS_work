"""
    Write a program to print all even numbers until n.
"""
n = int(input("enter the number:-"))
for i in range(n):
    if i%2==0:
        print(i)