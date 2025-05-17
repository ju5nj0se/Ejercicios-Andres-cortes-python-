from random import *

def GeneraNumero():
    numero = randint(1, 6)
    return numero

flag = True
while flag:
    op = input("1 Para salir y ENTER para tirar el dado\n>>")

    if op == "1":
        flag = False
    elif op == "":
        n = GeneraNumero()
        print(f"Ha salido la cara {n}")