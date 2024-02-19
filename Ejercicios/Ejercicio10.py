#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena= input ("Escribe tu cadena: \n")
cadena= cadena.replace(" ","").lower()
cadena_reversed=cadena[::-1]
if(cadena == cadena_reversed):
    print("Has escrito una cadena palíndroma")
else:
    print("No es una cadena palíndroma")