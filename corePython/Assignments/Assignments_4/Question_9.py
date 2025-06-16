"""
    Write a program to print all numbers in a range divisible by a given number.
"""
num = int(input("enter the number:-"))

for i in range(1,50):
    if i%num == 0:
        print(i)