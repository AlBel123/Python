import turtle
from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Score


screen = Screen()

screen.title("My Pong")
screen.bgcolor("green")
screen.setup(800, 600)

network = turtle.Turtle()
network.color("white")
network.ht()
network.penup()
network.pencolor("white")
network.pensize(4)
x = 0
y = 400
for n in range(20):
    network.goto(x, y)
    network.pendown()
    y -= 20
    network.goto(x, y)
    network.penup()
    y -= 20
    n += 1

screen.tracer(0)
right_p = Paddle((380, 0))
left_p = Paddle((-390, 0))
ball = Ball()
r_score = Score((150, 220))
l_score = Score((-150, 220))


screen.listen()
screen.onkey(right_p.move_up, "Up")
screen.onkey(right_p.move_down, "Down")
screen.onkey(left_p.move_up, "w")
screen.onkey(left_p.move_down, "s")

game_is_on = True
while game_is_on:

    screen.update()
    ball.move_ball()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()
    elif ball.distance(right_p) < 20 or ball.distance(left_p) < 20:
        ball.bounce_paddle()
    elif (ball.distance(right_p) < 50 and ball.xcor() > 370) or (ball.distance(left_p) < 50 and ball.xcor() < -370):
        ball.bounce_paddle()
    elif ball.xcor() >= 400:
        ball.reset_position()
        l_score.increase_score()
    elif ball.xcor() <= -400:
        ball.reset_position()
        r_score.increase_score()
    elif l_score.score >= 3 or r_score.score >= 3:
        l_score.game_over()
        game_is_on = False


screen.exitonclick()
