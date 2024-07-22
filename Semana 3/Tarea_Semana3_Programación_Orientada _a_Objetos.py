class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura

    def obtener_dia(self):
        return self.__dia

    def obtener_temperatura(self):
        return self.__temperatura

    def establecer_temperatura(self, temperatura):
        self.__temperatura = temperatura

class PromedioClimaSemanal:
    def __init__(self):
        self.climas_diarios = []

    def agregar_clima_diario(self, clima_diario):
        if isinstance(clima_diario, ClimaDiario):
            self.climas_diarios.append(clima_diario)
        else:
            raise TypeError("Se debe agregar una instancia de ClimaDiario")

    def calcular_promedio_semanal(self):
        if not self.climas_diarios:
            return 0.0
        total_temperatura = sum([clima.obtener_temperatura() for clima in self.climas_diarios]) # Cálcula las temperaturas
        return total_temperatura / len(self.climas_diarios)

# Uso del programa
if __name__ == "__main__":
    print("Programa para calcular el promedio semanal de temperaturas utilizando POO")
    promedio_clima = PromedioClimaSemanal()

    # Ingresar datos para cada día de la semana
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]   # Ingresamos los días de la semana
    for dia in dias:
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura para {dia}: "))   # Solicita la temperatura al usuario
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")  # Manejo de errores para valores que no sean numéricos
        clima_diario = ClimaDiario(dia, temperatura)
        promedio_clima.agregar_clima_diario(clima_diario)

    # Calcular y mostrar el promedio semanal
    promedio_semanal = promedio_clima.calcular_promedio_semanal()
    print(f"El promedio semanal de la temperatura es: {promedio_semanal:.2f}°C")  # Muestra el promedio de temperaturas