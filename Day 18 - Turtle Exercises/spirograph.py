import turtle as t
from utils_colors import random_color

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)

for angle in range(0, 360, 5):
    timmy.setheading(angle)
    timmy.color(random_color())
    timmy.circle(100)

screen = t.Screen()
screen.exitonclick()
