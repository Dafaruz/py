from tkinter import *

THEME_COLOR = "#375362"








# def chck_answer(**kwargs):
#     print(kwargs["value"])
#     #user_answer = kwargs["value"]


class TriviaWindow:
    def __init__(self, quiz_data):
        self.score_label = None
        self. other_class = quiz_data
        self.txt_data = None
        self.score = int(quiz_data.score)
        self.v_image = None
        self.x_image = None
        self.v_buttons = None
        self.x_buttons = None
        self.txt_input_wind = None
        self.root = Tk()
        self.root.title("Trivia game")
        self.root.config(bg=THEME_COLOR, pady=40, padx=20)
        self.canvas(quiz_data)
        self.buttons()
        self.the_score_txt()


    def canvas(self,quiz_data):

        self.txt_input_wind = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.txt_data = self.txt_input_wind.create_text(150, 200, text=f"{quiz_data.current_question.text}\n\n" , fill=THEME_COLOR, font=("Arial", 15), width=280, anchor='center')
        self.txt_input_wind.grid(column=0, row=1, columnspan=2)

    def buttons(self):

        self.v_image = PhotoImage(file="images/true.png")
        self.x_image = PhotoImage(file="images/false.png")

        self.v_buttons = Button(image=self.v_image, width=100, height=100, command=self.v_press, highlightthickness=0)
        self.x_buttons = Button(image=self.x_image, width=100, height=100, command=self.x_press, highlightthickness=0)

        self.x_buttons.grid(column=0, row=2, sticky="w" )
        self.v_buttons.grid(column=1, row=2, sticky="e" )

    def the_score_txt(self):

        self.score_label = Label(text=f"your score is: {self.score}", font=("Ariel", 15, "bold"), bg=THEME_COLOR, fg="white", pady=20)
        self.score_label.grid(column=1, row=0)

    def v_press(self):
        if self.other_class.check_answer("True"):
            self.score += 1
            self.the_score_txt()
        text = self.other_class.next_question()
        self.txt_input_wind.itemconfig(self.txt_data, text=f"{text}\n\n\n\n")

    def x_press(self):
        if self.other_class.check_answer("False"):
            
            self.score += 1
            self.the_score_txt()
        text = self.other_class.next_question()
        self.txt_input_wind.itemconfig(self.txt_data, text=f"{text}\n\n\n\n")
