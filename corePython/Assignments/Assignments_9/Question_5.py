"""
    Write a program to find factorial using recursion.
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter the number:-"))
print("factorial:-",factorial(n))