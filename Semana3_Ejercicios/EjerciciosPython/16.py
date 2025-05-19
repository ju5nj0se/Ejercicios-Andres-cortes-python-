from random import *
a = randint(1, 10)

flag = True
while flag:
    numero = int(input(">> "))

    if numero > a:
        print("\nRestale")
    elif numero < a:
        print("\nSumale")
    elif numero == a:
        print("Lo encontraste!!")
        flag = False
    