#Funcion Menu
def Menu(Elegir):
    while True:
        try:
            Elegir = int(input("\n----Bienvenido  a la Biblioteca Virtual----\n" \
                "- 1 Para agregar un libro\n" \
                "- 2 Para buscar libros\n" \
                "- 3 Para actualizar un libro\n" \
                "- 4 Para eliminar un libro\n"
                "- 5 Para salir\n" \
                "--> "))
        except ValueError:
            Elegir = int(input("\nERROR: La opcion debe ser un numero\n--> "))
            continue 
        if Elegir < 1 or Elegir > 5:
            Elegir = int(input(("\nERROR: Las opciones esta de 1 a 5\n--> ")))
            continue
        break
    return Elegir
    

#Diccionario
Biblioteca = {
    "00": {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    "01": {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949},
    "02": {'titulo': 'Noches Blancas', 'autor': 'Fyodor Dostoyevski', 'año': 1917}
}

# FUNCIONES CRUD
def Crear(): #Crear Libro
    ID = str(input("\nIngrese un ID para el libro.\n--> "))
    Titulo = str(input("\nIngrese un titulo para el libro.\n--> "))
    Autor = str(input("\nIngrese un autor para el libro.\n-->"))

    while True:
        try:
            Año = int(input("\nIngrese el año de publicacion del libro.\n--> "))

        except ValueError:
            print("ERROR: Ingrese un año valido")
            continue
        if ID == "":
            ID = input("\nERROR: El ID no puede estar vacio\n--> ")
            continue
        elif ID in Biblioteca.keys():
            ID = input("\nERROR: El ID ya existe, ingrese uno diferente\n--> ")
            continue
            
        Biblioteca.setdefault(ID, {'titulo': Titulo, 'autor': Autor, 'año': Año})
        print("\nDocumento creado con exito!")
        break

def Buscar(): #Buscar libro e imprmir todos los libros
    VerLibros = input("- Para ver todos los libros almacenados escriba 'ver'.\n- Para buscar un libro por su ID o Titulo escriba 'see'.\n--> ")

    while True: 
        #Ver todos los libros
        if VerLibros == "ver": 
            for i in Biblioteca.keys():
                print(f"\n- ID: {i}\n- Titulo: {Biblioteca.get(i).get("titulo")}\n- Autor: {Biblioteca.get(i).get("autor")}\n- Año: {Biblioteca.get(i).get("año")}") 
            break
        #Buscar libro por ID o Titulo
        elif VerLibros == "see": #Opcion en caso de que quiera buscar un libro por su titulo o por su autor
        
            print("Si no conoce algun campo, dejelo vacio. Para salir deje los 2 campos vacios")
            ID = str(input("Ingrese el ID del libro\n--> "))
            Titulo = str(input("Ingrese el Titulo del libro\n--> "))

            if ID in Biblioteca.keys() and Titulo == "":
                print(f"\n- ID: {ID}\n- Titulo: {Biblioteca.get(ID).get('titulo')}\n- Autor: {Biblioteca.get(ID).get('autor')}\n- Año: {Biblioteca.get(ID).get('año')}")
                break

            elif Titulo != "" and ID == "":
                for i in Biblioteca.keys():
                    if Titulo == Biblioteca.get(i).get("titulo"):
                        print(f"\n- ID: {i}\n- Titulo: {Biblioteca.get(i).get("titulo")}\n- Autor: {Biblioteca.get(i).get("autor")}\n- Año: {Biblioteca.get(i).get("año")}")
                break

            elif Titulo == "" and ID == "":
                break

def Actualizar(ID): #Actualizar libro
    ID = str(input("Ingrese el ID del libro que va actualizar\n-->"))
    while True:
        if ID in Biblioteca.keys():
            Titulo = str(input(f"\nTitulo anterior --> {Biblioteca.get(ID).get("titulo")}\nNuevo titulo--> "))
            Autor = str(input(f"\nAutor anterior--> {Biblioteca.get(ID).get("autor")}\nNuevo Autor--> "))
            while True:
                try:
                    Año = int(input(f"\nAño anterior--> {Biblioteca.get(ID).get("año")}\nNuevo año -->"))
        
                except:
                    print("ERROR: Ingrese un año valido")
                    continue
                    
                NewDict = {"titulo":Titulo, "autor":Autor, "año":Año}
                Biblioteca[ID].update(NewDict)
                print("Libro Actualizado!!")
                break
        elif ID is not Biblioteca.keys():
            print("Libro no encontrado")
            break
       
def Eliminar(): #Eliminar Libro
    ID = str(input("Ingrese ID del libro que desea eliminar\n--> "))
    if ID in Biblioteca.keys():
        Biblioteca.pop(ID)
        print("Libro Eliminado con exito!")
    elif ID is not Biblioteca.keys():
        print("No se ha podido encontrar el Libro, asegurese de haber ingresado el ID bien")
    


#Declaracion de variables principales
ID = str()
Titulo =str()
Autor = str()
Año = int()         

Elegir = int(0)

#COMIENZO DEL PROGRAMA
while True:
    Elegir = Menu(Elegir)
    
    if Elegir == 1:
        Crear()

    elif Elegir == 2:
        Buscar()
        
    elif Elegir == 3:
        Actualizar(ID)
    
    elif Elegir == 4:
        Eliminar()

    elif Elegir == 5:
        print("\nBye Bye")
        break
