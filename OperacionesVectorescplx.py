import sys
import numpy as np
#Juan Sebastian Buitrago Piñeros
#Operaciones Vectores Complejos
def suma_vectores(vectorA, vectorB):
    """
    Adición de vectores complejos
    """
    long_vectorA, long_vectorB = len(vectorA), len(vectorB)
    if long_vectorA == long_vectorB:
        N_vector1 = np.array(vectorA, dtype=complex)
        N_vector2 = np.array(vectorB, dtype=complex)
        result = N_vector1 + N_vector2
        return str(result)
    else:
        sys.exit("Error, no tienen la misma longuitud")

def inverso_vectores(vectorA):
    """
    Inverso (aditivo) de un vector complejos.
    """
    vectorA = -vectorA
    return vectorA

def multiplicacion_vectores(vectorA, escalar):
    """
    Multiplicación de un escalar por un vector complejo.
    """
    result = vectorA * escalar
    return result

def adicion_matriz_cplx(matriz1, matriz2):
    """
    Adición de matrices complejas.
    """
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No son de dimensiones iguales las matricez, por lo tanto, no se puede hacer la adición")
        sys.exit()
    result = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            cplx_suma = matriz1[i][j] + matriz2[i][j]
            fila.append(cplx_suma)
        result.append(fila)
    return result

def inverso_matriz_cplx(matriz):
    """
    Inversa (aditiva) de una matriz compleja.
    """
    result = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            inverso_adit = -matriz[i][j]
            fila.append(inverso_adit)
        result.append(fila)
    return result

def multiplicacion_matricez_cplx(escalar, matriz):
    """
    Multiplicación de un escalar por una matriz compleja.
    """
    result = [[escalar * element for element in fila] for fila in matriz]
    """ #Adicionales
    La linea de arriba quiere decir esto...
    result = []
    for fila in matriz:
        Nfila = []
        for element in fila:
            Nelement = escalar * element
            Nfila.append(Nelement)
        result.append(Nfila)
    """
    return result

def transpuesta_matriz(matrix_o_vector):
    """
    Transpuesta de una matriz/vector
    """
    NFila = len(matrix_o_vector)
    Ncolum = len(matrix_o_vector[0])
    result = []
    for j in range(Ncolum):
        trans_fila = []
        for i in range(NFila):
            trans_fila.append(matrix_o_vector[i][j])
        result.append(trans_fila)
    return result

def conjugar_matriz(matrix):
    """
    Conjuga una matriz
    """
    conjugar = [[complex(x.real, -x.imag) for x in fila] for fila in matrix]
    """ #Resumen de la linea de arriba
    conjugar = []
    for fila in matrix:
        conjugar_fila = []
        for element in fila:
            conjugar_fila.append(complex(element.real, -element.imag))
        conjugar.append(conjugar_fila)
    return conjugar
    """
    return conjugar

def conjugar_vector(vector):
    """
    Conjunga un vector dado
    """
    conjugar = [complex(x.real, -x.imag) for x in vector]
    return conjugar

def adjunta_matriz(matriz):
    """
    Adjunta (daga) de una matriz/vector
    """
    if len(matriz[0]) == 1:  # Si es un vector
        return [[elemento.conjugate()] for elemento in matriz]
    elif len(matriz[0]) > 1:  # Si es una matriz
        return [[elemento.conjugate() for elemento in fila] for fila in matriz]
    else:
        print("La entrada debe ser matriz o vector")
        sys.exit()

def Produc_dos_matriz(A, B):
    """
    Producto de dos matrices (de tamaños compatibles)
    """
    if len(A[0]) != len(B):
        print("Las matrices no son compatibles para la multiplicación.")
        sys.exit()
    fila_A = len(A)
    col_B = len(B[0])
    resultado = [[0] * col_B for _ in range(fila_A)]
    for i in range(fila_A):
        for j in range(col_B):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            resultado[i][j] = suma
    return resultado
