from tkinter import *

def convert():
    try:  # handles if user types letters instead of numbers
        amount = float(entry_amount.get())
        currency = currency_var.get()
        if currency == "USD":
            result = amount * 0.012
            label_result.config(text=result)
        elif currency == "EUR":
            result = amount * 0.011
            label_result.config(text=result)
        elif currency == "JPY":
            result = amount * 1.64
            label_result.config(text=result)
    except:
        label_result.config(text="Enter a number!")  # no crashing

# GUI setup
root = Tk()
root.title("Currency Converter")

Label(root, text="Amount in INR:").pack()
entry_amount = Entry(root)
entry_amount.pack()

currency_var = StringVar()
currency_var.set("USD")
OptionMenu(root, currency_var, "USD", "EUR", "JPY").pack()

Button(root, text="Convert", command=convert).pack()

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
