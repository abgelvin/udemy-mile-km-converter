from tkinter import *


def button_clicked():
    answer = float(value.get())
    result.config(text=round(answer * 1.609, 2))


# Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
value = Entry(width=10)
value.grid(column=1, row=0)

# Labels
miles = Label(text='Miles', font=('calibri', 24))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

equal = Label(text='is equal to', font=('calibri', 24))
equal.grid(column=0, row=2)
equal.config(padx=10, pady=10)

result = Label(text=0, font=('calibri', 24))
result.grid(column=1, row=2)
miles.config(padx=10, pady=10)

km = Label(text='Km', font=('calibri', 24))
km.grid(column=2, row=2)
km.config(padx=10, pady=10)



# Button
button = Button(text='Calcualate', command=button_clicked)
button.grid(column=1, row=3)





window.mainloop()