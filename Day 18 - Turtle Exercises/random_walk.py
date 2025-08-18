import random
from utils_colors import random_color
import turtle as t

directions = [0, 90, 180, 270]
t.colormode(255)
timmy = t.Turtle()
timmy.speed("fast")
timmy.pensize(8)

screen = t.Screen()


for _ in range(100):
    dir = random.choice(directions)
    timmy.pencolor(random_color())
    timmy.setheading(random.choice(directions))

    timmy.forward(50)

screen.exitonclick()
