from collections import Counter
import re

def contar_combinaciones(texto, n):
    """Cuenta combinaciones de longitud n en el texto."""
    return Counter(texto[i:i+n] for i in range(len(texto) - n + 1))

def procesar_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Limpieza del texto: incluir letras y la ñ, convertir a minúsculas
    texto_limpio = re.sub(r'[^a-zA-ZñÑ]', '', contenido).lower()

    resultados = {}
    for n in range(1, 5):
        combinaciones = contar_combinaciones(texto_limpio, n)
        mas_frecuentes = combinaciones.most_common(26)
        resultados[n] = mas_frecuentes

    return resultados

def guardar_resultados(resultados, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        for n in range(1, 5):
            f.write(f"Top 26 combinaciones de {n} letra(s):\n")
            for combinacion, frecuencia in resultados[n]:
                f.write(f"{combinacion}: {frecuencia}\n")
            f.write("\n")

# Uso principal
entrada = 'texto_cifrado.txt'         # Reemplaza con el nombre del archivo que deseas analizar
salida = 'frecuencias.txt'      # Nombre del archivo de salida

resultados = procesar_archivo(entrada)
guardar_resultados(resultados, salida)

print("Frecuencias guardadas en 'frecuencias.txt'.")
