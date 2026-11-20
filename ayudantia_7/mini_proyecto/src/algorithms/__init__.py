from src.algorithms.binaria import BusquedaBinaria
from src.algorithms.lineal import BusquedaLineal

# La UI y los experimentos usan este diccionario: agregar un algoritmo = agregar una línea.
ALGORITMOS = {a.nombre: a for a in (BusquedaLineal(), BusquedaBinaria())}
