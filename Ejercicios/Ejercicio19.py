def calcular_temperatura_media(temp_max, temp_min, dias_anteriores):
    suma_anteriores = sum(dias_anteriores)
    return (temp_max + temp_min + suma_anteriores) / (2 + len(dias_anteriores))

def main():
    num_dias = int(input("Ingrese el número de días: "))
    temperaturas_anteriores = []
    for dia in range(1, num_dias + 1):
        temp_max = float(input(f"Ingrese la temperatura máxima del día {dia}: "))
        temp_min = float(input(f"Ingrese la temperatura mínima del día {dia}: "))
        temp_media = calcular_temperatura_media(temp_max, temp_min, temperaturas_anteriores)
        temperaturas_anteriores.append(temp_media)
        print(f"La temperatura media acumulada hasta el día {dia} es: {temp_media} grados Celsius")


main()
