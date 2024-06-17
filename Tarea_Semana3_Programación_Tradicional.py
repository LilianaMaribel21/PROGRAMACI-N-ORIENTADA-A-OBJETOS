# Función para ingresar datos diarios (temperaturas)

def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] # Ingresamos los días de la semana

    for dia in dias_semana:
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))   # Solicita la temperatura al usuario
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")    # Manejo de errores para valores que no sean numéricos
        temperaturas.append(temperatura)

    return temperaturas


def calcular_promedio_semanal(temperaturas):
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

# Imprimir y calcular el promedio semanal
def main():
    print("Programa para calcular el promedio semanal de temperaturas utilizando Programación Tradicional\n")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)

    print("\nLas temperaturas ingresadas fueron:", temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")   # Muestra el promedio de temperaturas


if __name__ == "__main__":
    main()