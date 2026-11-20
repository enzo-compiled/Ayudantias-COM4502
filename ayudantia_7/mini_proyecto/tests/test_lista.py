import unittest

from src.models.lista import ListaNumeros


class TestListaNumeros(unittest.TestCase):
    def test_ordena_al_crear(self):
        self.assertEqual(ListaNumeros([5, 1, 3]).datos, [1, 3, 5])

    def test_desde_texto(self):
        self.assertEqual(ListaNumeros.desde_texto("3, 1, 2").datos, [1, 2, 3])

    def test_texto_invalido(self):
        with self.assertRaises(ValueError):
            ListaNumeros.desde_texto("1, a, 3")

    def test_texto_vacio(self):
        with self.assertRaises(ValueError):
            ListaNumeros.desde_texto("  ")

    def test_separador_punto_y_coma_y_negativos(self):
        self.assertEqual(ListaNumeros.desde_texto("3; -1, 2").datos, [-1, 2, 3])

    def test_aleatoria_distinta_y_ordenada(self):
        lista = ListaNumeros.aleatoria(30, maximo=50, semilla=1)
        self.assertEqual(len(lista), 30)
        self.assertEqual(lista.datos, sorted(set(lista.datos)))

    def test_aleatoria_invalida(self):
        with self.assertRaises(ValueError):
            ListaNumeros.aleatoria(0)
        with self.assertRaises(ValueError):
            ListaNumeros.aleatoria(11, maximo=9)


if __name__ == "__main__":
    unittest.main()
