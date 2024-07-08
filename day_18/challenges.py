import turtle
from turtle import Turtle , Screen
from random import randint
from tkinter import *
david = Turtle()        # creating an object
david.shape("turtle")   # creating an object shape
turtle.colormode(255)  # define the color to rgb

def rendom_color():
    color=((randint(0 , 255) , randint(0 , 255) , randint(0 , 255)))
    return color


# 1st challenge
# for step in range(4):
#     david.forward(100)
#     david.right(90)
#

# 2nd challenge
# for i in range(20):
#     david.forward(10)
#     david.penup()
#     david.forward(10)
#     david.pendown()
# 3rd challenge

# for movment in range(3,20):
#     david.pencolor((randint(0 , 255) , randint(0 , 255) , randint(0 , 255)))
#     for _ in range(1,(movment+1)):
#         david.forward(100)
#         david.right(360/movment)

# 4th challenge
#
# def where_to_go(angle):
#
#     list_to_do = [david.right(randint(0, angle)*90), david.left(randint(0, angle)*90)]
#     list_to_do[randint(0, 1)]
#
# david.pensize(10)
# while True:
#     david.forward(20)
#     david.pencolor((randint(0 , 255) , randint(0 , 255) , randint(0 , 255)))
#     where_to_go(randint(0,5))

# 5ft challenge
david.speed(0)
circle_rad = 100
def draw_turtle(space):
    for _ in range(360//space):
        david.pencolor(rendom_color())
        david.circle(100)
        david.setheading(david.heading()+space)

draw_turtle(1)






