from snake import Snake
from food import Food
from turtle import Screen
import time
from scoreboard import ScoreBoard



screen = Screen()
score = ScoreBoard()

def esc():
    print('bye')
    return


def go_again():
    screen.clear()
    score.score=0
    snake_game()



# create a screen object withe size and trigger
# the tracer to 0 So it will need to update when we will trigger A update method


def snake_game():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("snake game")
    screen.tracer(0)
    food = Food()

    snake = Snake()
    flag = 0
    screen.listen()  # listen for kay stroke
    screen.update()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        snake.move()
        if snake.square_list[0].distance(food)<=15:
            score.score_went_up()
            food.refresh()
            snake.snake_eat()
        if snake.square_list[0].xcor() <= -290 or snake.square_list[0].xcor() >= 290 or snake.square_list[0].ycor() >= 290 or snake.square_list[0].ycor() <= - 290:
            score.game_is_over()
            screen.update()
            break

        for square in snake.square_list[len(snake.square_list) : 1 : -1 ]:
            if snake.square_list[0].distance(square) <20:
                flag = 1


        if flag == 1:
            score.game_is_over()
            screen.update()
            break

    while True:
        score.game_is_over()
        screen.update()
        screen.onkey(go_again, "1")
        screen.onkey(esc, "2")


snake_game()
