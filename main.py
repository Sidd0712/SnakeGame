import time
from tkinter import messagebox
from turtle import Screen
from border import Border
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_on:
    screen.update()

    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score = scoreboard.score
        messagebox.showinfo("Crashed!", f"You crashed.\nYour score was {score}.")
        scoreboard.reset()
        snake.reset()
        time.sleep(1)

    # detect collision with its on tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score = scoreboard.score
            messagebox.showinfo("Crashed!", f"You crashed.\nYour score was {score}.")
            scoreboard.reset()
            snake.reset()
            time.sleep(1)

screen.exitonclick()
