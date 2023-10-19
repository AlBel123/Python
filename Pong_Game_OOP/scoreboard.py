from turtle import Turtle

ALIGNMENT = "center"
FONT_1 = 'Courier', 40, 'bold'
FONT_2 = 'Courier', 50, 'bold'


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.ht()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" {self.score}", move=False, align=ALIGNMENT, font=FONT_1)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT_2)