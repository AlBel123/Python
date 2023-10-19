from turtle import Turtle, Screen


screen = Screen()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white", "black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 70
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 70
        self.goto(self.xcor(), new_y)
