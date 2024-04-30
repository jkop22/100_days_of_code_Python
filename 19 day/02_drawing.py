from turtle import Turtle, Screen
import sys

sys.setrecursionlimit(10**8)

johny = Turtle()
screen = Screen()

johny.speed("fast")

screen.listen()

def m_forward():
    johny.forward(1)
    
screen.onkeypress(fun = m_forward, key="w")

def m_backward():
    johny.backward(1)

screen.onkeypress(fun = m_backward, key="s")

def r_left():
    johny.left(1)

screen.onkeypress(fun = r_left, key="a")

def r_right():
    johny.right(1)

screen.onkeypress(fun = r_right, key="d")

def t_reset():
    johny.clear()
    johny.teleport(0, 0)

screen.onkey(fun = t_reset, key="c")

screen.exitonclick()