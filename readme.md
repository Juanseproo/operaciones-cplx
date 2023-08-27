# Libreria de Operaciones de Números Complejos

Este repositorio contiene pruebas unitarias para un módulo llamado `OperacionesVectorescplx`, el cual proporciona operaciones relacionadas con números complejos. Las pruebas están escritas utilizando el marco de trabajo `unittest` de Python.

### Autor
Juan Sebastian Buitrago Piñeros

## Instalación

1. Clona el repositorio en tu máquina local:
git clone https://github.com/tu-nombre-de-usuario/pruebas-numeros-complejos.git

2. Cambia al directorio del proyecto:

3. Asegúrate de tener Python instalado. El código está escrito en Python 3.

## Ejecución de las Pruebas

Para ejecutar las pruebas unitarias, sigue estos pasos:

1. Abre una terminal o línea de comandos.

2. Navega al directorio del proyecto si aún no estás allí.

3. Ejecuta el siguiente comando:

Esto ejecutará el conjunto de pruebas y mostrará los resultados.

## Casos de Prueba

La clase de pruebas unitarias `TestCplxOperatins` contiene los siguientes métodos de prueba:

### `test_suma_vectores()`

Adición de vectores complejos

### `test_inverso_vectores()`

Inverso (aditivo) de un vector complejos.

### `test_multiplicacion_vectores()`

Multiplicación de un escalar por un vector complejo.

### `test_adicion_matriz_cplx()`

Adición de matrices complejas.

### `test_inverso_matriz_cplx()`

Inversa (aditiva) de una matriz compleja.

### `test_multiplicacion_matricez_cplx()`

Multiplicación de un escalar por una matriz compleja.

### `test_transpuesta_matriz()`

Transpuesta de una matriz/vector

### `test_conjugar_matriz()`

Conjuga una matriz

### `test_conjugar_vector()`

Conjuga un vector

### `test_adjunta_matriz()`

Adjunta (daga) de una matriz/vector

### `test_Produc_dos_matriz()`

Producto de dos matrices (de tamaños compatibles)

Cada método de prueba contiene afirmaciones para comparar la salida real de las funciones probadas con los resultados esperados. Si las afirmaciones pasan, la prueba es exitosa; de lo contrario, falla.

### Licencia

Este proyecto está autorizado bajo la licencia MIT; consulte el archivo LICENSE.md para obtener más información.