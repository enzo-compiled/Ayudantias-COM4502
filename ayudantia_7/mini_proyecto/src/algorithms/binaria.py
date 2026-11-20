from src.algorithms.base import Buscador


class BusquedaBinaria(Buscador):
    nombre = "Binaria"
    complejidad = "O(log n)"

    def _ejecutar(self, datos, objetivo, recorridos):
        izq, der = 0, len(datos) - 1
        comparaciones = 0
        while izq <= der:
            medio = (izq + der) // 2
            if recorridos is not None:
                recorridos.append(medio)
            comparaciones += 1
            if datos[medio] == objetivo:
                return medio, comparaciones
            if datos[medio] < objetivo:
                izq = medio + 1
            else:
                der = medio - 1
        return None, comparaciones
