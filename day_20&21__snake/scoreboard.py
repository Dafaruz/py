from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.score_went_up()
        self.score_list=[]
    def game_is_over(self):
        self.goto(x=0, y=0)
        self.score_list.append(self.score)
        self.write(arg=f"GAME OVER  your score is : {self.score} top score is {max(self.score_list)}", move=False, align='center', font=('Arial', 14, 'bold'))

    def score_went_up(self):
        self.goto(x=0, y=270)
        self.write(arg=f"your score is : {self.score}", move=False, align='center', font=('Arial', 14, 'bold'))
        self.clear()
        self.score += 1
        self.write(arg=f"your score is : {self.score}", move=False,  align='center', font=('Arial', 14, 'bold'))

