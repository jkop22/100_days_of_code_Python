# simple console calculator
import os
from art import logo

def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiplicate(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": plus,
    "-": minus,
    "*": multiplicate,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    for key in calculations:
        print(key)

    want_continue = True
    while want_continue:
        operator = input("select math operation from operators above: ")
        num2 = float(input("Enter second number: "))

        result = calculations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        repeat = input(f"Type C if you want to continue with {result}, N to start new calculation or X to quit: ")
        if repeat == "C":
            num1 = result            
        elif repeat == "N":
            want_continue = False
            os.system("cls")
            calculator()
        else:
            print("Goodbye")
            break
      
calculator()