from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        with open("score.txt", mode="r") as file:
            self.h_score=file.read()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} max : {self.h_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        with open("score.txt", mode="r") as file:
            f_score = file.read()
        if self.score >= int(f_score):
            self.h_score = self.score
            self.score = 0
            self.write_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def write_score(self,):
        with open("score.txt", mode="w") as file:
            file.write(str(self.h_score))

            self.update_scoreboard()