"""
    Write a program to accept distance in km and convert it into
    meters and centimeters both.
"""
dis = float(input("Enter the distance in km:-"))


m = dis * 1000

c = m * 100


print(f"{dis} km distance convert into {m} meter and {c} centimeters.")
