import random
from game_data import data
import art
from os import system

def get_item():
    index = random.randint(0, len(data)-1)
    item = data[index]
    del data[index]
    return item

def evaluate(i1,i2,guess):
    if i1["follower_count"] > i2["follower_count"] and guess == "A":
        return True
    elif i1["follower_count"] < i2["follower_count"] and guess == "B":
        return True
    else:
        return False

def game_start():
    item1 = get_item()
    item2 = get_item()

    result = True
    score = 0

    while result is True:    
        system("cls")
        # print(item1["follower_count"], item2["follower_count"]) - for testing only
        print(f"{item1["name"]} is {item1["description"]} from {item1["country"]}")
        print(art.vs)
        print(f"{item2["name"]} is {item2["description"]} from {item2["country"]}")
        guess = input(f"Who has more follwers 'A' or 'B': ")
        result = evaluate(item1, item2, guess)
        if result == True:
            print("Good Guess!")
            score += 1
            item1 = item2
            item2 = get_item()
        else:
            print(f"Bad guess .. game over .. U scored {score} points.")

game_start()