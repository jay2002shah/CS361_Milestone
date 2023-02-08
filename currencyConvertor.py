
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox

root = Tk()
root.title('Jay Shah - Currency Conversion')
root.geometry("520x520")

#create tabs
my_book = ttk.Notebook(root)
my_book.pack(pady=5)

#create two frames
currency_frame = Frame(my_book, width=500, height=500)
conversion_frame = Frame(my_book, width=500, height=500)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

my_book.add(currency_frame, text='Currencies')
my_book.add(conversion_frame, text='Convert')

# make it so it disables the screen to change if input not given by the user
my_book.tab(1, state='disabled')

def unlock():
        if not curr_entry.get() or not conversion_entry.get() or not rate_entry.get():
                mbox.showwarning('WARNING', 'Please Enter Inputs in the Field')
        else:
                my_book.tab(1, state='normal')

def lock():
        my_book.tab(1, state='disabled')

def clear():
        pass

main = LabelFrame(currency_frame, text="Currency to Convert")
main.pack(pady=20)
curr_entry = Entry(main, font=("Times New Roman", 30))
curr_entry.pack(pady=10, padx=10)

#Currency frame
conversion = LabelFrame(currency_frame, text = "Conversion")
conversion.pack(pady=20)

#convert to label
conversion_label = Label(conversion, text = "Currency to Convert To")
conversion_label.pack(pady=10)
conversion_entry = Entry(conversion, font=("Times New Roman", 30))
"currencyConvertor.py" 94L, 2684B
