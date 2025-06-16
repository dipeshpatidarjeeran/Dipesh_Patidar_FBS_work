"""
    Write a program to check if user has entered correct userid and password.
"""
Id = input("enter the user Id:-")
password = input("enter the password:-")

correct_id = "admin"
correct_pass = "asdf@123"

if Id == correct_id and password == correct_pass:
    print("correct userid and password")
else:
    print("Incorrect userid and password")