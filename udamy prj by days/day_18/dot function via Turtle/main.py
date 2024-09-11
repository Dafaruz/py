import random
import turtle
import colorgram
from turtle import Turtle, Screen
rgb_colors = []
david = Turtle()
colors = colorgram.extract('dots.jpg', 25)
turtle.colormode(255)
david.penup()

for i in range(len(colors)):
    red = colors[i].rgb.r
    green = colors[i].rgb.g
    blue = colors[i].rgb.b
    rgb = (red, green, blue)
    rgb_colors.append(rgb)


def screen_size(x, y):
    turtle.screensize(x, y)
    print(turtle.screensize())
    return turtle.screensize()


def random_colors():
    random_color = random.choice(rgb_colors)
    return random_color


def turtle_position():
    screen_size(200, 200)
    for state in range(0, 10):
        david.goto(0, state*50)
        for _ in range(10):
            david.forward(50)
            david.dot(10, random_colors())


turtle_position()
screen = Screen()
screen.exitonclick()
