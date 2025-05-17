import string 
Mayusculas = string.ascii_uppercase
Minusculas = string.ascii_lowercase
Numeros = string.digits
CarEspeciales = "!#$%&/()="

contraseña = input("Ingrese la contraseña: ")

listaContraseña = []

for i in contraseña:
    listaContraseña.append(i)

if Mayusculas in listaContraseña:
    print("si se puede")



