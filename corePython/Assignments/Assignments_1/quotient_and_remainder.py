"""
    write a program to find quotient and remainder of two numbers.
"""

num1 = int(input("enter the first number:-"))
num2 = int(input("enter the second number:-"))

# calculate quotient and remainder
quotient = num1//num2
remainder = num1%num2

print(f"Quotient is {quotient} and Remainder is {remainder} .")