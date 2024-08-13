BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
import pandas

def v_press():
    pass

def x_press():
    pass
#----------------------------------- sector to extract the data to csv --------------#
data_frame = pandas.read_csv("data/french_words.csv")  # import the data as a data frame




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

v_button = Button(image=v_image, width=100, height=100, command=v_press,padx=100, highlightthickness=0)
x_button = Button(image=x_image, width=100, height=100, command=x_press,padx=100, highlightthickness=0)
v_button.grid(column=1, row=1,)
x_button.grid(column=0, row=1,)

#--------------------------- canvas ------------------------------#

card = Canvas(width=800, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 300, image=card_front_image)
width = card.winfo_reqwidth()/2
height = card.winfo_reqheight()/2
word = card.create_text(width, height, text="the word", font=("Ariel", 35, "bold"), fill="black", anchor="center")
lang = card.create_text(width, height-150, text="title", font=("Ariel", 35, "bold"), fill="black", anchor="center")
card.grid(row=0, column=0, columnspan=2) # columnspan will spread the obj to the desire value



root.mainloop()
