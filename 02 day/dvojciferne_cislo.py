# user zada dvojciferne cislo a vypise se jejich soucet

num_str = input("Zadej dvojciferne cislo: ")

a = int(num_str[0])
b = int(num_str[-1])
c = a + b

print(str(a) + " + " + str(b) + " = " + str(c))
        