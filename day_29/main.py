from tkinter import *
from random import choice, shuffle
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
txt = ['', '', '']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    password = ""                # init the password
    for letter in range(0, 6):
        password += choice(letters)

    for symbol in range(0, 3):
        password += choice(symbols)

    for number in range(0, 4):
        password += choice(numbers)

    password_list = list(password)      # concert to list so we can shuffle
    shuffle(password_list)                     # shuffle
    password = ''.join(password_list)         # join from list to string
    password_entry.delete(1, END)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():

    with open("User Data.txt", mode='a') as file:        # notice mode  is appended to add new line

        txt[0] = website_entry.get()
        txt[1] = mail_entry.get()
        txt[2] = password_entry.get()
        print(txt[0])
        if '' in txt:
            popup = Tk()
            popup.minsize(width=300, height=200)
            popup.title(' dont leave it empty you asshole')
            pop_label = Label(popup, text='pls fix it u jackass', font=("Ariel", 15))
            pop_label.pack()
        else:
            file.write(str(f"{txt[0]} | {txt[1]} |{txt[2]} \n"))

# ---------------------------- UI SETUP ------------------------------------------------------------------------ #


window = Tk()   # create the Tk window

window.config(padx=50, pady=50, bg="white")

# _____________________________________canvas sector_____________________________________________________________#

logo_image = PhotoImage(file="logo.png")
logo = Canvas(width=300, height=200, bg="white", highlightthickness=0)
logo.create_image(100, 100, image=logo_image)
logo.grid(column=1, row=0)                  # grid alignment

# _____________________________________ Button sector _____________________________________________________________#

generate = Button(text="Generate password", command=generate_pass)      # create the generate button
generate.grid(column=1, row=4, sticky='e')          # notice the sticky option will stick it to west or est etc

add = Button(text="Add", width=30, command=add_info)      # add to notepad
add.grid(column=1, row=5, sticky="w", pady=5)          # grid alignment

# _____________________________________ Entry sector _____________________________________________________________#


password_entry = Entry(width=30)                    # create the entry pass section
password_entry.grid(column=1, row=4, sticky='w')       # notice the sticky option will stick it to west or est etc

website_entry = Entry(width=50)                     # create the entry website section
website_entry.grid(column=1, row=2)                 # grid alignment

mail_entry = Entry(width=50)                     # create the entry user_name section
mail_entry.grid(column=1, row=3)                   # grid alignment

# _____________________________________label sector_____________________________________________________________#

user_label = Label(text="User name:", font=("Ariel", 15), bg="white")            # create the label  user section
user_label.grid(column=0, row=3)

web_label = Label(text="Website:", font=("Ariel", 15), bg="white")             # create the label website section
web_label.grid(column=0, row=2)                                                 # grid alignment

password_l = Label(text="password:", font=("Ariel", 15), bg="white")          # create the label pass section
password_l.grid(column=0, row=4)                                                # grid alignment


window.mainloop()
