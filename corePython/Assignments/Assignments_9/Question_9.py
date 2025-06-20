"""
    Write a program to calculate the m to the power n using recursion.
"""
def power(m,n):
    if n==0:
        return 1
    else:
        return m*power(m,n-1)
    
m = int(input("enter the base of power:-"))
n = int(input("enter the power:-"))
print(power(m,n))