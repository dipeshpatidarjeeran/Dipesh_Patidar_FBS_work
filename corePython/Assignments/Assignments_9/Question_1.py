"""
    Write a program to find sum of following series using recursive functions:
    i. 1! + 2! + 3! + 4! +..... + n!
    Note : For fact and sum two recursive functions
"""
def factorial(n):
    fact = 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def sum_fact(n):
    if n==0:
        return 0
    else:
        fact = factorial(n)
        return fact + sum_fact(n-1)
    
n = int(input("enter the number of series for factorial:-"))
print(sum_fact(n))