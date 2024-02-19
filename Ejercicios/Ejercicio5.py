# Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

cadena= input("Escribe el nombre: ")

def obtener_iniciales(nombre_completo):
    #Dividimos el nombre completo en palabras
    palabras = nombre_completo.split()

    iniciales =""
    for palabra in palabras:
        iniciales += palabra[0]
    return iniciales.upper()

print("Las iniciales del nombre: "+cadena+ " son: \n"+ obtener_iniciales(cadena))