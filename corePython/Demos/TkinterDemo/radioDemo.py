from tkinter import *
from tkinter import messagebox

def submit():
    val1 = x.get()
    val2 = y.get()
    val3 = z.get()
    course = ''
    if val1 == 1:
        course += "python\n"
    if val2 == 1:
        course += "java\n"
    if val3 == 1:
        course += "Testing\n"
    if course:
        messagebox.showinfo(message=course)
    else:
        messagebox.showerror(message="Not select course")

if __name__ == "__main__":
    window = Tk()
    window.title("Radio Button")
    window.geometry("500x600")
    

    x = IntVar()
    y = IntVar()
    z = IntVar()

    text = Label(window, text="Please select course:")
    c1 = Checkbutton(window, text="Python", variable=x)
    c2 = Checkbutton(window, text="Java", variable=y)
    c3 = Checkbutton(window, text="Testing", variable=z)
    btn = Button(window, text="submit", command=submit)

    text.pack()
    c1.pack()
    c2.pack()
    c3.pack()
    btn.pack()
    window.mainloop()