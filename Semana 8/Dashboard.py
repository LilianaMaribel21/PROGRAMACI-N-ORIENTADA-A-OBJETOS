import os


# Función para mostrar el código de un script Python
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)

    # Intenta abrir el archivo y leer su contenido
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            # Imprime un título con el nombre del script
            print(f"\n--- Código de {ruta_script} ---\n")
            # Lee y imprime el contenido del archivo
            print(archivo.read())
    except FileNotFoundError:
        # Si el archivo no se encuentra, imprime un mensaje de error
        print("El archivo no se encontró.")
    except Exception as e:
        # Si ocurre cualquier otro error al leer el archivo, imprime un mensaje de error
        print(f"Ocurrió un error al leer el archivo: {e}")


# Función para mostrar el menú principal
def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Define un diccionario con las opciones del menú
    opciones = {
        '1': 'Semana 2/Tarea_Semana2.py',
        '2': 'Semana 3/Tarea_Semana3_Programación_Tradicional.py',
        '3': 'Semana 4/Tarea_Semana4_Ejemplo2_Mundo_Real_POO.py',
        '4': 'Semana 4/Tarea_Semana4_Ejemplos_MundoReal_POO.py',
        '5': 'Semana 5/Tarea_Semana5_Tipos_de_datos_Identificadores.py',
        '6': 'Semana 6/Tarea_Semana6_Clases_objetos_herencia_encapsulamiento_y_polimorfismo.py',
        '7': 'Semana 7/Tarea_Semana7_Constructores_y_Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }
    while True:
        # Imprime el título del menú
        print("\nMenu Principal - Dashboard")

        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        # Pide al usuario que seleccione una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")

        # Si el usuario selecciona la opción 0, sale del bucle
        if eleccion == '0':
            break
        # Si el usuario selecciona una opción válida, muestra el código del script
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        # Si el usuario selecciona una opción no válida, imprime un mensaje de error
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard solo si se llama directamente al script
if __name__ == "__main__":
    mostrar_menu()