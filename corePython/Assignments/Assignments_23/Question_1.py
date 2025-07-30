# 1. Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

from tkinter import *
from tkinter import messagebox

def admin():
    user = userText.get()
    passw = passText.get()

    with open("Projects/LibraryManagementSystem/data/admin.txt", 'r') as fp:
        adData = fp.read()
        adList = adData.split(", ")
    if user == adList[0] and passw == adList[1]:
        messagebox.showinfo(message="successfully login")
    else:
        messagebox.showerror(message="Invalid credentials")

if __name__ == "__main__":
    window = Tk()
    window.title("login")
    window.geometry("400x500")

    userlab = Label(window, text="username:", pady=5)
    passlab = Label(window, text="password:", pady=5)
    userText = Entry(window)
    passText = Entry(window)
    btn = Button(window, text="login", command=admin)

    userlab.grid(row=1, column=1)
    passlab.grid(row=2, column=1)
    userText.grid(row=1, column=2)
    passText.grid(row=2, column=2)
    btn.grid(row=3, column=1, columnspan=2)
    window.mainloop()