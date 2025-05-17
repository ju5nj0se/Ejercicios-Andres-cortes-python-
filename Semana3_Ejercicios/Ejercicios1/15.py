cadena = input()

def invertir(cadena):
    rev= []
    for i in cadena:
        rev.insert(0, i)
    return rev
print(invertir(cadena))