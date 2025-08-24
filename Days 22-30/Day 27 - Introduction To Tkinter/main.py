from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=100)

window.config(padx=40, pady=40)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(END, string="0")


miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=2, row=0)

equat_to_label = Label(text="is equal to", font=("Arial", 10, "normal"))
equat_to_label.grid(column=0, row=1)

km_result_label = Label(text="Km", font=("Arial", 10, "normal"))
km_result_label.grid(column=2, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)


def calculate():
    miles = float(miles_input.get())
    km_output = str(miles * 1.609)
    km_label.config(text=km_output)


calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()
