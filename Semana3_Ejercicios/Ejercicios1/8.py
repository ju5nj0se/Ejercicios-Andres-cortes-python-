entrada = input("Ingrese la palabra: ")
letra = input("Letra: ")


def contarLetra(entrada, letra):
    a = 0
    for i in entrada:
        if letra == i:
            a += 1
    return a

print(f"La letra aparece: {contarLetra(entrada, letra)}")