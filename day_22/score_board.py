from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, location):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=location, y=250)
        self.score_went_up(location)
        self.score_list = []

    def score_went_up(self, location):
        self.goto(x=location, y=250)
        self.write(arg=f"{self.score}", move=False, align='center', font=('Arial', 20, 'bold'))
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", move=False,  align='center', font=('Arial', 20, 'bold'))
