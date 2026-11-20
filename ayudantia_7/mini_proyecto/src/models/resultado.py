"""Objeto que viaja desde los algoritmos hacia la UI y los experimentos."""
from dataclasses import dataclass, field


# @dataclass genera solo el __init__: Resultado("Binaria", True, 2, 3, 0.0001)
@dataclass
class Resultado:
    #Cada línea es "nombre: tipo" (el tipo solo documenta, Python no lo obliga)
    algoritmo: str  # nombre del algoritmo, ej. "Binaria"
    encontrado: bool # True si el valor estaba en la lista
    indice: int | None # posición del objetivo; None si no está ("int | None" = entero o None)
    comparaciones: int  # cuántas veces se comparó con el objetivo
    tiempo: float   # segundos que tardó la búsqueda
    # default_factory=list crea una lista vacía nueva por objeto (un "= []" se compartiría entre todos)
    recorridos: list[int] = field(default_factory=list)  # índices visitados (solo si registrar=True)
