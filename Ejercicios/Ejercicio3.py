# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena = input ("Escribe una cadena: ")

caracter= input ("Escribe un caracter: ")

if (caracter.isalpha()):
    print (cadena.count(caracter))
else:
    print ("No has introducido un caracter")

