#Maximo y minimo

numerosTotales = int(input("Introduce los números que quieras comparar: \n"))

def calcularMaxMin(numerosTotales):
    numeros = []

    for i in range(1,numerosTotales +1):
        pedirNumero = float(input("Introduce numeros mostro: \n"))
        numeros.append(pedirNumero)

    numeroMaximo = max(numeros)
    numeroMinimo = min(numeros)
    print("El número máximo es: " +str(numeroMaximo)+" y el número mínimo es: " + str(numeroMinimo))
calcularMaxMin(numerosTotales)