año = int(input("Año: "))

if año % 100 == 0:
    if  año % 400 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
        #exit()

elif año % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")

