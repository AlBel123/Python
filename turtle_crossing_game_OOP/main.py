import random
import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

car_manager = CarManager()
score = Scoreboard()

should_continue = True
while should_continue:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # detect collision with a car
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            score.game_over()
            should_continue = False
    # detect the finish line achievement
    if player.ycor() == 300:
        score.increase_score()
        player.restart()
        car_manager.level_up()

screen.exitonclick()
