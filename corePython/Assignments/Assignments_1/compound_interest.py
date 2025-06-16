"""
    write a program to ente P T R and calculate compound interest.
"""
p = int(input("enter the principal:-"))
r = int(input("enter the rate:-"))
t = int(input("enter the time:-"))
n = int(input("enter the number of times interest:-"))

# calculate compound interest
compound_interest = p*(1+r/n)**(n*t)                      # formula A = P (1 + r/n)^(nt)

print(f"compound interest is {compound_interest} .")