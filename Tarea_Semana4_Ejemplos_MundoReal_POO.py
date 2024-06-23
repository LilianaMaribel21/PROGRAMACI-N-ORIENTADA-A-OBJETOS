class Camioneta:
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None  # Inicialmente, la camioneta no tiene conductor

    def asignar_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona

    def __str__(self):
        return f'Camioneta {self.modelo} del año {self.anio}, conducido por {self.conductor.nombre if self.conductor else "nadie"}.'


class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Persona {self.nombre} con licencia número {self.licencia}.'


# Creamos objetos
camioneta1 = Camioneta('Ford F150', 2010)
camioneta2 = Camioneta('Chevrolet Luv Dmax', 2012)
persona = Persona('Elizabeth', 5)

# Asignaremos un conductor a la camioneta
camioneta1.asignar_conductor(persona)

# Ejemplo de salida
print(camioneta1)   # Debe imprimir: Camioneta Ford F150 del año 2010, conducido por Elizabeth.
print(camioneta2)   # Debe imprimir: Camioneta Chevrolet Luv Dmax del año 2012, conducido por Kennya
print(persona)      # Debe imprimir: Persona Elizabeth con licencia número 5.
