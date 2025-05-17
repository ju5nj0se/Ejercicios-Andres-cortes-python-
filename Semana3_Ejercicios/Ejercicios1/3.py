def ParImpar(numero):
    if numero % 2 == 0:
        return "espar"
    else:
        return "es impar"

a = int(input("Numero: "))

b = ParImpar(a)
print(b)

