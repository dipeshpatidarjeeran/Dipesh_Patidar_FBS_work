"""
    Write a program to find sum of digits using recursion.
"""
def sumOfDigit(n):
    if n==0:
        return 0
    else:
        return n%10+sumOfDigit(n//10)
    
n = int(input("enter the number:-"))
print("sum of digit:-",sumOfDigit(n))