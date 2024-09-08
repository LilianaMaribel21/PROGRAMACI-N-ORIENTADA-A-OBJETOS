# Tarea Semana 12: Sistema de Gestión de Biblioteca Digital

import json

# Clase Libro: representa un libro con atributos como título, autor, categoría e ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.categoria = categoria  # Categoría a la que pertenece el libro
        self.isbn = isbn      # Identificador único del libro (ISBN)

# Clase Usuario: representa un usuario con nombre, ID y lista de libros prestados
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre  # Nombre del usuario
        self.id_usuario = id_usuario  # Identificación única del usuario
        self.libros_prestados = []  # Lista de libros prestados por el usuario

# Clase Biblioteca: administra libros, usuarios y el sistema de préstamos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario de libros disponibles con el ISBN como clave
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios registrados
        self.historial_prestamos = {}  # Registro de préstamos {ID_usuario: [lista de ISBNs]}

    # Método para añadir un nuevo libro a la biblioteca
    def anadir_libro(self, titulo, autor, categoria, isbn):
        if isbn not in self.libros_disponibles:
            nuevo_libro = Libro(titulo, autor, categoria, isbn)  # Crear una instancia de libro
            self.libros_disponibles[isbn] = nuevo_libro  # Agregar el libro al diccionario de libros disponibles
            print(f"Libro '{titulo}' añadido exitosamente.")
        else:
            print(f"El libro con ISBN {isbn} ya existe en la biblioteca.")

    # Método para eliminar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]  # Eliminar el libro del diccionario
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    # Método para registrar un nuevo usuario
    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            nuevo_usuario = Usuario(nombre, id_usuario)  # Crear una instancia de usuario
            self.usuarios_registrados.add(id_usuario)  # Agregar el ID de usuario al conjunto
            self.historial_prestamos[id_usuario] = []  # Iniciar el historial de préstamos del usuario
            print(f"Usuario '{nombre}' registrado exitosamente.")
        else:
            print(f"El usuario con ID {id_usuario} ya está registrado.")

    # Método para eliminar un usuario registrado
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)  # Eliminar el usuario del conjunto de registrados
            del self.historial_prestamos[id_usuario]  # Eliminar su historial de préstamos
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Método para prestar un libro a un usuario registrado
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            if isbn not in self.historial_prestamos[id_usuario]:
                self.historial_prestamos[id_usuario].append(isbn)  # Agregar el libro al historial de préstamos
                print(f"Libro con ISBN {isbn} prestado al usuario con ID {id_usuario}.")
            else:
                print(f"El usuario ya tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"ID de usuario o ISBN incorrecto.")

    # Método para devolver un libro prestado
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.historial_prestamos[id_usuario]:
            self.historial_prestamos[id_usuario].remove(isbn)  # Eliminar el libro del historial de préstamos
            print(f"Libro con ISBN {isbn} devuelto por el usuario con ID {id_usuario}.")
        else:
            print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")

    # Método para buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if getattr(libro, criterio, '').lower() == valor.lower()]
        if resultados:
            for libro in resultados:
                print(f"Encontrado: {libro.titulo} por {libro.autor}")
        else:
            print(f"No se encontraron libros por {criterio}: {valor}")

    # Método para listar los libros que tiene prestado un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            prestamos = self.historial_prestamos.get(id_usuario, [])
            if prestamos:
                print(f"Libros prestados a {id_usuario}:")
                for isbn in prestamos:
                    libro = self.libros_disponibles.get(isbn)
                    print(f"  - {libro.titulo} por {libro.autor}")
            else:
                print(f"El usuario con ID {id_usuario} no tiene libros prestados.")
        else:
            print(f"Usuario con ID {id_usuario} no registrado.")

    # Método para guardar los datos de la biblioteca en un archivo JSON
    def guardar_datos(self, archivo):
        with open(archivo, 'w') as f:
            datos = {
                'libros': {isbn: libro.__dict__ for isbn, libro in self.libros_disponibles.items()},
                'usuarios': list(self.usuarios_registrados),
                'prestamos': self.historial_prestamos
            }
            json.dump(datos, f)
            print(f"Datos guardados en {archivo}.")

    # Método para cargar los datos de la biblioteca desde un archivo JSON
    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.libros_disponibles = {isbn: Libro(**libro) for isbn, libro in datos['libros'].items()}
                self.usuarios_registrados = set(datos['usuarios'])
                self.historial_prestamos = datos['prestamos']
                print(f"Datos cargados desde {archivo}.")
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")

# Menú interactivo para administrar la biblioteca
def menu():
    biblioteca = Biblioteca()
    archivo_datos = 'biblioteca_datos.json'
    biblioteca.cargar_datos(archivo_datos)

    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados")
        print("9. Guardar y salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.anadir_libro(titulo, autor, categoria, isbn)
        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)
        elif opcion == '4':
            id_usuario = input("ID de usuario: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == '5':
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == '6':
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == '7':
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input(f"Introduce el valor para buscar por {criterio}: ")
            biblioteca.buscar_libros(criterio, valor)
        elif opcion == '8':
            id_usuario = input("ID de usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)
        elif opcion == '9':
            biblioteca.guardar_datos(archivo_datos)
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")

menu()
