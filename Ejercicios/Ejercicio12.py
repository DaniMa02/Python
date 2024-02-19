def leer_notas():

    notas = []

    for i in range(5):
        while True:
            nota= float(input("Escribe la nota número " +str(i+1)+": \n"))
            if 0<= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10. Intentalo de nuevo")
    return notas


def calcular_media(notas):
    return sum(notas)/len(notas)
def calcular_max(notas):
    return max(notas)
def calcular_min(notas):
    return min(notas)

notas = leer_notas()

nota_max = calcular_max(notas)
nota_min = calcular_min(notas)
media = calcular_media(notas)

print("Notas introducidas "+str(notas))
print("Media: "+str(media))
print("Nota máxima: "+str(nota_max))
print("Nota mínima: "+str(nota_min))