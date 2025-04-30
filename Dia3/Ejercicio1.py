# Cada libro debe de tener ID, titulo, autor y año de publicacion

#Menu
print("---------------------------------------------\n" \
"1 para agregar un libro\n" \
"2 para mostrar todos los libros almacenados\n" \
"3 para actualizar un libro\n" \
"4 para eliminar un libro\n"
"5 para salir\n" \
"---------------------------------------------")

#Creacion del diccionario Biblioteca
Biblioteca = {
    0: {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    1: {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949},
    2: {'titulo': 'Noches Blancas', 'autor': 'Fyodor Dostoyevski', 'año': 1917}
}

#Variables que van a funcionar como filtros en caso de que el valor se erroneo o directamente no se introduzca un valor
ID = int()
Titulo = str()
Autor = str()
Año = int()


# Creacion de la funciones que nos van a permitir hacer las diferentes acciones
def Crear(Titulo, Autor, Año): #Agregar nuevos libros al diccionario
    ID = int(len(Biblioteca))
    print(Biblioteca)
    Biblioteca.setdefault(ID, (Titulo, Autor, Año))
    print(Biblioteca)

def Buscar(ID, Titulo): #Mostrar todos lo libros almacenados y permitir buscar un libro por su ID o Titulo
    if ID != None:
        if ID in Biblioteca.keys():
            print(f"Id: {Biblioteca.get(ID)}")
    
Op = int(input("Elija una opcion: "))


if Op == 1:
    Titulo = input("Ingrese un titulo para el libro: ")
    Autor = input("Ingrese un autor para el libro: ")
    Año = int(input("Ingrese el año de publicacion del libro: "))
    Crear(Titulo, Autor, Año)
