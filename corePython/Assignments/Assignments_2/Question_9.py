"""
    Write a program to swap two numbers without using third variable.
"""
a = int(input("enter the first number:-"))
b = int(input("enter the second number:-"))

print(f"before swaping value of a is {a}")
print(f"before swaping value of b is {b}")
print()
a,b = b,a

print(f"after swaping value of a is {a}")
print(f"after swaping value of b is {b}")