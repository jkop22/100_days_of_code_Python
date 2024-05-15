from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Project")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.12)
    
    snake.move_snake()
    # detekce kolize s foodem pomocí Turtle metody distance - hlídáme vzdálenost mezi foodem a hlavou hada
    if snake.segments[0].distance(food) < 16:
        food.refresh()
        score.update()
        snake.extend()
    # detekce kolize se zdmi
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_on = False
        score.game_over()
    # detekce kolize s vlastním tělem (pokud hlava zkoliduje s jakýmkoliv dalším segmentem hada)
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            score.game_over()   


        













screen.exitonclick()