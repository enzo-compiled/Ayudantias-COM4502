"""define QUÉ hace un buscador; cada subclase define CÓMO."""
import time
from abc import ABC, abstractmethod

from src.models.resultado import Resultado


class Buscador(ABC):
    nombre: str = ""
    complejidad: str = ""

    def buscar(self, datos: list[int], objetivo: int, registrar: bool = False) -> Resultado:
        """Mide el tiempo y delega la búsqueda real en _ejecutar.

        registrar=True guarda los índices visitados (para la UI);
        en los experimentos va en False para no distorsionar los tiempos.
        """
        recorridos: list[int] = []
        inicio = time.perf_counter()
        indice, comparaciones = self._ejecutar(datos, objetivo, recorridos if registrar else None)
        tiempo = time.perf_counter() - inicio
        return Resultado(self.nombre, indice is not None, indice, comparaciones, tiempo, recorridos)

    @abstractmethod
    def _ejecutar(self, datos: list[int], objetivo: int, recorridos: list[int] | None):
        """Devuelve (indice | None, comparaciones)."""
