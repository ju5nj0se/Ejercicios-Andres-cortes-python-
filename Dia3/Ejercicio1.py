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
    1: {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    2: {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949},
    3: {'titulo': 'Noches Blancas', 'autor': 'Fyodor Dostoyevski', 'año': 1917}
}

#Variables que van a funcionar como filtros en caso de que el valor se erroneo o directamente no se introduzca un valor
ID = 0
Titulo = ""
Autor = ""
Año = None


# Creacion de la funciones que nos van a permitir hacer las diferentes acciones
def Crear(ID, Titulo, Autor, Año): #Agregar nuevos libros al diccionario
    ID = Biblioteca.key[-1]+1
    

'''
def Leer(): #Muestro todos los libros almacenados y permite buscar libros por su ID O Titulo

def Actualizar(): #Modifica la informacion de un libro por su ID 

def Eliminar(): #Elimina un libro por su ID

'''

Op = input("Elija una opcion")


if Op == 1:
    ID = int(input("Ingrese un id para el libro: "))
    Titulo = input("Ingrese un titulo para el libro: ")
    Autor = input("Ingrese un autor para el libro: ")
    Año = int(input("Ingrese el año de publicacion del libro: "))
    Crear(ID, Titulo, Autor, Año)
elif Op == 2:
