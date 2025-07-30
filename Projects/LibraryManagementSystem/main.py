import time, getpass
from colorama import Fore, Style
from pyfiglet import figlet_format
from librarian import Librarian
from validation_path import path
ch = 0 
banner = figlet_format("L M S", font="slant")
print(Fore.CYAN + Style.BRIGHT + banner + Style.RESET_ALL)
print("📚📖📘 Welcome to Library Management System 📘📖📚")

while(ch != '2'):
    print(Fore.YELLOW + Style.BRIGHT + """📋 Please select choice:
            1. 🔐 login
            2. 🚪exit
        """ + Style.RESET_ALL)
    ch = input("Enter the choice:")

    if(ch == '1'):
        eid = input("Enter the Email Id:-")
        passw = getpass.getpass("Enter the Password:-")
        try:
            with open(path + "admin.txt", 'r') as fp:
                adData = fp.read()
                adList = adData.split(", ")

        except FileNotFoundError as e:
            print("error:",e)

        else:
            if eid == adList[0] and passw == adList[1]:
                print(Fore.GREEN + Style.BRIGHT + "✅ Logout successful..." + Style.RESET_ALL)
                Librarian()
                
            else:
                print(Fore.RED + Style.BRIGHT + "⚠️  Invalid credentials..." + Style.RESET_ALL)
                
    elif(ch == '2'):
        print(Fore.GREEN + Style.BRIGHT + "🎉📚 Thank you for visiting! Have a great day! 🎉📚" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "❌ Invalid choice. Please try again." + Style.RESET_ALL)