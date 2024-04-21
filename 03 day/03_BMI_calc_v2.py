hmotnost = int(input("Zadej svou hmotnost (v kilogramech): "))
vyska = int(input("Zadej svou vysku (v centimetrech): "))

bmi = round(hmotnost / (vyska / 100) ** 2, 2)

if bmi < 18.5:
    result = "Podvyziva"
elif bmi < 25:
    result = "Zdrava vaha"
elif bmi < 30:
    result = "Nadvaha"
elif bmi < 35:
    result = "Obezita"
else:
    result = "Tezka obezita"

print(f"Tva BMI je {bmi} => {result}.")

