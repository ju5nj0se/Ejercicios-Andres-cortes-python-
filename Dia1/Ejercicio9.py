año = int (input("Ingrese un año para si es bisiesto: "))
bisiesto = False
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    bisiesto = True
    print(bisiesto)
else:
    print(bisiesto)