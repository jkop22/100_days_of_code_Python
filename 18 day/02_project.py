from turtle import Turtle, Screen
import random

colors = [(219, 31, 18), (241, 210, 16), (60, 36, 40), (211, 196, 183), (40, 217, 217), (235, 48, 134), (22, 112, 182), (58, 41, 152), (47, 195, 14)]

screen = Screen()
screen.colormode(255)
screen.setup(600, 600)

johny = Turtle()

x_coord = -230
y_coord = -230

gap = 50

for i in range(10):    
    for j in range(10):    
        johny.color(random.choice(colors))
        johny.teleport(x_coord + j * gap, y_coord + i * gap)
        johny.dot(20)











screen.exitonclick()





