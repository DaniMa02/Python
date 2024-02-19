# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

listavalores= [random.randint(1, 10) for _ in range(10)]

for valor in listavalores:
    cuadrado = valor ** 2
    cubo = valor ** 3
    print(valor,cuadrado,cubo)

