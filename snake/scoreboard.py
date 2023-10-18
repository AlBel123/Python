from turtle import Turtle

ALIGNMENT = "center"
FONT = 'Courier', 24, 'bold'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 255)
        self.color("white")
        self.score = 0
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        # self.clear()
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=('Courier', 40, 'bold'))
