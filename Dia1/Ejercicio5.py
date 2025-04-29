compra = int(input("¿Cuánto has gastado en la tienda?: "))
porcentaje = float(input("¿Qué porcentaje de propina quieres dejar?: "))
propina = float(compra * porcentaje / 100)
print("Propina: ", propina)