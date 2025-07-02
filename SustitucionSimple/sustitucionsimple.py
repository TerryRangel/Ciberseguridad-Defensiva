from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import os
import string

# Cambiar directorio de trabajo al del script para leer archivos relativos
os.chdir(os.path.dirname(__file__))

# Funciones auxiliares
def ngramas(texto, n):
    """Divide el texto en ngramas eliminando espacios."""
    texto = texto.replace(" ", "")
    return [texto[i:i+n] for i in range(len(texto)-n+1)]

def frec_ngramas(texto, n):
    """Calcula las frecuencias de los ngramas de un texto."""
    ng = ngramas(texto, n)
    frecuencias = Counter(ng)
    return pd.DataFrame(frecuencias.most_common(), columns=['letra','frecuencia'])

def leer_frecuencias(archivo):
    """Lee un fichero con las frecuencias de los ngramas en español."""
    return pd.read_csv(archivo, sep=" ", names=["letra", "frecuencia"])

def leer_texto_cifrado(texto_cifrado, n):
    """Lee el texto cifrado y calcula las frecuencias de los ngramas."""
    with open(texto_cifrado, 'r', encoding='utf-8') as f:
        texto = f.read().strip()
    return frec_ngramas(texto, n)

# Alfabeto permutado (clave)
alfabeto_permutado = {
     'a': 'u', 'b': 'q', 'c': 't', 'd': 'f', 'e': 'v',
     'f': 'n', 'g': 'r', 'h': 'a', 'i': 'x', 'j': 'b',
     'k': 'd', 'l': 'e', 'm': 'y', 'n': 'j', 'o': 'p',
     'p': 'c', 'q': 'h', 'r': 'z', 's': 'k', 't': 'i',
     'u': 'l', 'v': 's', 'w': 'g', 'x': 'o', 'y': 'w',
     'z': 'm'
}

# Algoritmo de descifrado
def algoritmo_descifrado(texto_cifrado, alfabeto_permutado):
    """Descifra el texto cifrado a partir de la clave de descifrado."""
    texto_plano = ""
    with open(texto_cifrado, 'r', encoding='utf-8') as f:
        texto = f.read()

    for letra in texto:
        if letra.lower() in alfabeto_permutado:
            # Conserva mayúsculas si las hay
            descifrada = alfabeto_permutado[letra.lower()]
            if letra.isupper():
                descifrada = descifrada.upper()
            texto_plano += descifrada
        else:
            texto_plano += letra  # No sustituir caracteres no alfabéticos
    return texto_plano

# --- Inicio del análisis y gráficos ---

if __name__ == "__main__":

    # Monogramas (letras)
    monogramas_es = leer_frecuencias("spanish_monograms.txt")
    monogramas_es.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de monogramas en español")
    plt.xlabel("Letra")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    monogramas_cifrado = leer_texto_cifrado('texto_cifrado.txt', 1)
    monogramas_cifrado.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de monogramas en texto cifrado")
    plt.xlabel("Letra")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    # Bigramas
    bigramas_es = leer_frecuencias("spanish_bigrams.txt")
    bigramas_es.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de bigramas en español")
    plt.xlabel("Bigramas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    bigramas_cifrado = leer_texto_cifrado('texto_cifrado.txt', 2)
    bigramas_cifrado.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de bigramas en texto cifrado")
    plt.xlabel("Bigramas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    # Trigramas
    """
    trigramas_es = leer_frecuencias("spanish_trigrams.txt")
    trigramas_es.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de trigramas en español")
    plt.xlabel("Trigramas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    trigramas_cifrado = leer_texto_cifrado('texto_cifrado.txt', 3)
    trigramas_cifrado.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de trigramas en texto cifrado")
    plt.xlabel("Trigramas")
    plt.ylabel("Frecuencia") 
    plt.tight_layout()
    plt.show()

    # Cuatrigramas
    cuatrigramas_es = leer_frecuencias("spanish_quadgrams.txt")
    cuatrigramas_es.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de cuatrigramas en español")
    plt.xlabel("Cuatrigramas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    cuatrigramas_cifrado = leer_texto_cifrado('texto_cifrado.txt', 4)
    cuatrigramas_cifrado.plot(x='letra', y='frecuencia', kind='bar', legend=False)
    plt.title("Frecuencia de cuatrigramas en texto cifrado")
    plt.xlabel("Cuatrigramas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()
    """

    # Descifrado y salida
    texto_descifrado = algoritmo_descifrado('texto_cifrado.txt', alfabeto_permutado)
    print("Texto descifrado:\n")
    print(texto_descifrado)
