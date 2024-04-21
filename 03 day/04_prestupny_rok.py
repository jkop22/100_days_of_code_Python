year = int(input("Zadej zkoumany rok: "))

if year % 4 == 0:    
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Rok {year} JE prestupny")
        else:
            print(f"Rok {year} NENI prestupny")
    else:
        print(f"Rok {year} JE prestupny")
else:
    print(f"Rok {year} NENI prestupny")