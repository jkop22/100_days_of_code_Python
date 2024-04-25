############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):       # iteruje se jenom do 19, pravá mez range je otevřená, musim ji přepsat na 21 aby vypis fungoval.
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)        # list je zero-based struktura, proto by zde měl být interval 0-5 pro bugfree funkčnost
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")             # blbá podmínka pro rok 1994. Ani jedné nevyhovuje, proto se nic nestane.
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?")
# if age > 18:                                  # chybí odsazení třetího řídku a přetypování na int v prvním 
# print("You can drive at age {age}.")          # a jako poslední chybí f string v printu aby se vypsiovala hodnota age

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))   # zde porovnávací místo přiřazovacíh operátoru
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)         # musí být taky ve symčce for
#   print(b_list) 

# mutate([1,2,3,5,8,13])


# number = int(input("Which number do you want to check?"))
# if number % 2 = 0:                  # musí být porovnávací operátor (==)
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# year = (input("Which year do you want to check?"))    # chybí pretypovaní na int
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:      # místo or and, místo if dva elify a pryč hranatou závorku
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])