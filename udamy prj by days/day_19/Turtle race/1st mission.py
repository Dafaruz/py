from turtle import Screen, Turtle

tur = Turtle()
screen = Screen()


def move_fd():
    tur.fd(10)


def move_bd():
    tur.bk(10)


def move_rt():
    tur.rt(10)


def move_lt():
    tur.lt(10)


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bd)
screen.onkey(key="a", fun=move_lt)
screen.onkey(key="d", fun=move_rt)


screen.exitonclick()
