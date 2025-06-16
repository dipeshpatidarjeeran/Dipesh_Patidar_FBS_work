"""
    write a program to ente P T R and calculate simple interest.
"""
p = int(input("enter the principal:-"))
r = int(input("enter the rate:-"))
t = int(input("enter the time:-"))

# calculate simple interest
simple_interest = (p*r*t)/100

print(f"simple interest is {simple_interest}")
