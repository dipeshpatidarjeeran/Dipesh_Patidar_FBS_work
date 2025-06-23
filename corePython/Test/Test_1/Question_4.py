"""
    Calculate the cost of painting the following building’s walls
    (both interior and exterior). You need to accept area and cost
    of both interior and exterior wall.
"""
a = int(input("enter the length:-"))

# interior = 7*a**2
# exterior = 7*a**2
area = (8*a**2)*2 - (2*a**2)/2

print(f"area of interior and exterior wall {area}")