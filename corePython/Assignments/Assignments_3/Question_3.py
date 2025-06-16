"""
    Write a program to input angles of a triangle and
    check whether triangle is valid or not.
"""

angle1 = int(input("enter first Angle:-"))
angle2 = int(input("enter second Angle:-"))
angle3 = int(input("enter third Angle:-"))

# calculate area of triangle
total = angle1 + angle2 + angle3 
if total == 180:
    print("triangle is valid")
else:
    print("triangle is not valid")