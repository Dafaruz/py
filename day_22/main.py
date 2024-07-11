from turtle import Screen
from block import Block
from ball import Ball
import time
from  score_board import  ScoreBoard

RIGHT = 270
LEFT = -270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

block_r = Block(RIGHT)
block_l = Block(LEFT)
ball = Ball()

score_l = ScoreBoard(LEFT/2)
score_r = ScoreBoard(RIGHT/2)
screen.update()
screen.listen()  # listen for kay stroke


screen.onkey(block_r.up, "Up")
screen.onkey(block_r.down, "Down")
screen.onkey(block_l.up, "w")
screen.onkey(block_l.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    location = ball.movement(block_r, block_l, screen)
    if location == 1:
        score_l.score_went_up(LEFT/2)

    if location == 0:
        score_r.score_went_up(RIGHT/2)

screen.exitonclick()
