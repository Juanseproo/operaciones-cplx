import OperacionesVectorescplx as lc
import unittest
import numpy as np
class TestCplxOperatins(unittest.TestCase):

    def test_suma_vectores(self):
        suma_vectores = lc.suma_vectores([1 + 2j, 3 - 1j, 0 + 4j],[0 - 1j, 2 + 2j, 1 - 3j])
        self.assertAlmostEqual(suma_vectores, "[1.+1.j 5.+1.j 1.+1.j]")
        suma_vectores = lc.suma_vectores([1 + 4j, 3 - 1j, 1 + 4j],[6 + 1j, 3 + 2j, 2 - 3j])
        self.assertAlmostEqual(suma_vectores,"[7.+5.j 6.+1.j 3.+1.j]") 

    def test_inverso_vectores(self):
        inverso_vectores = lc.inverso_vectores((-8 - 4j))
        self.assertAlmostEqual(inverso_vectores,(8+4j))
        inverso_vectores = lc.inverso_vectores((7 + 8j))
        self.assertAlmostEqual(inverso_vectores,(-7-8j))

    def test_multiplicacion_vectores(self):
        multiplicacion_vectores = lc.multiplicacion_vectores(-3 + 4j, 2)
        self.assertAlmostEqual(multiplicacion_vectores,(-6+8j))
        multiplicacion_vectores = lc.multiplicacion_vectores(2 - 5j, 10)
        self.assertAlmostEqual(multiplicacion_vectores,(20-50j))

    def test_adicion_matriz_cplx(self):
        test_adicion_matriz_cplx = lc.adicion_matriz_cplx([[2 + 3j, 1 - 2j], [0 + 1j, -2 + 0j]], [[-1 + 1j, 0 - 2j], [2 + 2j, 3 - 1j]])
        self.assertAlmostEqual(test_adicion_matriz_cplx,[[(1+4j), (1-4j)], [(2+3j), (1-1j)]])
        test_adicion_matriz_cplx = lc.adicion_matriz_cplx([[2.5 + 3.5j, 1.1 - 2j], [0 + 1j, -2 + 0j]], [[-1.5 + 1j, 0 - 2.3j], [2 + 2j, 3 - 1j]])
        self.assertAlmostEqual(test_adicion_matriz_cplx,[[(1+4.5j), (1.1-4.3j)], [(2+3j), (1-1j)]])

    def test_inverso_matriz_cplx(self):
        inverso_matriz_cplx = lc.inverso_matriz_cplx([[2 + 3j, 1 - 2j], [0 + 1j, -2 + 0j]])
        self.assertAlmostEqual(inverso_matriz_cplx,[[(-2-3j), (-1+2j)], [(-0-1j), (2-0j)]])
        inverso_matriz_cplx = lc.inverso_matriz_cplx([[2.6 + 3.4j, 1.1 - 2j], [0.9 + 1.5j, -2.2 + 0j]])
        self.assertAlmostEqual(inverso_matriz_cplx,[[(-2.6-3.4j), (-1.1+2j)], [(-0.9-1.5j), (2.2-0j)]])

    def test_multiplicacion_matricez_cplx(self):
        multiplicacion_matricez_cplx = lc.multiplicacion_matricez_cplx(2, [[2+3j, 1-2j, 0+1j], [-1j, 0+2j, 3-1j], [4-2j, 1j, -2-2j]])
        self.assertAlmostEqual(multiplicacion_matricez_cplx,[[(4+6j), (2-4j), 2j], [-2j, 4j, (6-2j)], [(8-4j), 2j, (-4-4j)]])
        multiplicacion_matricez_cplx = lc.multiplicacion_matricez_cplx(3,[[2.5+3.1j, 1-2.9j, 0.5+1j], [-1.1j, 0.5+2.6j, 3.5-1j], [4-2j, 1j, -2-2j]])
        self.assertAlmostEqual(multiplicacion_matricez_cplx,[[(7.5+9.3j), (3-8.7j), (1.5+3j)], [-3.3000000000000003j, (1.5+7.800000000000001j), (10.5-3j)], [(12-6j), 3j, (-6-6j)]])

    def test_transpuesta_matriz(self):
        transpuesta_matriz = lc.transpuesta_matriz([[2+3j, 1-2j, 0+1j],[-1j, 0+2j, 3-1j],[4-2j, 1j, -2-2j]])
        self.assertAlmostEqual(transpuesta_matriz,[[(2+3j), (-0-1j), (4-2j)], [(1-2j), 2j, 1j], [1j, (3-1j), (-2-2j)]])
        transpuesta_matriz = lc.transpuesta_matriz([[2+3j, 1-2j, 0+1j]])
        self.assertAlmostEqual(transpuesta_matriz,[[(2+3j)], [(1-2j)], [1j]])

    def test_conjugar_matriz(self):
        conjugar_matriz = lc.conjugar_matriz([[1+2j, 3-4j], [5+6j, 7-8j]])
        self.assertAlmostEqual(conjugar_matriz,[[(1-2j), (3+4j)], [(5-6j), (7+8j)]])
        conjugar_matriz = lc.conjugar_matriz([[1.5+2.5j, 3.4-4.7j], [5.4+6j, 7.9-8j]])
        self.assertAlmostEqual(conjugar_matriz,[[(1.5-2.5j), (3.4+4.7j)], [(5.4-6j), (7.9+8j)]])

    def test_conjugar_vector(self):
        conjugar_vector = lc.conjugar_vector([1+2j, 3-4j, 5+6j])
        self.assertAlmostEqual(conjugar_vector,[(1-2j), (3+4j), (5-6j)])
        conjugar_vector = lc.conjugar_vector([1.1+2j, 3-4.9j, 5+6.5j])
        self.assertAlmostEqual(conjugar_vector,[(1.1-2j), (3+4.9j), (5-6.5j)])

    def test_adjunta_matriz(self):
        adjunta_matriz = lc.adjunta_matriz([[1+2j, 3-1j], [0, 5]])
        self.assertAlmostEqual(adjunta_matriz,[[(1-2j), (3+1j)], [0, 5]])
        adjunta_matriz = lc.adjunta_matriz([[1.5+2.6j, 3.8-1j], [0.4, 5]])
        self.assertAlmostEqual(adjunta_matriz,[[(1.5-2.6j), (3.8+1j)], [0.4, 5]])

    def test_Produc_dos_matriz(self):
        Produc_dos_matriz = lc.Produc_dos_matriz([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
        self.assertAlmostEqual(Produc_dos_matriz,[[58, 64], [139, 154]])
        Produc_dos_matriz = lc.Produc_dos_matriz([[1.8, 2.9, 3.5], [44, 5, 6]], [[7, 8.9], [9, 10], [11, 12]])
        self.assertAlmostEqual(Produc_dos_matriz,[[77.19999999999999, 87.02], [419, 513.6]])


if __name__ == "__main__":
    unittest.main()
