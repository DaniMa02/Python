#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena= input("Introduce una cadena: ")
subCadena= input("Introduce una subcadena: ")

if subCadena in cadena:
    print ("Tu subcadena " +subCadena+ " está en " +cadena)
else:
    print ("Tu subcadena " +subCadena+ " no está en " +cadena)
