from turtle import Turtle
STARTING_POSITIONS=([350,0],[350,20],[350,-20],[350,40],[350,-40])
MOVE_DISTANCE=10
UP=90
DOWN=270
class paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.segments=[]
        paddle=Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position,0)
    def move_up(self):
        if self.ycor()<260:
            y=self.ycor()+30
            self.goto(self.xcor(),y)

    def move_down(self):
        if self.ycor()>-260:
            y = self.ycor() - 30
            self.goto(self.xcor(), y)










