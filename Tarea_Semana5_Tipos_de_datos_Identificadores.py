# Este programa calculara: el área de un cuadrado y el área de un círculo
# Convertira unidades de medida
# Gestiona información clave de un registro.

import math

def calcular_area_cuadrado(ancho, alto):
    """
    Calcula el área de un cuadradoo.

    :param ancho: Ancho del cuadrado (float)
    :param alto: Alto del cuadradoo (float)
    :return: Área del cuadrado (float)
    """
    return ancho * alto


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2


def convertir_centimetros_a_metros(centimetros):
    """
    Convierte una medida en metros a centímetros.

    :param centimetros: Medida en centimetros (float)
    :return: Medida en centímetros (float)
    """
    return centimetros * 100


def gestionar_registro(nombre_y_apellido, edad, altura_cm):
    """
    Gestiona la información básica de un registro.

    :param nombre_y_apellido: Nombre y apellido de la persona (string)
    :param edad: Edad de la persona (int)
    :param altura_m: Altura de la persona en metros (float)
    :return: Diccionario con la información del registro
    """
    altura_cm = convertir_centimetros_a_metros(altura_cm)
    return {
        "nombre_y_apellido": nombre_y_apellido,
        "edad": edad,
        "altura_cm": altura_cm
    }

# Cálculo del área del cuadrado
ancho = float(input("Introduce el ancho del cuadrado: "))
alto = float(input("Introduce la altura del cuadrado: "))
area_cuadrado = calcular_area_cuadrado(ancho, alto)
print(f"El área del cuadrado es: {area_cuadrado}")

# Verifica si el área es mayor que un valor umbral (por ejemplo, 60)
umbral = 60  # integer
es_area_grande = area_cuadrado > umbral  # boolean

# Muestra un mensaje adicional basado en la comparación
if es_area_grande:
    print("El área del cuadrado es grande.")
else:
    print("El área del cuadrado es pequeña.")

# Cálculo del área del círculo
radio = float(input("Introduce el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print(f"El área del círculo es: {area_circulo}")

# Gestión de información básica de un registro
nombre = input("Introduce tu nombre y apellido: ")
edad = int(input("Introduce tu edad: "))
altura_cm = float(input("Introduce tu altura en centimetros: "))
registro = gestionar_registro(nombre, edad, altura_cm)
print(f"Información del registro: {registro}")