import turtle
import math
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=800, height=600)

# Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemy_speed = 2

# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# Bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Move player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Fire bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Check for collision between bullet and enemy
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    # Reverse enemy direction and move down
    if enemy.xcor() > 280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    if enemy.xcor() < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check for collision between bullet and enemy
    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        # Reset the enemy
        enemy.setposition(random.randint(-200, 200), random.randint(100, 250))

    # Check for collision between player and enemy (game over)
    if is_collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

    time.sleep(0.02)

wn.mainloop()
