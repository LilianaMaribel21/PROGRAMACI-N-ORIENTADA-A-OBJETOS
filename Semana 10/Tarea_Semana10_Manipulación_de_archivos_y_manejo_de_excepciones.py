# Tarea Semana 10 - Manipulación de archivos y manejo de excepciones

import os

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self._id_producto = id_producto  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad en inventario
        self._precio = precio  # Precio del producto

    # Métodos para leer y escribir cada atributo
    def get_id_producto(self):
        return self._id_producto   # Devuelve el ID del producto

    def get_nombre(self):
        return self._nombre   # Devuelve el nombre del producto

    def set_nombre(self, nombre):
        self._nombre = nombre   # Establece el nombre del producto

    def get_cantidad(self):
        return self._cantidad   # Devuelve la cantidad del producto

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad    # Establece la cantidad del producto

    def get_precio(self):
        return self._precio   # Devuelve el precio del producto

    def set_precio(self, precio):
        self._precio = precio   # Establede el precio del producto

    # Método para mostrar la información del producto
    def mostrar_info(self):
        # Devuelve una cadena con la informqación del producto
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


    # Método para crear los datos del producto en una línea de texto
    def a_texto(self):
        return f"{self._id_producto},{self._nombre},{self._cantidad},{self._precio}"

# Clase que representa el inventario de productos
class Inventario:
    def __init__(self, archivo):
        # Inicializa la lista de productos y el nombre del archivo
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # Método para cargar los productos desde un archivo
    def cargar_desde_archivo(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        id_producto, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                print("Inventario cargado desde archivo con éxito.")  # Carga exitosa
            else:
                print(f"Archivo '{self.archivo}' no encontrado, se creará uno nuevo.")  # Archivo no encontrado
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo}' no fue encontrado.")  # Manejo de excepción
        except PermissionError:
            print(f"Error: Permiso denegado para leer el archivo '{self.archivo}'.")  # Manejo de excepción
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")  # Manejo de excepción genérica

    # Método para guardar los productos en un archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(producto.a_texto() + '\n')
            print("Inventario guardado en archivo con éxito.")  # Guardado exitoso
        except PermissionError:
            print(f"Error: Permiso denegado para escribir en el archivo '{self.archivo}'.")  # Manejo de excepción
        except Exception as e:
            print(f"Error inesperado al escribir en el archivo: {e}")  # Manejo de excepción genérica

    # Método para añadir un producto al inventario
    def añadir_producto(self, producto):
        # Verifica que el ID del producto sea único antes de añadirlo
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.")  # ID duplicado
                return
        self.productos.append(producto)
        self.guardar_en_archivo()  # Guarda el inventario en archivo
        print("Producto añadido con éxito.")  # Añadido exitoso

    # Método para eliminar un producto del inventario por ID
    def eliminar_producto(self, id_producto):
        # Elimina el producto por su ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()  # Guarda el inventario en archivo
                print("Producto eliminado con éxito.")  # Eliminado exitoso
                return
        print("Error: Producto no encontrado.")  # Código de error

    # Método para actualizar un producto en el inventario
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio del producto por ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()  # Guarda el inventario en archivo
                print("Producto actualizado con éxito.")  # Actualizado exitoso
                return
        print("Error: Producto no encontrado.")  # Código de error

    # Método para buscar un producto en el inventario por su nombre
    def buscar_producto(self, nombre):
        # Busca productos por nombre (puede haber nombres similares)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p.mostrar_info())
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos en el inventario
    def mostrar_todos(self):
        # Muestra todos los productos en el inventario
        if self.productos:
            for p in self.productos:
                print(p.mostrar_info())
        else:
            print("El inventario está vacío.")


# Función que muestra el menú de opciones al usuario
def menu():
    # Inicializa el inventario con el archivo de almacenamiento
    inventario = Inventario("inventario.txt")

    while True:
        # Muestra el menú de opciones
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        #Lee la opción señalada por el usuario
        opcion = input("Seleccione una opción: ")

        # Ejecura la acción correspondiente a la opción seleccionada
        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiarla): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para no cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del menú si se ejecuta como script principal
if __name__ == "__main__":
    menu()
