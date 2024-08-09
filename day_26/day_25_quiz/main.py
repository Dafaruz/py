import pandas
from turtle import Screen
import turtle
from  state_text import StateText


state_list=[]
data = pandas.read_csv("50_states.csv") # enter the csv into the variable in our main
screen = Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
x_coord = 0
y_coord = 0

while len(state_list) < 50:

    flag = "down"
    user_guess = screen.textinput(title="Guess the state ", prompt="what's the name?")
    list_data = data[data["state"].str.lower() == user_guess.lower()]

    

    for state in data["state"].str.lower() == user_guess.lower():

        if state and (user_guess not in state_list):
            x_coord = list_data["x"].values[0]
            y_coord = list_data["y"].values[0]
            state_name = list_data["state"].values[0]
            state_list.append(user_guess)
            temp = StateText(state_name.title(), x_coord, y_coord)
            print(f"you are right there is a {user_guess}")
            flag = "up"

    if flag == "down":
        print(f"the state : {user_guess.title()} is not on the state list ")


screen.exitonclick()
