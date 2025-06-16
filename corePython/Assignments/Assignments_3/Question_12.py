"""
    Write a program to check if given 3 digit number is a palindrome or not.
"""
num = int(input("enter the 3 digit number:-"))

var1 = num // 100
var2 = num % 10
if var1 == var2:
    print(f"{num} number is palindrome")
else:
    print("Not palindrome")