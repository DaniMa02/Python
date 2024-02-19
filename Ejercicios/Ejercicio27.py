def leer_fecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    return dia, mes, año

def dias_del_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if es_bisiesto(año):
            return 29
        else:
            return 28

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def calcular_dia_juliano(dia, mes, año):
    total_dias = dia
    for m in range(1, mes):
        total_dias += dias_del_mes(m, año)
    return total_dias


def main():
    dia, mes, año = leer_fecha()
    dia_juliano = calcular_dia_juliano(dia, mes, año)
    print("El día juliano correspondiente a la fecha ingresada es:", dia_juliano)

main()
