#Calcular factorial
numero_ingresado = int(input("Introduzca el número: "))
def calcular_factorial(numero):
    factorial = 1
    i = 1

    while i <= numero:
        factorial *= i
        i += 1

    return factorial

resultado= calcular_factorial(numero_ingresado)
print("El factorial de "+str(numero_ingresado)+ " es " + str(resultado))