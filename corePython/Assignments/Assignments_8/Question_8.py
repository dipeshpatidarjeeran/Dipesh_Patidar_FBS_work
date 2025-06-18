"""
    Write a program find reverse of a number
"""

def reverse(n):
    rev = 0 
    while(n>0):
        digit = n%10
        rev = rev*10 +digit
        n//=10

    return rev
n = int(input("enter the number:-"))
print("reverse number is:-",reverse(n))