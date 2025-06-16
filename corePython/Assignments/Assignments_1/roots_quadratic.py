"""
    Program to Find the Roots of a Quadratic Equation
"""

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

root1 = (-b + ((b**2 - 4*a*c)**0.5))/2*a
root2 = (-b - ((b**2 - 4*a*c)**0.5))/2*a

print("Root 1 =", root1)
print("Root 2 =", root2)