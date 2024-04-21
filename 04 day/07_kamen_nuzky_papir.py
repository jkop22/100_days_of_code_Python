import random

print("WELCOME TO THE ROCK-PAPER-SCISSORS GAME")

select = ["KAMEN", "NUZKY", "PAPIR"]

ur_turn = int(input("Zadej svou volbu (0-kamen, 1-nuzky, 2-papir): "))

if ur_turn > 2 or ur_turn < 0:
    print("Zadal jsi neplatnou volbu, PROHRALS!")
else:
    ai_turn = random.randint(0,2)

    print(f"Vybral sis {select[ur_turn]}.")
    print(f"Pocitac zahral {select[ai_turn]}.")
    print("------------------------")

    if select[ur_turn] == select[ai_turn]:
        print("REMIZA!")
    elif select[ur_turn] == "KAMEN":
        if select[ai_turn] == "NUZKY":
            print("VYHRAL JSI! :)")
        else:
            print("VYHRAL POCITAC :(")
    elif select[ur_turn] == "PAPIR":
        if select[ai_turn] == "KAMEN":
            print("VYHRAL JSI! :)")
        else:
            print("VYHRAL POCITAC :(")
    elif select[ur_turn] == "NUZKY":
        if select[ai_turn] == "PAPIR":
            print("VYHRAL JSI! :)")
        else:
            print("VYHRAL POCITAC :(")