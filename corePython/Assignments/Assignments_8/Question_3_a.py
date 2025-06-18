"""
    Write a program to find sum of following series using functions :
    a. 1+ 2 + 3 + 4+..... + n
"""
def sum_series(n):
    sum=0
    for i in range(1,n+1):
        sum+=i

    return sum

n = int(input("Enter the number of series:-"))
print("1+ 2 + 3 + 4+..... + n = ",sum_series(n))