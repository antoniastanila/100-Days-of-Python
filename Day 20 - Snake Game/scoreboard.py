from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.score_position()
        self.write_text()
        self.hideturtle()

    def score_position(self):
        self.goto(0, 250)

    def write_text(self):
        self.write(f"Score: {self.score}", False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False,
                   align=ALIGNMENT, font=FONT)
