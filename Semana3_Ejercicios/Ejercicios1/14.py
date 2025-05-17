lista = list(input("ingrese el texto: ").lower())


def vocales(lista):
    Vocales = [[],[],[],[],[]]

    for i in lista:
        match i:
            case "a":
                Vocales[0].append(i)
            case "e":
                Vocales[1].append(i)
            case "i":
                Vocales[2].append(i)
            case "o":
                Vocales[3].append(i)
            case "u":
                Vocales[4].append(i)

    return Vocales

print(vocales(lista))