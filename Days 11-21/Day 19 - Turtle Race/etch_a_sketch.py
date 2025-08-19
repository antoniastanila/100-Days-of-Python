from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def tilt_right():
    new_heading = timmy.heading()
    new_heading += 10
    timmy.setheading(new_heading)


def tilt_left():
    new_heading = timmy.heading()
    new_heading -= 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=tilt_right, key="d")
screen.onkey(fun=tilt_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
