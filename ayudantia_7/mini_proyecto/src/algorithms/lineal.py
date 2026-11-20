from src.algorithms.base import Buscador


class BusquedaLineal(Buscador):
    nombre = "Lineal"
    complejidad = "O(n)"

    def _ejecutar(self, datos, objetivo, recorridos):
        comparaciones = 0
        for i, valor in enumerate(datos):
            if recorridos is not None:
                recorridos.append(i)
            comparaciones += 1
            if valor == objetivo:
                return i, comparaciones
        return None, comparaciones
