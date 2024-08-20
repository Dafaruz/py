from turtle import Turtle

SPEED = 20
SIZE = 3


class Block:

    def __init__(self, location):
        self.step = SPEED
        self.block_list = []
        self.location = location
        self.block_creation(location)

    def block_creation(self, location):

        print('create blocks start')
        for index in range(-3, SIZE):
            print(index)
            blocks = Turtle("square")
            blocks.color("white")
            blocks.penup()
            blocks.speed('slow')
            blocks.goto(x=location, y=(0 + index*20))
            self.block_list.append(blocks)

    def up(self):
        if self.block_list[len(self.block_list)-1].ycor() <= 280:
            for block in range(len(self.block_list)-1, -1, -1):
                self.block_list[block].seth(90)
                self.block_list[block].fd(SPEED)
        else:
            pass

    def down(self):
        if self.block_list[0].ycor() >= -280:
            for block in range(-1, len(self.block_list)-1):
                self.block_list[block].seth(270)
                self.block_list[block].fd(SPEED)
        else:
            pass