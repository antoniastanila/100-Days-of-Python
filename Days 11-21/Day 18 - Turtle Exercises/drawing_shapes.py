import random
from turtle import Turtle, Screen

DEGREES = 360

timmy = Turtle()
pen_colors = ["#40E0D0", "#4682B4", "#000080", "#5D3FD3", "#00FFFF", "#4169E1",
              "#088F8F", "#0047AB", "#6082B6", "#CCCCFF", "#9FE2BF"]


def draw_shape(number_of_edges):
    current_angle = DEGREES / number_of_edges
    for _ in range(number_of_edges):
        timmy.forward(100)
        timmy.right(current_angle)


for number_of_edges in range(3, 11):
    timmy.pencolor(random.choice(pen_colors))
    draw_shape(number_of_edges)

screen = Screen()
screen.exitonclick()
