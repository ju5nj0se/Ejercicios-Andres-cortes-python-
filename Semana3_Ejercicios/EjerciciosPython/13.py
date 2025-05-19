n = int(input("Ingrese el limite de  numeros naturales que quiere sumar: "))
suma = 0

for i in range(1, n+1):
    suma = suma + i
print(suma)