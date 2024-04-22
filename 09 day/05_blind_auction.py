import os
from art import logo

print(logo)

auction_participants = []

def add_bid(b_name, b_offer):
    new_entry = {}
    new_entry["name"] = b_name
    new_entry["offer"] = b_offer
    auction_participants.append(new_entry)

new_bid = True

while new_bid:
    name = input("Enter your name: ")
    offer = int(input("Enter your bid offer: $"))
    add_bid(name, offer)
    repete = input("Is there another bidder? (Y / N):")
    os.system("cls")
    if repete == "N":
        new_bid = False
    
max = 0

for i in range(len(auction_participants)):
    if auction_participants[i]["offer"] > max:
        max = auction_participants[i]["offer"]
           
print(f"Auction winner is {auction_participants[i]["name"]} with a bid of {auction_participants[i]["offer"]}.")

    

    