import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()

screen.onkey(fun=player.move_up, key="Up")

car_list = []

game_is_on = True
game_loop_num = 0

while game_is_on:
    if game_loop_num % 6 == 0:
        car = CarManager()
        car_list.append(car)
    for current_car in car_list:
        current_car.move_car()
        if player.distance(current_car) < 20:
            game_is_on = False
            print("lost")

    if player.check_win():
        player.goto(STARTING_POSITION)

    time.sleep(0.1)
    screen.update()
    game_loop_num += 1

screen.exitonclick()
