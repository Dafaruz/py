##########################################################################
#                       This code is for a json file study               #
#                        day 30 of code via Udamy                        #
#                        by: Daniel Faruz                                #
#                                                                        #
##########################################################################

from tkinter import *
from random import choice, shuffle
import pyperclip
import json
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

txt = ['', '', '']


# ---------------------------- Search DATA ------------------------------- #
def search_data():
    web_name = website_entry.get()
    with open("User Data.json", "r") as json_file:
        j_data = json.load(json_file)
        try:
            messagebox.showinfo(title='User Name AND Password', message=f"""the password :{j_data[web_name]["password"]}
            \n the email: {j_data[web_name]["email"]}""")

        except KeyError:
            messagebox.showinfo(title='User Name AND Password', message=f" no data on this site")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    password = ""                # init the password
    for letter in range(0, 6):          # 6 letters
        password += choice(letters)

    for symbol in range(0, 3):         # 3 symbols
        password += choice(symbols)

    for number in range(0, 4):         # 4 numbers
        password += choice(numbers)

    password_list = list(password)      # concert to list so we can shuffle
    shuffle(password_list)                     # shuffle
    password = ''.join(password_list)         # join from list to string
    password_entry.delete(1, END)      # delete the entry data on the window
    password_entry.insert(0, string=password)     # enter the new string
    pyperclip.copy(password)                       # copy to clipboard the password

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info(js_dict):

    with open("User Data.json", mode='w') as data:

        txt[0] = password_entry.get()
        txt[1] = mail_entry.get()
        txt[2] = website_entry.get()

        # a part for empty info
        if "" in txt:

            popup = Tk()
            popup.minsize(width=300, height=200)
            popup.title(' one or more of the detail is empty pls refill')
            popup.config(bg="white")
            pop_label = Label(popup, text='pls fix it u jackass', font=("Ariel", 15))
            pop_label.pack()
            json.dump(js_dict, data, indent=4)
            return

        else:

                js_dict[str(website_entry.get())] = {"password": password_entry.get(), "email": mail_entry.get()}
                json.dump(js_dict, data, indent=4)   # if statement won't do  we will dump the info

# ---------------------------- UI SETUP ------------------------------------------------------------------------ #


try:              # will try to load data if the file is not there we init the dict
    with open("User Data.json", mode='r') as json_data:     # notice mode  is appended to add new line
        dict_j = json.load(json_data)
except (FileNotFoundError, json.JSONDecodeError):
    dict_j = {}       # init the json file


window = Tk()  # create the Tk window

window.config(padx=50, pady=50, bg="white")

# _____________________________________canvas sector_____________________________________________________________#

logo_image = PhotoImage(file="logo.png")
logo = Canvas(width=300, height=200, bg="white", highlightthickness=0)
logo.create_image(100, 100, image=logo_image)
logo.grid(column=1, row=0)                  # grid alignment

# _____________________________________ Button sector _____________________________________________________________#

generate = Button(text="Generate password", command=generate_pass)      # create the generate button
generate.grid(column=1, row=4, sticky='e')          # notice the sticky option will stick it to west or est etc

add = Button(text="Add", width=40, command=lambda: add_info(dict_j))      # add to notepad
add.grid(column=1, row=5, pady=5)          # grid alignment

website_b = Button(text="Search", command=search_data)
website_b.grid(column=1, row=2, sticky='e')

# _____________________________________ Entry sector _____________________________________________________________#


password_entry = Entry(width=30)                    # create the entry pass section
password_entry.grid(column=1, row=4, sticky='w')       # notice the sticky option will stick it to west or est etc

website_entry = Entry(width=40)                     # create the entry website section
website_entry.grid(column=1, row=2, sticky='w')                 # grid alignment

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
