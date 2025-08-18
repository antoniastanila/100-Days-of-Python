from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.move_distance = STARTING_MOVE_DISTANCE
        self.penup()
        self.setheading(180)
        self.locate_car()

    def locate_car(self):
        random_y = random.randint(-250, 250)
        self.goto(290, random_y)

    def move_car(self):
        self.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
