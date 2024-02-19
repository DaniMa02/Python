def EscribirCentrado(texto):
    longitud = len(texto)
    espacios = 40 - longitud // 2
    print('=' * 80)
    print(' ' * espacios + texto)
    print('=' * 80)

texto = input("Escribe lo que quieras: ")
EscribirCentrado(texto)