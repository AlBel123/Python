from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-260, 250), random.randint(-260, 250))
