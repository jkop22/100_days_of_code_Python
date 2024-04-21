print("Welcome to LOVE CALCULATOR <3")
name1 = input("Jak se jmenujes?: ").lower()
name2 = input("Jak se jmenuje tvole laska?: ").lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

true = str(t + r + u + e)

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

love = str(l + o + v + e)

result = int(true + love)

if result < 10 and result > 90:
    print(f"Vase skore je {result}, hodite se k sobe jako Cola a Mentos.")
elif result >= 40 and result <= 50:
    print(f"Vase skore je {result}, pohodovy vztah.")
else:
    print(f"Vase skore je {result}.")