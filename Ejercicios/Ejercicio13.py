# Creamos una matriz bidimensional para almacenar los nombres y edades de los alumnos
alumnos = []

# Solicitamos al usuario que ingrese nombre y edad de los alumnos
print("Introduce el nombre y la edad de cada alumno. Ingresa * como nombre para terminar.")

while True:
    nombre = input("Nombre del alumno: ")
    
    # Verificamos si se ingresa * como nombre para terminar la entrada de datos
    if nombre == '*':
        break
    
    edad = int(input("Edad del alumno: "))
    
    # Guardamos el nombre y la edad del alumno en la matriz de alumnos
    alumnos.append([nombre, edad])

# Mostramos los alumnos mayores de edad
print("\nAlumnos mayores de edad:")
for alumno in alumnos:
    if alumno[1] >= 18:
        print(alumno[0])

# Buscamos los alumnos mayores (los que tienen más edad)
mayor_edad = max(alumnos, key=lambda x: x[1])

print("\nAlumno(s) mayor(es):")
for alumno in alumnos:
    if alumno[1] == mayor_edad[1]:
        print(alumno[0])
