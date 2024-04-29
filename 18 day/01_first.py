from turtle import Turtle, Screen
from random import randint, choice

johny = Turtle()
screen = Screen()

johny.pensize(1)
johny.speed(9)
screen.colormode(255)

# rectangle
# for _ in range(4):
#     johny.forward(100)
#     johny.left(90)

# dashed line 1
# for _ in range(10):
#     johny.forward(10)
#     johny.color("white")
#     johny.forward(10)
#     johny.color("red")

# dashed line 2
# for _ in range(10):
#     johny.forward(10)
#     johny.pu()
#     johny.forward(10)
#     johny.pd()

# 3-10 uhelnik
# for i in range(3,11):
#     johny.pencolor(randint(0, 255), 
#           randint(0, 255), 
#           randint(0, 255))
#     for _ in range(i):
#         johny.forward(100)
#         johny.left(360 / i)

# random walk
# angle = [0, 90, 180, 270]

# for _ in range(150):
#     johny.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     johny.forward(20)
#     johny.setheading(choice(angle))


def spirograph(radius, gap):
    for _ in range(int(360 / gap)):
        johny.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        johny.circle(radius)
        johny.right(gap)

spirograph(90,10)

screen.exitonclick()


