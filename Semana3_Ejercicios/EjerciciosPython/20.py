altura = int(input("Altura: "))

for i in range(1, altura+1):

    print(" " * int(altura - i) + "*" * int(2 * i - 1))
    
