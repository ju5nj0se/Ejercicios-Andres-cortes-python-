Saldo  = int(500000)
Depositar = None
Retirar = None
Historial = []

while True:
    Elegir = int(input("\n---Bienvenido Juan---\n" \
    "1 Para ver el saldo de su cuenta\n" \
    "2 Para retirar dinero\n" \
    "3 Para depositar dinero\n" \
    "4 Para ver el historial de transacciones\n" \
    "5 Para retirar su tarjeta\n" \
    "--> "))

    if Elegir == 1:
        print(f"\nTienes un saldo de {Saldo}")

     
    elif Elegir == 2:
        Retirar = int(input("\nIngrese la cantidad de dinero a retirar\n--> "))
        if Retirar < Saldo:
            Saldo = Saldo - Retirar
            Historial.append(f"- Retiro de {Retirar}")
            print("Dinero retirado")
        else:
            print("Saldo insuficiente :)")

    elif Elegir == 3:
        Depositar = int(input("\nIngrese la cantidad de dinero a depositar\n--> "))
        Saldo = Saldo + Depositar
        Historial.append(f"- Deposito de {Depositar}")
        print("Dinero depositado")

    elif Elegir == 4:
        print("\n--Historial de transacciones--")
        for i in Historial:
            print(i)

    elif Elegir == 5:
        print("Adios Juan")
        break


    
