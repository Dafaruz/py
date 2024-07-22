import pandas
from turtle import Screen
import turtle
data = pandas.read_csv("50_states.csv") # enter the csv into the variable in our main

screen = Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


print(data["state"=="Alabama"])
# user_guess=screen.textinput(title="Guess the state ", prompt="what's the name?")

#if data[data["state"==user_guess]]:

screen.exitonclick()
