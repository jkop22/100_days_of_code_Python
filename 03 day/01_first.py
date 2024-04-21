print("Rollercoaster Entrance & Tickets")
height = int(input("Zadej svou vysku v centimetrech: "))
price = 0

if height >= 120:
    age = int(input("Muzes jet. Kolik ti je let: "))
    if age <= 12:
        price = 5
        print("Jsi děcko, velka sleva, listek stoji $5")
    elif age < 18:
        price = 7
        print("Jsi tynejdzr, mensi sleva, listek stoji $7")
    elif age >= 45 and age <= 55:
        price = 0
        print("Mas krizi stredniho veku, listek zdarma.")
    else:
        price = 12
        print("Dospely, plna cena, listek stoji $12")
    photo = input("Chces fotku z jizdy (+$3)? (Y/N): ")
    if photo == "Y":
        price += 3
    print(f"Celkova cena za vstup cini ${price}.")
else:
    print("Sorry, jsi moc malej. Listek nedostanes :(")