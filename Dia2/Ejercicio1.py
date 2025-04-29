num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

if (num1 < num2 and num1 < num3 ):
    print("Es menor: ", num1)
elif (num2 < num1 and num2 <num3):
    print("Es menor: ", num2)
else:
    print("Es menor: ", num3)