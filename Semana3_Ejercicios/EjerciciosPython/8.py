operacion = input("Ingrese la operacio aritmetica\n- Suma(+)\n- Resta(-)\n- Multiplicacion(*)\n- Division(/)\n--> ")

match operacion:
    case "+":
        num1 = int(input("Numero 1: "))
        num2 = int(input("Numero 2: "))

        print(f"Resultado-> {num1 + num2}")

    case "-":
        num1 = int(input("Numero 1: "))
        num2 = int(input("Numero 2: "))

        print(f"Resultado-> {num1 - num2}")

    case "*":
        num1 = int(input("Numero 1: "))
        num2 = int(input("Numero 2: "))

        print(f"Resultado-> {num1 * num2}")

    case "/":
        num1 = int(input("Divisor: "))
        num2 = int(input("Dividendo: "))

        print(f"Resultado-> {num1/num2}")