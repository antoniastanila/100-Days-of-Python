from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate_x, coordinate_y, color):
        super().__init__()
        self.shape("square")
        self.goto(coordinate_x, coordinate_y)
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
