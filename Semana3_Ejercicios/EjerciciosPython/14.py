num = int(input("Ingrese el numero del que desea saber su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")