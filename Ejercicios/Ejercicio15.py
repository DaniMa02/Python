miCadena = input("Introduce una cadena:\n")

diccionario = {}

for i in miCadena:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1

for letra, cantidad in diccionario.items():
    print("La letra {letra} aparece {cantidad} veces.")
