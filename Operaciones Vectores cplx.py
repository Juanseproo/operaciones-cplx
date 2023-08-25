import sys
import numpy as np
vectorA = [1 + 2j, 3 - 1j, 0 + 4j]
vectorB = [0 - 1j, 2 + 2j, 1 - 3j]
def imprimir_matriz(matriz):
    """
    Imprime la matriz correspodiente de una manera mas visible
    """
    for i in range(len(matriz)):
        elementos_como_cadenas = [str(elemento) for elemento in matriz[i]]
        resultado = " ".join(elementos_como_cadenas)
        print(resultado)
    sys.exit("Hecho")

def suma_vectores(vectorA,vectorB):
    """
    Adición de vectores complejos
    """
    long_vectorA, long_vectorB = len(vectorA), len(vectorB)
    if long_vectorA == long_vectorB:
        N_vector1 = np.array(vectorA, dtype=complex)
        N_vector2 = np.array(vectorB, dtype=complex)
        result = N_vector1 + N_vector2
        return result
        
    else:
        sys.exit("Error, no tienen la misma longuitud")
print(suma_vectores(vectorA, vectorB))