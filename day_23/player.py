from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pos = STARTING_POSITION
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed(MOVE_DISTANCE)
        self.seth(UP)

    def Up(self):

        if self.ycor() <= 280:
            self.seth(UP)
            self.fd(MOVE_DISTANCE)
        if self.ycor() >= 290:
            return 1
        else:
            return

    def Down(self):

        if -290 <= self.ycor():
            self.seth(DOWN)
            self.fd(MOVE_DISTANCE)
        if self.ycor() >= 290:
            return 1
        else:
            return
