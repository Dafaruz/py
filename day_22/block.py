from turtle import Turtle

SPEED = 20
SIZE = 5

class Block (Turtle):

    def __init__(self):
        super().__init__()
        self.step = SPEED
        self.block_list=[]
        self.block_creation()


    def block_creation(self):

        for index in range (0,SIZE):
            blocks = Turtle("square")
            blocks.size(20)
            blocks.color("white")
            blocks.penup()
            blocks.speed('slow')
            blocks.goto(x=-280 , y=(-40 + index*20))
