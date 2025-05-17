edad = int(input())

def Mayor(edad):
    if edad >= 18:
        return "es mayor de edad"
    else:
        return "es menor de edad"
    
val = Mayor(edad)
print(val)