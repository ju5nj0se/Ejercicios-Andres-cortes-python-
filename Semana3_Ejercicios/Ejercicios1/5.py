celcius = float(input("Grados celcius: "))
fahrenheit = float(33.8)



def calcular(celcius):
    global fahrenheit
    return celcius * fahrenheit

print(calcular(celcius))