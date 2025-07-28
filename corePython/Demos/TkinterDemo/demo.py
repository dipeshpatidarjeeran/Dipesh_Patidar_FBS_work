from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.geometry("300x400")
    window.title("Demo")
    window.configure(bg="black")
    title = Label(window, text="Hello World!")
    title.pack()
    window.mainloop()