invitados = ["Ana", "Luis", "Sofia"]
usuario = input("Ingrese el nombre del invitado: ")
estar = False

for i in range(len(invitados)):
    if invitados[i] == usuario:
        print("Estas en la lista de invitados")
    