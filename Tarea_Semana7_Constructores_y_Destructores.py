#Tarea Semana 7 Contructores y Destructore

class DataProcessor:
    def __init__(self, datafile):
        """
        Constructor de la clase DataProcessor.
        Este método se llama automáticamente cuando se crea una instancia de la clase.

        :param datafile: Nombre del archivo de datos que se va a manejar.
        """
        # Inicializa el atributo datafile con el nombre del archivo de datos
        self.datafile = datafile
        # Inicializa el atributo file como None, que se utilizará para almacenar el objeto de archivo
        self.file = None
        # Llama al método load_file para cargar el archivo de datos
        self.load_file()

    def load_file(self):
        """Método para cargar el archivo en modo lectura."""
        try:
            # Intenta abrir el archivo en modo lectura y asignarlo al atributo file
            self.file = open(self.datafile, 'r')
            print(f"Archivo de datos '{self.datafile}' cargado correctamente.")
        except FileNotFoundError:
            # Maneja el error si el archivo no se encuentra
            print(f"Error: No se encontró el archivo de datos '{self.datafile}'.")
            # Asigna None al atributo file si el archivo no se encontró
            self.file = None

    def process_data(self):
        """Método para procesar el contenido del archivo de datos."""
        if self.file:
            # Lee el contenido del archivo y lo asigna a la variable data
            data = self.file.read()
            print("Procesando el contenido del archivo de datos:")
            print(data)
        else:
            # Muestra un mensaje de error si el archivo no está cargado
            print("No se puede procesar el archivo porque no está cargado.")

    def __del__(self):
        # Destructor de la clase DataProcessor.
        # Este método se llama automáticamente cuando se elimina una instancia de la clase.
        # Se utiliza para liberar recursos, como cerrar archivos abiertos.
        if self.file:
            # Cierra el archivo si estaba abierto
            self.file.close()
            print(f"Archivo de datos '{self.datafile}' cerrado correctamente.")

# Uso de la clase DataProcessor
if __name__ == "__main__":
    # Crear una instancia de DataProcessor con el archivo "datos.txt"
    processor = DataProcessor("datos.txt")

    # Procesar el contenido del archivo de datos
    processor.process_data()

    # La instancia processor será destruida automáticamente al final del programa,
    # y el destructor (__del__) se llamará para cerrar el archivo.
    # No es necesario llamar explícitamente al destructor, ya que Python se encargará de eliminar la instancia.