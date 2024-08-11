from tkinter import *


def button_clicked():
    user_input = input.get()
    km=float(user_input)*1.65
    my_label_solve.config(text=km)

window = Tk()                   # crate an object from the tk class
window.title("Miles to Km")
window.config(padx=10, pady=10)       # create contour surrounding  the window

#Label mil
my_label_mil = Label(text="enter the units in miles")
my_label_mil.grid(column=0, row=0)
my_label_mil.config(padx=20, pady=20)

#Label km
my_label_km = Label(text="the distance in km is : ")
my_label_km.grid(column=0, row=2)
my_label_km.config(padx=20, pady=20)

# km
my_label_solve = Label(text="0")
my_label_solve.grid(column=1, row=2)
my_label_solve.config(padx=20, pady=20)

#Entry
input = Entry(width=20)
    # will fetch the value
input.grid(column=1, row=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)













window.mainloop()
