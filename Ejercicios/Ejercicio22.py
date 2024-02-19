import math

radio = float(input("Ingrese el radio de la circunferencia: "))

def calcularAreaPerimetroCircunferencia(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro


area, perimetro = calcularAreaPerimetroCircunferencia(radio)

print(f"El área de la circunferencia es: {area}")
print(f"El perímetro de la circunferencia es: {perimetro}")
