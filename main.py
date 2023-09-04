from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=20)

input_entry = Entry(width=8)
input_entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

text1_label = Label(text="is equal to")
text1_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def button_clicked():
    user_input = float(input_entry.get())
    res = user_input * 1.609344
    miles = round(res)
    output_label.config(text=miles)


calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()

