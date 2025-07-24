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
        try:
            with open("Projects/EMS/admin.txt", 'r') as fp:
                adData = fp.read()
                adList = adData.split(", ")

        except FileNotFoundError as e:
            ch = '2'
            print("error:",e)

        else:
            if uid == adList[0] and passw == adList[1]:
                print("logged in  successful...")
                admin = Admin()
            else:
                print("Invalid credentials...")
                
    elif(ch == '2'):
        print("Thankyou for Visiting!")
    else:
        print("Invalid choice...Please try again")