from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        # změna velikosti pomocí měřítka (defaultní velikost je 20x20), my tedy budeme mít circle poloviční (10x10)
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)     
        self.penup()
        self.speed("fastest")        
        self.refresh()

    def refresh(self):
        # nechcem food generovat úplně u okraje aby had nekrešnul do zdi, proto těch -30 jednotek
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 240)
        self.goto(rand_x, rand_y)
