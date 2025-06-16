"""
    Write a program to input all sides of a triangle and check whether triangle is valid or
    not.
"""
# formul = any two sides is greater than the third side.
side1 = int(input("enter the first side:-"))
side2 = int(input("enter the second side:-"))
side3 = int(input("enter the third side:-"))

if(side1+side2)>side3 and (side2+side3)>side1 and (side3+side1)>side2:
    print("triangle is valid")
else:
    print("triangle is not valid") 