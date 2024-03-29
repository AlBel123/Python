from turtle import Screen
from snake import Snake
from scoreboard import Score
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
score = Score()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.extend_snake()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # Detect collision with Tail
    # if Head collides with any segment of the Tail :
    # Game_Over
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()


screen.exitonclick()
