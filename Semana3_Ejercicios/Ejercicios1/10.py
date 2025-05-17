cadena = input()



def palindromo(cadena):
    lista1 = []
    for i in cadena:
        lista1.append(i)

    lista2 = list(reversed(lista1))

    cadena2 = "".join(lista2)

    if cadena == cadena2:
        return "es palindromo"
    
    else:
        return "no es palindromo"
    
print(palindromo(cadena))