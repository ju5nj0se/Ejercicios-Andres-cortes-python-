#Cada contacto debe de tener Nombre, Telefono y Email
#El nombre del contacto debe de ser unico y al actualizar o eliminar primero se debe verificar que exista el contacto



#Diccionario
Agenda = {"Juan":{"telefono":321, "email": "juan@hotmal.com"},
          "Ana":{"telefono":123, "email": "ana@hotmal.com"}
}

#Menu
def Menu():
    while True:
        try:
            Opcion = int(input("\n---Agenda---\n" \
            
            "1 Para agregar un nuevo contacto.\n"  \
            "2 Para buscar contacto.\n" \
            "3 Para actualizar un contacto.\n" \
            "4 Para eliminar un contacto\n" \
            "5 Para salir\n" \
            "--> "))
        except ValueError :
            Opcion = int(input("Ingrese una opcion valida \n" \
                               "--> "))
            continue
        else:
            return Opcion

# Varaiables
Nombre, Telefono, Email = None, None, None

def CrearContacto():
    Nombre = str(input("\nIngrese un nombre.\n--> "))
    Telefono = int(input("\nIngrese un Telefono.\n--> "))
    Email = str(input("\nIngrese un Email.\n--> "))

    while True:

        if Nombre in Agenda.keys():
                Nombre = input("\nEste nombre ya existe. Ingrese un diferente\n--> ")
        else:
            Agenda.setdefault(Nombre, {"telefono":Telefono, "email":Email}) #def clave para añadir clave:valor{clave:valor}
            print("Contacto creado con exito!")
            break

def BuscarContacto():
    
    while True:
        try:
            Buscar = int(input("\n- 1 Para listar todos los contactos. \n" \
                                "- 2 Para buscar un contacto por su nombre\n--> "))
        
        except ValueError or Buscar in range(1,2):
            print("ERROR: Ingrese una opcion valida")
            continue

        else:
            if Buscar == 1:
                for i in Agenda.keys():
                    print(f"\n- Nombre: {i}\n" \
                            f"- Telefono: {Agenda.get(i).get("telefono")}\n" \
                            f"- Email: {Agenda.get(i).get("email")}")
                break
            elif Buscar == 2:
                Nombre = input("\nIngrese el nombre a buscar\n--> ")
                
                if Nombre in Agenda.keys():
                    print(f"Nombre: {Nombre}\n" \
                              f"Telefono: {Agenda.get(Nombre).get("telefono")}\n" \
                              f"Email: {Agenda.get(Nombre).get("email")}")
                        
                break

def ActualizarContacto():
    Nombre = str(input(f"\nIngrese el nombre del contacto a actualizar\n--> "))
    if Nombre in Agenda.keys():
        print("\nContacto encontrado")
        Agenda[Nombre]["telefono"] = input(f"\nTelefono antiguo: {Agenda.get(Nombre).get("telefono")}\n--> ")
        Agenda[Nombre]["email"] = input(f"\nEmail antiguo: {Agenda.get(Nombre).get("email")}\n--> ")
        print("\nContacto actualizado con exito!")

    elif Nombre is not Agenda.keys():
        print("Contacto no encontrado")

def EliminarContacto():
        Nombre = str(input(f"\nIngrese el nombre del contacto a eliminar\n--> "))
        if Nombre in Agenda.keys():
            Agenda.pop(Nombre)
            print("Contacto Eliminado con exito")
        elif Nombre is not Agenda.keys():
            print("Contacto no encontrado")


#Comienzo del Programa                    
while True:
    Opcion = Menu()
    
    if Opcion == 1:
        CrearContacto()

    elif Opcion == 2:
        BuscarContacto()

    elif Opcion == 3:
        ActualizarContacto()
    
    elif Opcion==4:
        EliminarContacto()

    elif Opcion == 5:
        break
    
    

        

