from turtle import Turtle


class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.2, stretch_wid=30)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)

        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
