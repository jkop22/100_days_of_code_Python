import random

print("Welcome to the Guessing Game")
print("Can u guess the numer Im thinking of?")
SECRET = random.randint(1,100)

if (input("Do you want an easy (E) or hard (H) game?: ")) == "E":
    diff = 10
else:
    diff = 5

while True and diff > 0: 
    guess = int(input("Enter your guess: "))
    diff -= 1
    if guess == SECRET:
        print(f"WINNER!")
        break
    elif guess > SECRET:
        print(f"{guess} too HIGH, try again {diff} tries remainig.")
    else:
        print(f"{guess} too LOW, try again {diff} tries remainig.")
print("GAME LOST all tries gone")