from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()        
        self.count = 0
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.color("white")        
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.count}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ...", align="center", font=("Courier", 15, "normal"))        

    def update(self):
        self.count += 1
        self.clear()
        self.write_score()
        
        
        