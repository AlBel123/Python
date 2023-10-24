from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # this random function decreases avg 7 times the speed of new cars' appearance:

        random_chance = random.randint(1,7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, (random.randint(-8,9)*25))
            self.cars_list.append(new_car)

    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

