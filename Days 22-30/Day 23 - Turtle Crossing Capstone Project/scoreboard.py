from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x_coordinate, y_coordinate)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False,
                   align="left", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False,
                   align="center", font=('Arial', 30, 'bold'))
