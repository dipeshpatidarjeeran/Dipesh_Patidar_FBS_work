"""
    write a program to input two angles from user and find third angle of the triangle.
"""

angle1 = int(input("enter first Angle:-"))
angle2 = int(input("enter second Angle:-"))

# calculate area of triangle
#angle1 + angle2 + angle3 = 180            
angle3 = 180 - angle1 - angle2              # formul A+B+C=180

print(f"The third angle is {angle3}")