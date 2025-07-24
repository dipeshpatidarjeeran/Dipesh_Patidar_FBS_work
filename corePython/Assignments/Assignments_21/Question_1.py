# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
    # a. Invalid Number: If the user enters a number that is not valid, catch the
        # exception and display an error message.
    # b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
        # "/", catch the exception and display an error message.
    # c. Division by Zero: If the user tries to divide by zero, catch the exception and
        # display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.
class OperatorException(Exception):
    def __init__(self, op):
        self.op = op

    def __str__(self):
        return f'{self.op} operator not valid'
    
try:
    num1 = int(input("enter the first number:-"))
    num2 = int(input("enter the second number:-"))
    op = input("enter the operator(+, -, *, /):-")
    if op not in "+-*/":
        raise OperatorException(op)

except ValueError as e:
    print("ValueError:",e)

except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)

