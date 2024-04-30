from turtle import Turtle, Screen
import sys
import random
import tkinter as tk

def popup_message(message, screen):
    popup = tk.Tk()
    popup.wm_title("Message") 
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width - popup.winfo_reqwidth()) / 2
    y = (screen_height - popup.winfo_reqheight()) / 2   
    popup.geometry("+%d+%d" % (x, y))
    def close_windows():
        popup.destroy()
        screen.bye()    
    label = tk.Label(popup, text=message, padx=10, pady=10)
    label.pack()
    button = tk.Button(popup, text="OK", command=close_windows)
    button.pack()
    popup.mainloop()

sys.setrecursionlimit(10**8)
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Try to guess", prompt="Who will win this race? Select by the color: ")

names = ["andy", "ben", "cyril", "dan", "eve", "fred", "greg"]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]

for i in range(0, 7):
    names[i] = Turtle()
    names[i].shape("turtle")
    names[i].color(colors[i])
    names[i].teleport(-240, -120 + 40 * i)    

if guess:
    is_race_on = True

while is_race_on:
    for turtle in names:

        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                popup_message("WINNER!", screen)
            else:
                popup_message(f"LOOSER! The {winning_color} was the right guess ...", screen)

        rand_dist = random.randint(0, 10)
        turtle.penup()
        turtle.forward(rand_dist)