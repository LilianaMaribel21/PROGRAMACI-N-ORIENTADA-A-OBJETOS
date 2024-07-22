# Aplicación de Conceptos de POO
# Clases, objetos, herencia, encapsulamiento y polimorfismo


# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Encapsulación de atributo
        self._edad = edad  # Encapsulación de atributo

    def detalles(self):
        return f'Nombre: {self._nombre}, Edad: {self._edad}'

# Clase derivada Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self._salario = salario  # Encapsulación de atributo

    def detalles(self):
        return f'{super().detalles()}, Salario: {self._salario}'

# Clase derivada Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self._carrera = carrera  # Encapsulación de atributo

    def detalles(self):
        return f'{super().detalles()}, Carrera: {self._carrera}'

# Clase derivada Profesor, derivada de Empleado
class Profesor(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self._departamento = departamento  # Encapsulación de atributo

    def detalles(self):
        return f'{super().detalles()}, Departamento: {self._departamento}'

# Clase derivada Administrador, derivada de Empleado
class Administrador(Empleado):
    def __init__(self, nombre, edad, salario, puesto):
        super().__init__(nombre, edad, salario)
        self._puesto = puesto  # Encapsulación de atributo

    def detalles(self):
        return f'{super().detalles()}, Puesto: {self._puesto}'

# Clase derivada Interno, derivada de Estudiante
class Interno(Estudiante):
    def __init__(self, nombre, edad, carrera, empresa):
        super().__init__(nombre, edad, carrera)
        self._empresa = empresa  # Encapsulación de atributo

    def detalles(self):
        return f'{super().detalles()}, Empresa: {self._empresa}'

# Polimorfismo con método sobrescrito
def mostrar_detalles(persona):
    print(persona.detalles())

# Polimorfismo con argumentos múltiples
def mostrar_saludo(persona, saludo='Buenos días'):
    print(f'{saludo}, {persona._nombre}')

# Creación de instancias y demostración de funcionalidad
profesor = Profesor('Cristian', 35, 500, 'Química')
administrador = Administrador('Kennya', 40, 600, 'Trabajo Social')
interno = Interno('Elizabeth', 26, 'Ingeniería', 'Coorporacion La Favorita')

# Usar métodos para demostrar la funcionalidad
mostrar_detalles(profesor)
mostrar_detalles(administrador)
mostrar_detalles(interno)

# Polimorfismo con múltiples argumentos
mostrar_saludo(profesor)
mostrar_saludo(interno, 'Bienvenida')
