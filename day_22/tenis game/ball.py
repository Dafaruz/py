from turtle import Turtle
from random import randint

SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.setheading(randint(0, 180))

    def movement(self, block_r, block_l, screen):
        self.fd(SPEED)

        if self.ycor() >= 290.0 or self.ycor() <= -290.0:
            self.seth(-self.heading())
            while not (self.ycor() >= 290.0 or self.ycor() <= -290.0):
                self.fd(SPEED)
                screen.update()

        if self.xcor() >= 300:
            self.goto(x=0, y=0)
            return 1

        if self.xcor() <= -300:
            self.goto(x=0, y=0)
            return 0

        if self.xcor() >= 250:
            for index, i_block in enumerate(block_r.block_list):
                if self.distance(i_block) <= 40:
                    self.setheading(180+(-3+index)*-10)
                    while not self.xcor() >= 240:
                        self.fd(SPEED)
                        screen.update()

        if self.xcor() <= -250:
            for index, i_block in enumerate(block_l.block_list):
                if self.distance(i_block) <= 40:
                    self.setheading(0+(-3+index)*-10)
                    while not self.xcor() <= -240:
                        self.fd(SPEED)
                        screen.update()