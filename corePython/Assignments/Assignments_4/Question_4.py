"""
    Write a program to print factorial of a number .
"""
n = int(input("enter the number:-"))
fact = 1
for i in range(1, n+1):
    fact *= i

print(f"factorial is {fact}")