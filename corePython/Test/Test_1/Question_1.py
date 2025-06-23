"""
    Write a program to find the area and perimeter of following
    figure (Accept the length, breadth and radius from user:
"""
l = int(input("Enter the length:-"))
r = int(input("Enter the radius:-"))
b = r*2
# calculate  area of triangle
triangle = l*b

# calculate half area of circule
circule = 0.5*(22/7*r**2)           # a = 22/7*r**2
total_area = triangle + circule

print(f"Calculate total area is {total_area}")

