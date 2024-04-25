import random
# 4.1 constansts for difficulty select function
EASY_TRIES = 10
HARD_TRIES = 5
# 3. check function
def check_guess(guess, SECRET, turns):
    if guess > SECRET:
        print(f"{guess} is too HIGH")
        return turns -1
    elif guess < SECRET:
        print(f"{guess} is too LOW")
        return turns -1
    else:
        print("WELL DONE!")

# 4. setting the difficulty function
def set_difficulty():
    level = input("Select game difficulty ('E'asy / 'H'ard): ")
    if level == "E":
        return EASY_TRIES
    else:
        return HARD_TRIES

def game(): # 6. basic game function
    # 1. welcome message and generate a random number to guess
    print("Welcome to the Guessing Game")
    print("Can u guess the numer Im thinking of?")
    SECRET = random.randint(1, 100)
    print(SECRET)
    # 2. players guess
    turns = set_difficulty() # 4.2 difficulty tracking variable    

    guess = 0 # 5.1 global variable needed for the loop below
    while guess != SECRET: # 5. loop for repeating od guessing
        print(f"You have {turns} attempts to guess the secret number.")
        guess = int(input("Whats your guess: "))
        turns = check_guess(guess, SECRET, turns) 
        if turns == 0:
            print(f"Sorry, U LOOSE, secret number was {guess}.")
            return       

game() # 6.1 game() function call