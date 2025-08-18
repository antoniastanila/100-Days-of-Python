from turtle import Turtle


class Score(Turtle):
    def __init__(self, alignment, coordinate_x, coordinate_y):
        super().__init__()
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.alignment = alignment
        self.goto(coordinate_x, coordinate_y)

    def increase(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"{self.score}", move=False,
                   align=self.alignment, font=('Arial', 40, 'normal'))
