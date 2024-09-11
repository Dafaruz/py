from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
RANDOM_INDEX = 0
COUNTER = 3
timer_id = None

##----------------------------------- sector to extract the data to csv --------------##
data_frame = pandas.read_csv("data/french_words.csv")  # import the data as a data frame


def v_press():
    global RANDOM_INDEX
    global data_frame

    data_frame = data_frame.drop(index=RANDOM_INDEX)
    card_flip(COUNTER)


def x_press():

    card_flip(COUNTER)


def card_flip(counter):
    global RANDOM_INDEX
    global timer_id

    if counter == COUNTER:
        RANDOM_INDEX = randint(0, len(data_frame.French)-1)     # change the index to some randon int
        card.itemconfig(image, image=card_front_image)
        card.itemconfig(lang, text="French")
        card.itemconfig(word, text=data_frame.French[RANDOM_INDEX])   # crate a word in French for the user to guess

    if counter > 0:                                     # statement to  ensure the counter will run
        timer_id = root.after(1000, card_flip, counter-1)

    else:                         # counter hit 0so we need to flip show the word in english and the title to english
        root.after_cancel(timer_id)
        card.itemconfig(image, image=card_back_image)
        card.itemconfig(lang, text="English")
        card.itemconfig(word, text=data_frame.English[RANDOM_INDEX])





# ---------------------------- GUI section ------------------------------#

root = Tk()  # create a root window
root.title("fr 2 en guess card")
root.config(height=800, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)
# ---------------------------- image sector ------------------------------#
v_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")


#--------------------------- button sector ------------------------------#

v_button = Button(image=v_image, width=100, height=100, command=v_press, padx=100, highlightthickness=0)
x_button = Button(image=x_image, width=100, height=100, command=x_press, padx=100, highlightthickness=0)
v_button.grid(column=1, row=1,)
x_button.grid(column=0, row=1,)

#--------------------------- canvas ------------------------------#

card = Canvas(width=800, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
image = card.create_image(400, 300, image=card_front_image)

width = card.winfo_reqwidth()/2       # get size of canvas element on x /2
height = card.winfo_reqheight()/2       # get size of canvas element on y /2

lang = card.create_text(width, height-150, text="Card GAME", font=("Ariel", 35, "bold"), fill="black", anchor="center")
word = card.create_text(width, height, text=" READY ?", font=("Ariel", 35, "bold"), fill="black", anchor="center")
card.grid(row=0, column=0, columnspan=2)  # columnspan will spread the obj to the desire value


root.mainloop()
