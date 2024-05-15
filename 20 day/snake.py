from turtle import Turtle

DEFAULT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in DEFAULT_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body_piece = Turtle("square")
        body_piece.color("white")
        body_piece.penup()
        body_piece.goto(position)
        self.segments.append(body_piece)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move_snake(self):
        for seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_num - 1].xcor()
            new_y = self.segments[seq_num - 1].ycor()
            self.segments[seq_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)
    
    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)
    
    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)

    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)


