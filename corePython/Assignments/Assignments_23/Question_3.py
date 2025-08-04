# Design a basic calculator to perform +,-,/,*
from tkinter import *

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    add = num1 + num2
    output.config(text=f"Addition of {num1} and {num2} is {add}")

def sub():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    add = num1 - num2
    output.config(text=f"Subtraction of {num1} and {num2} is {add}")

def multi():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    add = num1 * num2
    output.config(text=f"Multiplication of {num1} and {num2} is {add}")

def division():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    add = num1 / num2
    output.config(text=f"Division of {num1} and {num2} is {add}")

if __name__ == "__main__":
    window = Tk()
    window.geometry("300x400")
    window.configure(bg="gray")
    window.title("Addition")

    text1 = Label(window, text="Enter num1")
    text2 = Label(window, text="Enter num2")
    entry1 = Entry(window)
    entry2 = Entry(window)
    btn1 = Button(window, text="ADD", command=add)
    btn2 = Button(window, text="sub", command=sub)
    btn3 = Button(window, text="multi", command=multi)
    btn4 = Button(window, text="divi", command=division)
    output = Label(window)

    text1.grid(row=1, column=1)
    text2.grid(row=2, column=1)
    entry1.grid(row=1, column=2)
    entry2.grid(row=2, column=2)
    btn1.grid(row=3, column=1)
    btn2.grid(row=3, column=2)
    btn3.grid(row=4, column=1)
    btn4.grid(row=4, column=2)
    output.grid(row=5, column=1, columnspan=2)
    window.mainloop()