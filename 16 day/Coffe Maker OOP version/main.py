from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

def coffee_machine():
    is_on = True
    while is_on:
        choice = my_menu.get_items()
        select = input(f"What would you like ({choice}): ")
        if select == "espresso" or select == "latte" or select == "cappuccino":
            print(f"ingredients check for {select} ...")
            order = my_menu.find_drink(select)
            result = my_coffee_maker.is_resource_sufficient(order)
            if result:
                print(f"Ok, insert coins and pay for the order - (${order.cost}).")
                paid = my_money_machine.make_payment(order.cost)
                if paid:
                    my_coffee_maker.make_coffee(order)
                else:
                    print("Sorry, not enough money. Bye.")
            else:
                print("Sorry not enough ingredients for your order. Call maintenance")   
                sys.exit()             
        elif select == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            coffee_machine()
        elif select == "off":
            print("Shutting down the machine .. Bye")
            is_on = False
    print("Sorry, maintenance in progress ...")
    start = input("Maintenance done? (Y / N): ")
    if start == "Y":
        coffee_machine()
    else:
        sys.exit()        

coffee_machine()