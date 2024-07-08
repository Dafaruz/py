from turtle import Turtle

STEP = 20


class Snake:

    def __init__(self):
        self.square_list = []
        self.create_snake()

    # create a snake body start with 3 boxes

    def create_snake(self):
        for i in range(0, 3):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.speed('slow')
            new_square.goto(x=(0+i*-20), y=0)
            self.square_list.append(new_square)
        # screen update will show the status when it is triggered

    def snake_eat(self):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.speed('slow')
        new_square.goto(x=self.square_list[len(self.square_list)-1].xcor(), y=self.square_list[len(self.square_list)-1].ycor())
        self.square_list.append(new_square)


######################################################################################################################################################


    def move(self):

        for square in range(len(self.square_list)-1, 0, -1):    # this loop will take care so that each square will go to n-1
            self.square_list[square].goto(self.square_list[square-1].xcor(), self.square_list[square-1].ycor())  # This line will move box number n to n-1 when n is the max number of boxes
        self.square_list[0].fd(STEP)


#################################################################################################################################################
##########                                                          movement                                                #####################
#################################################################################################################################################
    def up(self):

        if self.square_list[0].heading() == 270:
            return
        else:
            self.square_list[0].seth(90)

    def down(self):
        if self.square_list[0].heading() == 90:
            return
        else:
            self.square_list[0].seth(270)

    def left(self):
        if self.square_list[0].heading() == 0:
            return
        else:
            self.square_list[0].seth(180)

    def right(self):
        if self.square_list[0].heading() == 180:
            return
        else:
            self.square_list[0].seth(0)
