"""
    Write a program to swap two numbers using third variable.
"""
a = int(input("enter the first number:-"))
b = int(input("enter the second number:-"))

print(f"before swaping value of a is {a}")
print(f"before swaping value of b is {b}")
print()
c = a+b 
a = c-a
b = c-b

print(f"after swaping value of a is {a}")
print(f"after swaping value of b is {b}")