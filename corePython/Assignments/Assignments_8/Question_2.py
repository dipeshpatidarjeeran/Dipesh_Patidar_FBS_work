"""
    write a program to calcualte area or circle
"""

def circle(a):
    area = 22/7*a**2
    return area

a = int(input("Enter the redius:-"))
print("Area of circle:-",circle(a))