from turtle import Turtle
import random
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.x=random.choice([10,-10])
        self.y=random.choice([10,-10])
        self.move_speed=0.1

        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(0,0)
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bounce(self):
        self.y*=-1
    def bounce_paddle(self):
        self.x*=-1
        self.move_speed*=0.9
    def reset_position(self):
        self.goto(0,0)
        self.x*=-1
        self.move_speed=0.1

