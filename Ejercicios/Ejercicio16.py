precios_frutas = {
    "manzana": 2,
    "banana": 1.5,
    "naranja": 3,
    "pera": 2.5,
    "uva": 4
}

nombreFruta= input("Introduce una fruta: ")

if nombreFruta in precios_frutas:
    cantidadVendida= float(input("Introduce la cantidad de fruta que se ha vendido: "))

    print(cantidadVendida * precios_frutas.get(nombreFruta))
else:
    print("La fruta no existe.")
