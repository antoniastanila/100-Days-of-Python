from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from middle_line import MiddleLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(coordinate_x=350, coordinate_y=0, color="red")
left_paddle = Paddle(coordinate_x=-350, coordinate_y=0, color="green")
ball = Ball(color="blue")
middle_line = MiddleLine()

right_score = Score("right", coordinate_x=50, coordinate_y=225)
left_score = Score("left", coordinate_x=-50, coordinate_y=225)

screen.listen()

screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

is_game_on = True

while is_game_on:
    right_score.display_score()
    left_score.display_score()
    time.sleep(ball.speed_increase)
    screen.update()
    ball.move()

    if ball.hit_right_wall():
        left_score.increase()
        ball.reset()
        screen.update()
        time.sleep(1.5)

    elif ball.hit_left_wall():
        right_score.increase()
        ball.reset()
        screen.update()
        time.sleep(1.5)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_ball_x()


screen.exitonclick()
