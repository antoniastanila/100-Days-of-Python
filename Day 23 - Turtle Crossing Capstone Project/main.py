import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("#EEDCF8")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(x_coordinate=-250, y_coordinate=250)
screen.listen()

screen.onkey(fun=player.move_up, key="Up")

car_list = []

game_is_on = True
game_loop_num = 0
acceleration_factor = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_loop_num % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    for current_car in car_manager.all_cars:
        if player.distance(current_car) < 20:
            scoreboard.game_over()
            game_is_on = False
            print("lost")

    if player.check_win():
        player.goto(STARTING_POSITION)
        car_manager.level_up()
        scoreboard.score += 1
        scoreboard.update_score()

    game_loop_num += 1

screen.exitonclick()
