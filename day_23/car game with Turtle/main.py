import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


level = 0
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

index = 0  # resolve the distance between cars

score = ScoreBoard()

screen.listen()  # listen for kay stroke
screen.onkey(player.Up, "Up")
screen.onkey(player.Down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if index == 0:
        cars.append(CarManager())  # create a list of cars
    for i in cars:
        i.move(level)
        if i.list[0].distance(player) <= 20:
            print('you lose')
            game_is_on = False
            break

    if player.ycor() >= 290:
        level += 1
        player.goto(player.pos)
        score.score_went_up()


    index += 1
    index = index % 10  # will set to 0 when it goes up to 10


score.game_over()
screen.update()
screen.exitonclick()