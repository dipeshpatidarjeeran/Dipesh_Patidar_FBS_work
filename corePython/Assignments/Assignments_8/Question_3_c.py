"""
    Write a program to find sum of following series using functions :
    1^1 + 2^2 + 3^3+ ...... n^n
"""

def sum_sq_series(a):
    sum=0
    for i in range(1,a+1):
        sum+=i**i
    return sum

n = int(input("enter the number of series:-"))
print("1^1 + 2^2 + 3^3+ ...... n^n =",sum_sq_series(n))