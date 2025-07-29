from tkinter import *
from tkinter import messagebox
def saveData():
    Id = entry1.get()
    name = entry2.get()
    dept = entry3.get()
    sal = entry4.get()
    if Id == '' or name == '' or dept == '' or sal == '':
        messagebox.showerror(message="data not selected...")
    else:
        data = f'{Id}, {name}, {dept}, {sal}'
        with open("corePython/Demos/TkinterDemo/emp.txt", "a") as fp:
            fp.write(data+"\n")
            messagebox.showinfo(message="Successfully Emp Data Save")

if __name__ == "__main__":
    window = Tk()
    window.title("Employee Data Save")
    window.geometry("500x600")

    lable = Label(window, text="Enter Employee Details")
    text1 = Label(window, text="Employee Id:")
    text2 = Label(window, text="Employee Name:")
    text3 = Label(window, text="Employee Department:")
    text4 = Label(window, text="Employee Salary:")
    entry1 = Entry(window)
    entry2 = Entry(window)
    entry3 = Entry(window)
    entry4 = Entry(window)
    btn = Button(window, text="submit", command=saveData)

    lable.grid(row=1, column=1, columnspan=2)
    text1.grid(row=2, column=1)
    text2.grid(row=3, column=1)
    text3.grid(row=4, column=1)
    text4.grid(row=5, column=1)
    entry1.grid(row=2, column=2, pady=5)
    entry2.grid(row=3, column=2, pady=5)
    entry3.grid(row=4, column=2, pady=5)
    entry4.grid(row=5, column=2, pady=5)

    btn.grid(row=7, column=1, columnspan=2, pady=5)
    window.mainloop()