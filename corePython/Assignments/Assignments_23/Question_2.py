# 2. Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.
from tkinter import *
from tkinter import ttk

conversion_rates = {
    "INR": 1.0,        
    "USD": 0.012,       
}

def currency_converter():
    froms = combo_from.get()
    to = combo_to.get()
    amount = text1.get()
    
    converted = float(amount) * (conversion_rates[to] / conversion_rates[froms])
    result.config(text=f"{converted:.2f} {to}")

if __name__ == "__main__":
    window = Tk()
    window.title("Currency Converter")
    window.geometry("400x500")
    lable1 = Label(window, text="amount")
    lable1.grid(row=1, column=1)
    text1 = Entry(window)
    text1.grid(row=1,column=2, pady=5)

    from_box = Label(window, text="froms currency:")
    from_box.grid(row=2,column=1)
    combo_from = ttk.Combobox(window, values=list(conversion_rates.keys()))
    combo_from.grid(row=2,column=2, pady=5)

    to_box = Label(window, text="To currency:")
    to_box.grid(row=3,column=1)
    combo_to = ttk.Combobox(window, values=list(conversion_rates.keys()))
    combo_to.grid(row=3,column=2, pady=5)

    btn = Button(window, text="convert", command=currency_converter).grid(row=4, column=1,columnspan=2, pady=5)
    result = Label(window)
    result.grid(row=5,column=1,columnspan=2, pady=5)
    
    window.mainloop()