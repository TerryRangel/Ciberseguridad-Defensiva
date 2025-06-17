# Ataques estadisticos: Analisis de frecuencias
## Funciones auxiliares
import os
os.chdir(os.path.dirname(__file__))

def ngramas(texto, n):
    """Divide el texto en ngramas."""
    texto = texto.replace(" ", "")
    return [texto[i:i+n] for i in range(len(texto)-n+1)]
from collections import Counter
import pandas as pd

def frec_ngramas(texto, n):
    """Calcula las frecuencias de los ngramas de un texto."""
    ng = ngramas(texto, n)
    frecuencias = Counter(ng)
    return pd.DataFrame(frecuencias.most_common(), columns=['letra', 'frecuencia'])
def leer_frecuencias(archivo):
    """Lee un fichero con las frecuencias de los ngramas para el idioma Espanol."""
    return pd.read_csv(archivo, sep=" ", names=["letra", "frecuencia"])
def leer_texto_cifrado(texto_cifrado, n):
    """Lee el texto cifrado y calcula las frecuencias de los ngramas."""
    with open(texto_cifrado) as f:
        texto_cifrado = f.readlines()[0]
    return frec_ngramas(texto_cifrado, n)
## Playfair Square

## Analisis Bigramas
bigramas_cifrado = leer_texto_cifrado('texto_cifrado.txt', 2)
bigramas_cifrado.head(10)
bigramas_es = leer_frecuencias("spanish_bigrams.txt")
bigramas_es.head(10)