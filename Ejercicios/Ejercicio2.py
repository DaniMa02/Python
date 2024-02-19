# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena= input("Introduzca una cadena: ")
subcadena= input("Introduzca una subcadena: ")

if cadena.startswith(subcadena):
    print("Tu cadena comienza igual que tu subcadena.")
else:
    print("Tu cadena y subcadena no coinciden.")