# Programa Tradicional para calcular el promedio semanal del clima

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"Promedio semanal: {promedio:.2f} °C")

main()
