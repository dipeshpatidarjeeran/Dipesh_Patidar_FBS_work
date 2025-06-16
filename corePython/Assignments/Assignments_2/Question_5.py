"""
    write a program to calculate selling price of book based on cost price and discount.
"""
cp = int(input("enter the cost price of book:-"))
disc = int(input("enter the discount:-"))

# calculate selling price
sp = cp*(1-disc/100)

print(f"Selling price is {sp}")