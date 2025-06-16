"""
    Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)
"""
import random
cap = random.randint(1111,9999)

Id = input("enter the user Id:-")
password = input("enter the password:-")

correct_id = "admin"
correct_pass = "asdf@123"

if Id == correct_id and password == correct_pass:
    print("correct userid and password")
    cap_code = int(input(f"Please enter the same captcha({cap}):-"))
    if cap == cap_code:
        print("success.")
    else:
        print("failed.")
else:
    print("Incorrect userid and password")