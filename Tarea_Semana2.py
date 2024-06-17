class Personaje:

    # Creamos un nuevo personaje con sus atributos básicos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre  
        self.fuerza = fuerza  
        self.inteligencia = inteligencia  
        self.defensa = defensa  
        self.vida = vida  
        self.nivel = 1  

    # Procedimiento para mostrar los atributos del personaje
    def atributos(self):
        print(f"{self.nombre} (Nivel {self.nivel}):")  # Indica el nombre y nivel del personaje
        print(f"· Fuerza: {self.fuerza}")  # Indica la fuerza del personaje
        print(f"· Inteligencia: {self.inteligencia}")  # Indica la inteligencia del personaje
        print(f"· Defensa: {self.defensa}")  # Indica la defensa del personaje
        print(f"· Vida: {self.vida}")  # Indica la vida del personaje

    # Procedimiento para subir de nivel y mejorar los atributos del personaje
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza  # Aumenta la fuerza del personaje
        self.inteligencia += inteligencia  # Aumenta la inteligencia del personaje
        self.defensa += defensa  # Aumenta la defensa del personaje
        self.nivel += 1  # Aumenta el nivel del personaje

    # Procedimiento para verificar si el personaje está vivo
    def esta_vivo(self):
        return self.vida > 0  # Devuelve True si la vida es mayor que 0

    # Procedimiento para marcar al personaje como muerto
    def morir(self):
        self.vida = 0  # Establece la vida a 0
        print(f"{self.nombre} ha muerto")  # Imprime que el personaje ha muerto

    # Procedimiento para recibir daño y reducir la vida del personaje
    def recibir_daño(self, daño):
        daño_real = max(daño - self.defensa, 0)  # Calcula el daño real restando la defensa
        self.vida -= daño_real  # Reduce la vida por el daño recibido
        print(f"{self.nombre} ha recibido {daño_real} puntos de daño")  # Indica el daño recibido
        if not self.esta_vivo():  # Si la vida es 0 o menos, el personaje muere
            self.morir()

    # Procedimiento para atacar a otro personaje
    def atacar(self, enemigo):
        daño = self.calcular_daño()  # Calcula el daño a infligir
        enemigo.recibir_daño(daño)  # El enemigo recibe el daño

    # Procedimiento para calcular el daño básico del personaje (puede ser sobrescrito en subclases)
    def calcular_daño(self):
        return self.fuerza  # Devuelve la fuerza como el daño básico

# Clase 'Guerrero' que hereda de 'Personaje'
class Guerrero(Personaje):

    # Inicializa un guerrero con atributos adicionales
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de la clase base
        self.espada = espada  # Daño adicional del arma espada

    # Procedimiento para cambiar el arma del guerrero
    def cambiar_arma(self, daño_espada):
        self.espada = daño_espada  # Actualiza el daño de la espada

    # Reemplazar el método 'atributos' para incluir la espada
    def atributos(self):
        super().atributos()  # Llama al método 'atributos' de la clase base
        print(f"· Espada: {self.espada}")  # Indica el daño de la espada

    # Reemplazar el método 'calcular_daño' para incluir el daño de la espada
    def calcular_daño(self):
        return self.fuerza + self.espada  # Regresa la fuerza más el daño de la espada

# Clase 'Mago' que hereda de 'Personaje'
class Mago(Personaje):

    # Inicializa un mago con atributos adicionales
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  # Llama al constructor de la clase base
        self.libro = libro  # Poder adicional del libro de hechizos

    # Procedimiento para cambiar el libro del mago
    def cambiar_libro(self, poder_libro):
        self.libro = poder_libro  # Renueva el poder del libro

    # Reemplazar el método 'atributos' para incluir el libro
    def atributos(self):
        super().atributos()  # Llama al método 'atributos' de la clase base
        print(f"· Libro: {self.libro}")  # Muestra el poder del libro

    # Reemplazar el método 'calcular_daño' para incluir el poder del libro
    def calcular_daño(self):
        return self.inteligencia + self.libro  # Devuelve la inteligencia más el poder del libro

# Función para simular un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 1  # Inicia el contador de turnos
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():  # Continúa mientras ambos personajes estén vivos
        print(f"\nTurno {turno}")  # Indica el número de turno
        if jugador_1.esta_vivo():  # Si el jugador 1 está vivo ataca
            print(f">>> Acción de {jugador_1.nombre}:")
            jugador_1.atacar(jugador_2)  # El jugador 1 ataca al jugador 2
            jugador_1.atributos()  # Indica los atributos del jugador 1
        if jugador_2.esta_vivo():  # Si el jugador 2 está vivo, ataca
            print(f">>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)  # El jugador 2 ataca al jugador 1
            jugador_2.atributos()  # Indica los atributos del jugador 2
        turno += 1  # Aumenta el contador de turnos
    if jugador_1.esta_vivo():  # Si el jugador 1 sigue vivo después del combate gana
        print(f"\nHa obtenido la victoria {jugador_1.nombre}")
    elif jugador_2.esta_vivo():  # Si el jugador 2 sigue vivo después del combate gana
        print(f"\nHa obtenido la victoria {jugador_2.nombre}")
    else:  # Si los dos mueren marca un empate
        print("\nEmpate")

# Modo de uso: creación de un guerrero y un mago
personaje_1 = Guerrero("Cristina", 25, 23, 4, 100, 5)  
personaje_2 = Mago("Valentina", 10, 12, 4, 100, 8)  

# Indica los atributos iniciales de los personajes
personaje_1.atributos()
personaje_2.atributos()

# Empieza el combate entre los dos personajes
combate(personaje_1, personaje_2)
