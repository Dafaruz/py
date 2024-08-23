from tkinter import *

THEME_COLOR = "#375362"


def v_press( ):
    pass

def x_press():
    pass


class TriviaWindow:

    def __init__(self, quiz_data):
        self.score = quiz_data
        self.v_image = None
        self.x_image = None
        self.v_buttons = None
        self.x_buttons = None
        self.txt_input_wind = None
        self.v_press = None
        self.x_press = None
        self.root = Tk()
        self.root.title("Trivia game")
        self.root.config(bg=THEME_COLOR, pady=20, padx=20)
        self.canvas()
        self.buttons()
        self.the_score_txt()

    def canvas(self):

        self.txt_input_wind = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.txt_input_wind.grid(column=0, row=1, columnspan=2)

    def buttons(self):

        self.v_image = PhotoImage(file="images/true.png")
        self.x_image = PhotoImage(file="images/false.png")
        self.v_buttons = Button(image=self.v_image, width=100, height=100, command=v_press, highlightthickness=0)
        self.x_buttons = Button(image=self.x_image, width=100, height=100, command=x_press, highlightthickness=0)
        self.x_buttons.grid(column=0, row=2, )
        self.v_buttons.grid(column=1, row=2, )


    def the_score_txt(self):

        self.score = Label(text=f"your score is: {self.score}", font=("Ariel", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
