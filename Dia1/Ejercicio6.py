import random
NumeroRandom = int(random.randint(1, 10))
adivinar = int(input("Adivina el número entre 1 y 10\n: "))
while adivinar != NumeroRandom:
    NumeroRandom = int(random.randint(1, 10))
    if adivinar == NumeroRandom:
        print("Correcto!")

    elif adivinar > NumeroRandom:
        print(" \nEl numero es menor")
        adivinar = int(input(": "))

    elif adivinar < NumeroRandom:
        print(" \nEl numero es mayor")
        adivinar = int(input(": "))