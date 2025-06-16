"""
    Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18)
"""
person = input("Are you Male person(yes/no):-")

if person == "yes":
    age = int(input("enter your age:-"))
    if age>=21:
        print("your are eligible to marry")
    else:
        print("your are not eligible to marry")
else:
    age = int(input("enter your age:-"))
    if age>=18:
        print("your are eligible to marry")
    else:
        print("your are not eligible to marry")