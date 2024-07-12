from  turtle import Turtle
from random import randint , choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SIZE = 2
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.y_pos = randint(-250, 250)          # generate THE Y POSITION
        self.x_pos = 310                 # the screen is 300so we won't see the cars until it heds to left cor(180)
        self.paint = (choice(COLORS))    # color to the cars
        self.list = []
        self.create_cars()

    def create_cars(self):
        for index in range(0, 2):
            block = Turtle("square")            # create you instance
            block.penup()
            block.seth(LEFT)
            block.goto(x=(self.x_pos-index*20), y=self.y_pos)
            block.color(self.paint)
            self.list.append(block)

    def move(self, level):
        for index in self.list:
            index.fd(STARTING_MOVE_DISTANCE+level*2)
