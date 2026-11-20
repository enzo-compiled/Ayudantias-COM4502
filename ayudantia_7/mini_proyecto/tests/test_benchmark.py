import unittest

from src.algorithms import ALGORITMOS
from src.experiments.benchmark import grafico_png, medir


class TestExperimentos(unittest.TestCase):
    def test_medir_forma(self):
        tiempos = medir(tamanos=[10, 100], repeticiones=2)
        self.assertEqual(set(tiempos), set(ALGORITMOS))
        for ts in tiempos.values():
            self.assertEqual(len(ts), 2)

    def test_grafico_es_png(self):
        png = grafico_png(tamanos=[10, 100], tiempos={n: [1e-6, 2e-6] for n in ALGORITMOS})
        self.assertTrue(png.startswith(b"\x89PNG"))


if __name__ == "__main__":
    unittest.main()
