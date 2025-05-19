nf = int(input("Ingrese el numero a factoriar: "))
factorial = 1

for i in range(1, nf+1):
    factorial *= i

print(factorial)