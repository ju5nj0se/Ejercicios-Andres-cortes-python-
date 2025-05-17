entrada = input("Numeros separados por comas: ")
entrada2 = list(map(int, entrada.split(",")))

def devolverPares(entrada2):
    pares = []

    for i in entrada2:
        if i % 2 == 0:
            pares.append(i)

    return pares

print(devolverPares(entrada2))