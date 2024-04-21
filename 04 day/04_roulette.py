import random

names_string = input("Zadej jmena vsech stolovniku oddelena carkou: ")
names = names_string.split(", ")

rand_num = random.randint(0, len(names)-1)
# jednodussi rand_person = random.choice(names)

print(f"{names[rand_num]} dneska plati celou utratu. Diky!")