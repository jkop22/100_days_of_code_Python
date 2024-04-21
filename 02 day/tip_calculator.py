# welcome message

# celkova utrata v dolarech (i se znakem meny - $)

# kolik procent chcem dat dysko? Na vyber 10,12 nebo 15

# kolik lidi jedlo?

# vypocita kolik by mel zaplatit kazdy clovek - vypis opet vcetne $ signu

print("Welcome to the tip calculator.")
total = float(input("Zadej celkovou utratu (i s $ na zacatku): ")[1:])
tip_percent = int(input("Zadej velikost zpropitneho v procentech (10, 12 nebo 15): "))
num_of_persons = int(input("Kolik vás bylo v restauraci: "))

tip_dollars = total * (tip_percent / 100)
total_incl_tip = total + tip_dollars
total_per_person = format(total_incl_tip / num_of_persons, ".2f")

print(f"Kazdy by mel zaplatit ${total_per_person}")