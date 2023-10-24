import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = turtle.Turtle()
        self.level_number = 1
        self.level.ht()
        self.level.penup()
        self.level.goto(-280, 250)
        self.level.color("black")
        self.level.write(f"Level {self.level_number}", move=False, align="left", font=FONT)

    def update_score(self):
        self.level.clear()
        self.level.write(f"Level {self.level_number}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.level_number += 1
        self.update_score()

    def game_over(self):
        self.level = turtle.Turtle()
        self.level.ht()
        self.level.penup()
        self.level.color("black")
        self.level.write(f"Game Over", move=False, align="center", font=("Courier", 50, "bold"))
