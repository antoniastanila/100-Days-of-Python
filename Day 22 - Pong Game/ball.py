from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(color)
        self.y_increment = 10
        self.x_increment = 10
        self.speed_increase = 0.1
        self.player_turn = "right"

    def move(self):
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)

    def reset(self):
        self.home()
        if self.player_turn == "right":
            self.player_turn = "left"
            self.x_increment = -10
        else:
            self.player_turn = "right"
            self.x_increment = 10

        self.y_increment = 10
        self.speed_increase = 0.1

    def hit_right_wall(self):
        return self.xcor() > 380

    def hit_left_wall(self):
        return self.xcor() < -390

    def bounce_ball_y(self):
        self.y_increment *= -1

    def bounce_ball_x(self):
        self.x_increment *= -1
        self.speed_increase *= 0.7
