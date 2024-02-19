def TimeToSec():
    horas = int(input("Introduce las horas que quieres convertir a segundos: "))
    minutos = int(input("Introduce las minutos que quieres convertir a segundos: "))
    segundos = int(input("Introduce las segundos que quieres convertir a segundos: "))

    totalSegundos = horas * 3600 + minutos * 60 + segundos
    print("La cantidad de tiempo introducida es igual a " +str(totalSegundos)+ " segundos.")


def SecToTime():
    segundos = int(input("Introduce el tiempo en segundos: "))
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60


    print("El tiempo en segundos introducido es equivalente a: " +str(horas)+ " hora(s), " +str(minutos)+ " minuto(s) y " +str(segundos)+ " segundo(s).")

def main():
    while True:
        print("\nMenú:")
        print("1. Convertir a segundos")
        print("2. Convertir a horas, minutos y segundos")
        print("3. Salir del programa")
        opcion = input("Introduzca su opción: ")
        if opcion == "1":
            TimeToSec()
        elif opcion == "2":
            SecToTime()
        elif opcion == "3":
            print("Has salido del programa")
            break
        else:
            print("La opción no existe. Introduzca 1, 2 o 3.")

main()