"""
    Write a program to find sum of following series using functions :
    b. 1!+ 2! + 3! + 4!+..... + n!
"""

def sum_fact_series(n):
    sum=0
    for i in range(1,n+1):
        fact=1
        for j in range(1,i+1):
            fact*=j
        sum+=fact
    return sum

n = int(input("Enter the number of series:-"))
print("1!+ 2! + 3! + 4!+..... + n! =",sum_fact_series(n))