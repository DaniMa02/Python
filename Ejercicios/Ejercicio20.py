texto_original = input("Ingrese un texto: ")

def ConvertirEspaciado(texto):
    nuevo_texto = ""
    for letra in texto:
        nuevo_texto += letra + " "
    return nuevo_texto


texto_convertido = ConvertirEspaciado(texto_original)

print(texto_convertido)

