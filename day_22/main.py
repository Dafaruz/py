from turtle import Screen
from block import Block
import time
RIGHT = 270
LEFT = -270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

block_r = Block(RIGHT)
block_l = Block(LEFT)

screen.update()
screen.listen()  # listen for kay stroke

screen.onkey(block_r.up, "Up")
screen.onkey(block_r.down, "Down")
screen.onkey(block_l.up, "Left")
screen.onkey(block_l.down, "Right")

# Verify block creation
for i, block in enumerate(block_r.block_list):
    print(f'Block {i}: {block.pos()}')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()



screen.exitonclick()


