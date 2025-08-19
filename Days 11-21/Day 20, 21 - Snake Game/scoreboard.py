from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_hs()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.score_position()
        self.update_score()
        self.hideturtle()

    def score_position(self):
        self.goto(0, 250)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_hs(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        self.read_hs()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False,
    #                align=ALIGNMENT, font=FONT)
