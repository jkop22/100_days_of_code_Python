from turtle import Turtle, Screen

johny = Turtle()
screen = Screen()

screen.listen()

def move():
    johny.forward(20)

screen.onkey(move, "space")

screen.exitonclick()