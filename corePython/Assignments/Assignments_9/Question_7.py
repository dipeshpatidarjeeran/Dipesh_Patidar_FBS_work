"""
    Write a program to find sum of digits using recursion.
"""
def sumOfDigit(n,sum=0):
    if n==0:
        return sum
    else:
        return sumOfDigit(n//10,sum + n%10)
    
n = int(input("enter the number:-"))
print("sum of digit:-",sumOfDigit(n))