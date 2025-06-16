"""
    write a program to calculate area and circumference of circle.
"""
r = int(input("enter the radius of the circle:-"))

# calculate area of circle
area = 22/7*r**2                             # formul A = πr2

# calculate circumference of circle
c = 2*22/7*r                                 # formul C = 2πr

print(f"Area of circle is {area} and circumference of circle is {c} .")