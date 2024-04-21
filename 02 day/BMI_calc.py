hmotnost = int(input("Zadej svou hmotnost (v kilogramech): "))
vyska = int(input("Zadej svou vysku (v centimetrech): "))

bmi = round(hmotnost / (vyska / 100) ** 2, 2)

print(f"Tva BMI je {bmi}.")

