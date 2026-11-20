import unittest

from src.algorithms import ALGORITMOS


class TestBuscadores(unittest.TestCase):
    """Los mismos casos se prueban con TODOS los algoritmos."""

    def por_algoritmo(self, datos, objetivo, indice_esperado):
        for nombre, buscador in ALGORITMOS.items():
            with self.subTest(algoritmo=nombre):
                r = buscador.buscar(datos, objetivo)
                self.assertEqual(r.indice, indice_esperado)
                self.assertEqual(r.encontrado, indice_esperado is not None)

    def test_elemento_en_el_medio(self):
        self.por_algoritmo([1, 3, 5, 7, 9], 5, 2)

    def test_primer_elemento(self):
        self.por_algoritmo([1, 3, 5, 7, 9], 1, 0)

    def test_ultimo_elemento(self):
        self.por_algoritmo([1, 3, 5, 7, 9], 9, 4)

    def test_no_existe(self):
        self.por_algoritmo([1, 3, 5, 7, 9], 4, None)

    def test_lista_vacia(self):
        self.por_algoritmo([], 1, None)

    def test_un_elemento(self):
        self.por_algoritmo([7], 7, 0)
        self.por_algoritmo([7], 3, None)

    def test_binaria_usa_menos_comparaciones(self):
        datos = list(range(1000))
        lineal = ALGORITMOS["Lineal"].buscar(datos, 999)
        binaria = ALGORITMOS["Binaria"].buscar(datos, 999)
        self.assertLess(binaria.comparaciones, lineal.comparaciones)


class TestDetalles(unittest.TestCase):
    def test_negativos_y_duplicados(self):
        datos = [-5, -1, 2, 2, 2, 8]
        for nombre, buscador in ALGORITMOS.items():
            with self.subTest(algoritmo=nombre):
                self.assertEqual(buscador.buscar(datos, -5).indice, 0)
                self.assertEqual(datos[buscador.buscar(datos, 2).indice], 2)
                self.assertFalse(buscador.buscar(datos, 100).encontrado)

    def test_registrar_guarda_recorridos(self):
        datos = [1, 3, 5, 7, 9]
        self.assertEqual(ALGORITMOS["Lineal"].buscar(datos, 5, registrar=True).recorridos, [0, 1, 2])
        self.assertEqual(ALGORITMOS["Binaria"].buscar(datos, 9, registrar=True).recorridos, [2, 3, 4])

    def test_sin_registrar_no_guarda_recorridos(self):
        self.assertEqual(ALGORITMOS["Lineal"].buscar([1, 2, 3], 3).recorridos, [])

    def test_comparaciones_peor_caso(self):
        datos = list(range(1024))
        self.assertEqual(ALGORITMOS["Lineal"].buscar(datos, -1).comparaciones, 1024)
        self.assertLessEqual(ALGORITMOS["Binaria"].buscar(datos, -1).comparaciones, 11)

    def test_resultado_tiene_metadatos(self):
        r = ALGORITMOS["Binaria"].buscar([1, 2, 3], 2)
        self.assertEqual(r.algoritmo, "Binaria")
        self.assertGreaterEqual(r.tiempo, 0)


if __name__ == "__main__":
    unittest.main()
