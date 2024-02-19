dividendo = int(input("Escribe el dividendo: "))
divisor = int(input("Escribe el divisor: "))

def EsMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

if EsMultiplo(dividendo, divisor):
    print(str(divisor) + " es múltiplo de " + str(dividendo))
else:
    print(str(divisor) + " no es múltiplo de " + str(dividendo))
