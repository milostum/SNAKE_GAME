from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#     []        {}

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# DIFFICULTY
difficulty = screen.textinput("Chose the difficulty:", "easy or hard")

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

screen.listen()

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if difficulty == "hard":
        # Detect collision with wall.
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            game_is_on = False
            scoreboard.game_over()
    else:
        if snake.head.xcor() > 285:
            snake.head.goto(-285, snake.head.ycor())
        elif snake.head.xcor() < -285:
            snake.head.goto(285, snake.head.ycor())
        elif snake.head.ycor() > 285:
            snake.head.goto(snake.head.xcor(), -285)
        elif snake.head.ycor() < -285:
            snake.head.goto(snake.head.xcor(), 285)

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
