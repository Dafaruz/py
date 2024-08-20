from turtle import Turtle

FONT = ("Courier", 24, "normal")


class StateText (Turtle):

    def __init__(self,user_guess, x_cord, y_cord):
        super().__init__()
        self.guess = user_guess
        self.hideturtle()
        self.color('black')
        self.penup()
        self.user_geuss_right(x_cord,y_cord)


    def user_geuss_right (self,x_cord,y_cord):
        self.goto(x=x_cord, y=y_cord)
        self.write(arg=self.guess, move=False, align='center', font=('Arial', 14, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"game over", move=False, align='center', font=('Arial', 14, 'bold'))