import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which turtle will win the race?")

X_AXIS_START_POSITION = -230
X_AXIS_END_POSITION = 230

is_race_on = False


def place_turtle(turtle, y_axis):
    turtle.goto(X_AXIS_START_POSITION, y_axis)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_axis = -125
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtles.append(turtle)
    place_turtle(turtle, y_axis)
    y_axis += 50

print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > X_AXIS_END_POSITION:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
