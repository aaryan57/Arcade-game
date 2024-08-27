from turtle import Turtle
class scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1=0
        self.score2=0
        self.color("white")

        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score
        self.goto(-100, 260)
        self.write(f"{self.score1}", align="center", font=("Arial", 24, "normal"))

        self.goto(100, 260)
        self.write(f"{self.score2}", align="center", font=("Arial", 24, "normal"))

    def increase_l(self):
        self.score1 += 1
        self.clear()
        self.update_score()

    def increase_r(self):
        self.score2 += 1
        self.clear()
        self.update_score()

