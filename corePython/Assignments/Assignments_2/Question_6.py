"""
    write a program to calculate total salary of employee based on basic, da=10% of basic,
    ta=12% of basic, hra=15% of basic.
"""
bs = int(input("enter the basic salary:-"))
da = 10/100
ta = 12/100
hra = 15/100
total_salary = bs + bs*da + bs*ta + bs*hra

print(f"total salary is {total_salary}")