import random
from turtle import  Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtule will win the race? Enter a color: ")
turtle_list = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    print(new_turtle)
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70+(index*30))
    turtle_list.append(new_turtle)


if user_bet:
    race_is_on = True

while race_is_on:
    for i in range(0, 6):
        turtle_list[i].fd(random.randint(0, 10))
        if turtle_list[i].xcor() > 230:
            race_is_on = False
            print(turtle_list[i])
            if user_bet == turtle_list[i].pencolor():
                print(f"you won the {user_bet} tutle beet the crap out of them ")
            else:
                print(f"you lose the winner is: {colors[i]} ")


screen.exitonclick()
