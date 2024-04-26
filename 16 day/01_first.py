# OOP basics
# car = CarBlueprint()        třídy se zapisují "PascalCase" způsobem, na rozdíl od názvů funkcí a proměnných

import turtle

johny = turtle.Turtle()         # nový objekt kurzoru
johny.shape("turtle")           # změna kurzoru na želvu :)
johny.color("coral")            # změna barvy kurzoru
johny.forward(100)              # posun kurzoru vpřed o 100 jednotek (nakreslení čáry - trajktorie pohybu)
for _ in range(3):
    johny.left(90)              # otočení vlevo o 90 stupňů
    johny.forward(100)

johnys_screen = turtle.Screen() # canvas pro želvu

johnys_screen.canvheight = 500  # nastavení rozměrů canvasu
johnys_screen.canvwidth = 500

johnys_screen.exitonclick()     # metoda pro nastavení zavření canvasu až po kliknutí myši

