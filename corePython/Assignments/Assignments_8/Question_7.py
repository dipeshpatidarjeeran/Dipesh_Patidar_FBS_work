"""
    Write a program to find sum of digits of a number.
"""
def sum_digit(n):
    sum = 0
    while(n>0):
        digit = n%10
        sum+=digit
        n//=10

    return sum

n = int(input("enter the number:-"))
print("sum of digit:-",sum_digit(n))