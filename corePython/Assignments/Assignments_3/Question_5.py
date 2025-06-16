"""
    Write a program to check whether the triangle is equilateral, isosceles or scalene
triangle.
"""
side1 = int(input("enter the first side:-"))
side2 = int(input("enter the second side:-"))
side3 = int(input("enter the third side:-"))

if side1 == side2 == side3:
    print("The triangle is Equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")