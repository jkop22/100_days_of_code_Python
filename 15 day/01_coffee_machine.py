from data import MENU
from data import resources
import sys

def report(res):
    print(f"Water: {res["water"]}")
    print(f"Milk: {res["milk"]}")
    print(f"Coffee: {res["coffee"]}")
    print(f"Money: {res["money"]}")

def ingredients_check(a, b):    
    if "milk" in a["ingredients"]:
        if a["ingredients"]["water"] < b["water"] and a["ingredients"]["coffee"] < b["coffee"] and a["ingredients"]["milk"] < b["milk"]:
            return True
        else:
            return False
    else:
        if a["ingredients"]["water"] < b["water"] and a["ingredients"]["coffee"] < b["coffee"]:
            return True
        else:
            return False   

def payment_process(coffee):
    cost = coffee["cost"]    
    penny = int(input("Insert Pennies: ")) * 0.01
    nickel = int(input("Insert Nickels: ")) * 0.05
    dime = int(input("Insert Dimes: ")) * 0.10
    quarter = int(input("Insert Quarters: ")) * 0.25
    total = penny + nickel + dime + quarter
    if total > cost:
        print(f"Thank you, here is the change back: ${round(total - cost, 2)}")
        return True
    elif total == cost:
        print(f"Thank you.")
        return True
    else:
        return False  

def make_coffee(coffee, cup, ingredients):
    ingredients["water"] -= coffee["ingredients"]["water"]
    ingredients["coffee"] -= coffee["ingredients"]["coffee"]
    ingredients["money"] += coffee["cost"]
    if "milk" in coffee["ingredients"]: 
        ingredients["milk"] -= coffee["ingredients"]["milk"]
    print(f"Here is your cup of {cup}. Enjoy") 
    another = input("Do U want another one? (Y / N)") 
    if another == "Y":
        coffee_machine()
    else:
        print("Your bad, bye ...")            

def coffee_machine():
    is_on = True
    while is_on:
        select = input("What would you like (espresso/latte/cappuccino): ")
        if select == "espresso" or select == "latte" or select == "cappuccino":
            print(f"ingredients check for {select} ...")
            result = ingredients_check(MENU[select], resources)
            if result:
                print(f"Ok, insert coins and pay for the order - (${MENU[select]["cost"]}).")
                paid = payment_process(MENU[select], select)
                if paid:
                    make_coffee(MENU[select], select, resources)
                else:
                    print("Sorry, not enough money. Bye.")
            else:
                print("Sorry not enough ingredients for your order. Call maintenance")   
                sys.exit()             
        elif select == "report":
            report(resources)
            coffee_machine()
        elif select == "off":
            print("Shutting down the machine .. Bye")
            is_on = False
    print("Sorry, maintenance in progress ...")
    start = input("Maintenance done? (Y / N): ")
    if start == "Y":
        coffee_machine()

coffee_machine()