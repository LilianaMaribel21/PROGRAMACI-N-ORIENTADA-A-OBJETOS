# Tarea Semana 9 - Sistema de Gestión de Inventarios

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



# Clase que representa el inventario de productos
class Inventario:
    def __init__(self):
        # Crear lista para almacenar los productos
        self.productos = []

    # Método para añadir o eliminar productos

    def añadir_producto(self, producto):
        # Verificar si el ID del producto es único
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.") # código de error
                return
    # Agrega el producto al inventario
        self.productos.append(producto)
        print("Producto añadido con éxito.") # código exitoso

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        # Busca el producto en el inventario y lo elimina
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado con éxito.") # código exitoso
                return
        print("Error: Producto no encontrado.") # código de error

    # Método para actualizar la cantidad o precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Busca el ID producto en el inventario y actualiza su cantidad o precio
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado con éxito.") # código exitoso
                return
        print("Error: Producto no encontrado.") # código de error

    # Método para buscar producos por su nombre
    def buscar_producto(self, nombre):
        # Buscar productos en el inventario que coincidan con el nombre
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
        # Muestra la información de los productos encontrados
            for p in resultados:
                print(p.mostrar_info())
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos en el inventario
    def mostrar_todos(self):
        # Muestra la información de todos los productos en el inventario
        if self.productos:
            for p in self.productos:
                print(p.mostrar_info())
        else:
            print("El inventario está vacío.")


# Función que muestra el menú de opciones al usuario
def menu():
    # Creea una instancia de la clase Inventario
    inventario = Inventario()

    while True:
        # Muestra el menú de opciones
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        # Lee la opción seleionada por el usuario
        opcion = input("Seleccione una opción: ")

# Ejecuta la acción correspondiente a la opción seleccionada
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
            cantidad = input("Ingrese la nueva cantidad (o deje en blaco  para no cambiarla): ")
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
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()