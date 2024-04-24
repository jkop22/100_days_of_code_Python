# scope

enemies = 1

def incr_enem():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")

incr_enem()
print(f"Enemies outside function: {enemies}")

# local

def drink_potion():
    potion_strength = 2
    print(potion_strength)

print(potion_strength)