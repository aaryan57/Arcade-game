from turtle import Screen
from paddle import paddle
from ball import ball
from scorecard import scorecard

import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
paddle1=paddle(350)
paddle2=paddle(-350)
ball=ball()
score=scorecard()

screen.listen()
screen.onkey(paddle1.move_up, "Up")        # Right paddle moves up with "Up" arrow key
screen.onkey(paddle1.move_down, "Down")    # Right paddle moves down with "Down" arrow key
screen.onkey(paddle2.move_up, "w")         # Left paddle moves up with "w" key
screen.onkey(paddle2.move_down, "s")
game=True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce()
    if ball.distance(paddle1)<50 and ball.xcor()>320 or ball.distance(paddle2)<50 and ball.xcor()<-320:
        # print("made contact")
        ball.bounce_paddle()
    if ball.xcor()>380:
        ball.reset_position()
        score.increase_l()
    if ball.xcor()<-380:
        ball.reset_position()
        score.increase_r()




screen.exitonclick()