"""
    Write a program to calculate area of rectangle
"""
def rectangle(l,b):
    area = l*b
    return area

lenght = int(input("enter the lenght:-"))
breadth = int(input("enter the breadth:-"))
print("Area of rectangle is:-",rectangle(lenght,breadth))