print("Vitejte v La Strada Pizza. Objednavejte:")
size = input("Jak velkou pizzu chceš? (S, M nebo L): ")
more_pepperoni = input("Chces extra feferonky? (Y/N): ")
extra_cheese = input("Chces pridat sejra? (Y/N): ")

total = 0

if size == "S":
    total = 15    
elif size == "M":
    total = 20
else:
    total = 25
   
if extra_cheese == "Y":
    total += 1

if more_pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

print(f"Celkova cena objednavky je ${total}. Thanks")


