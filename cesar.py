def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo
        else:
            resultado += caracter
    return resultado

texto_usuario = input("Introduce un texto: ")
print("\nResultados del cifrado con desplazamientos de 1 a 26:\n")

for i in range(1, 27):
    texto_cifrado = cifrado_cesar(texto_usuario, i)
    print(f"Desplazamiento {i}: {texto_cifrado}")
