# Ejemplo2 Mundo POO - Concesionaria de renta de camionetas

class Camionetas:
    def __init__(self, modelo, tipo, precio):
        self.modelo = modelo
        self.tipo = tipo
        self.precio = precio
        self.ocupado = False

    def reservar(self):
        if not self.ocupado:
            self.ocupado = True
            return True
        return False

    def liberar(self):
        self.ocupado = False

    def __str__(self):
        estado = 'ocupado' if self.ocupado else 'disponible'
        return f'Auto {self.modelo}: Tipo {self.tipo}, Precio {self.precio} - {estado}'

class Camioneta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.camionetas = []

    def agregar_camioneta(self, camioneta):
        self.camionetas.append(camioneta)

    def mostrar_camionetas(self):
        for camioneta in self.camionetas:
            print(camioneta)

    def reservar_camioneta(self, modelo):
        for camioneta in self.camionetas:
            if camioneta.modelo == modelo:
                return camioneta.reservar()
        return False

    def liberar_camioneta(self, modelo):
        for camioneta in self.camionetas:
            if camioneta.modelo == modelo:
                camioneta.liberar()
                return True
        return False

# Crear instancias y mostrar la interacción
concesionaria = Camioneta("Camionetas en renta")

# Agregar camionetas a la Concesionaria
concesionaria.agregar_camioneta(Camionetas("Chevrolet", "Luv Dmax 4x4", 1500))
concesionaria.agregar_camioneta(Camionetas("Toyota", "Hilux", 2275))
concesionaria.agregar_camioneta(Camionetas("Suzuki", "Vitara Live 2020", 2150))

# Mostrar camionetas
print("Estado inicial de las camionetas:")
concesionaria.mostrar_camionetas()

# Reservar una camioneta
print("\nReservando la camioneta Chevrolet...")
concesionaria.reservar_camioneta("Chevrolet")
concesionaria.mostrar_camionetas()

# Liberar una camioneta
print("\nLiberando la camioneta Chevrolet...")
concesionaria.liberar_camioneta("Chevrolet")
concesionaria.mostrar_camionetas()