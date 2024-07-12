from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(x=150, y=250)
        self.score_went_up()


    def score_went_up(self):
        self.goto(x=150, y=250)
        self.write(arg=f"your level : {self.score}", move=False, align='center', font=('Arial', 14, 'bold'))
        self.clear()
        self.score += 1
        self.write(arg=f"your level :{self.score}", move=False,  align='center', font=('Arial', 14, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"game over", move=False, align='center', font=('Arial', 14, 'bold'))