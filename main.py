from tkinter import *

window = Tk()
window.title("miles to km converter")
window.minsize(height=300, width=500)
window.config(padx=100, pady=100)


def miles_to_km():
    Km = round(float(mile_entry.get()) * 1.6, 2)
    label4.config(text=f"{Km}")


label1 = Label(text="is equal to", font="Arial")
label1.grid(column=0, row=2)

label2 = Label(text="Mile", font="Arial")
label2.grid(column=3, row=0)

label3 = Label(text="KM", font="Arial")
label3.grid(column=3, row=2)

label4 = Label(text="0", font="Arial")
label4.grid(column=2, row=2)

mile_entry = Entry(width=15)
mile_entry.grid(column=2, row=0)

button = Button(text="Calculate", font="Arial", command=miles_to_km)
button.grid(column=2, row=3)





window.mainloop()
