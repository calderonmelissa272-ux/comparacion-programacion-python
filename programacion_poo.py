# Programa POO para calcular el promedio semanal del clima

class ClimaSemanal:
    def _init_(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)

clima = ClimaSemanal()
clima.ingresar_temperaturas()
print(f"Promedio semanal: {clima.calcular_promedio():.2f} °C")
