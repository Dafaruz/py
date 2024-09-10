import turtle

# Set up the screen
win = turtle.Screen()
win.title("Breakout Clone")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [250, 225, 200, 175, 150]

for color, y in zip(colors, y_positions):
    for i in range(-350, 400, 70):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(color)
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(i, y)
        bricks.append(brick)

# Score
score = 0

# Pen (for displaying score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Paddle movement functions
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 30
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 30
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        pen.goto(0, 0)
        pen.write("Game Over", align="center", font=("Courier", 36, "normal"))
        break

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 27:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick out of the screen
            bricks.remove(brick)
            score += 1
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Check if all bricks are broken
    if len(bricks) == 0:
        pen.goto(0, 0)
        pen.write("You Win!", align="center", font=("Courier", 36, "normal"))
        break
