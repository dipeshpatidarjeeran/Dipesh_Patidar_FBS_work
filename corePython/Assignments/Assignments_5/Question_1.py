"""
    Write a program to prompt user to enter userid and password. 
    If Id and password is incorrect give him chance to re-enter 
    the credentials. Let him try 3 times. After that program to terminate.
"""
correct_id = "admin"
correct_pass = "asdf@123"

for i in range(1,4):
    Id = input("enter the user Id:-")
    password = input("enter the password:-")
    if Id == correct_id and password == correct_pass:
        print("correct userid and password")
        break
    else:
        print("Incorrect userid and password please re-enter")
        
else:
    print("You have no valid id and password")