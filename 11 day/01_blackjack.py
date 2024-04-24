import random
import os

def deal_card():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        score = 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    score = sum(hand)
    return score

def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Loose, computer has BLACKJACK"
    elif player_score == 0:
        return "Win, U have BLACKJACK"
    elif player_score > 21:
        return "Loose, U bust"
    elif computer_score > 21:
        return "Win, computer busted"
    elif player_score > computer_score:
        return "U win"
    else:
        return "Computer win"
    
def play_blackjack():

    player_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computers first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            next_card = input("Do you want to draw another card? Y/N: ")
            if next_card == "Y":
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(compare(player_score, computer_score))
    print(f"You: {player_hand}, {player_score}")
    print(f"Computer: {computer_hand}, {computer_score}")

while input("Do you want to play a game of Blackjack? (Y/N): ") == "Y":
    os.system("cls")
    play_blackjack()