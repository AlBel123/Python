from turtle import Turtle

ALIGNMENT = "center"
FONT = 'Courier', 24, 'bold'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.hi_score = int(file.read())
        self.goto(0, 255)
        self.color("white")
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score is {self.hi_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):

        if self.score == self.hi_score:
            self.hi_score += 1
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score == self.hi_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.hi_score}")
        self.score = 0
        self.update_scoreboard()

