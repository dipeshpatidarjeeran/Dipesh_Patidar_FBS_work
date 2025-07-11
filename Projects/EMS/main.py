from admin import Admin
ch = 0 
while(ch != '2'):
    print("""Please select choice:
          1. login
          2. exit""")
    ch = input("Enter the choice:")

    if(ch == '1'):
        uid = input("Enter the admin Id:-")
        passw = input("Enter the Password:-")
        if uid == 'admin' and passw == '1234':
            print("logged in  successful...")
            admin = Admin()
        else:
            print("Invalid credentials...")
    elif(ch == '2'):
        print("Thank for chocing us!")
    else:
        print("Invalid choice...Please try again")