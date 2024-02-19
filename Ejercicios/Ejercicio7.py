#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena= input("Introduce una cadena: ")

letraASustituir= input("Introduce la letra que quieres sustituir: ")

letraParaSustituir= input("Introducir la letra por la que quieres sustituirla: ")

cadenasustituida= cadena.replace(letraASustituir,letraParaSustituir)

print(cadenasustituida)