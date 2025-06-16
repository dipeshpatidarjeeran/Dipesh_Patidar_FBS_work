"""
    write a program to calculate area of triangle and rectangle
"""
length = int(input("enter the Length:-"))
breadth = int(input("enter the breadth:-"))
# calculate area of rectangle
area = length * breadth
print(f"Area of rectangle is {area} .")


b = int(input("enter the base:-"))
h = int(input("enter the height:-"))
# calculate area of triangle 
area = 1/2*(b*h)
print(f"Area of triangle is {area}")