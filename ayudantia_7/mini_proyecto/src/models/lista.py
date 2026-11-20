"""Modelo del problema: una lista de números siempre ordenada."""
import random


class ListaNumeros:
    def __init__(self, datos: list[int]):
        # Ordenamos al crear: la búsqueda binaria lo exige, la lineal no, pero por consistencia y simplicidad lo hacemos siempre.
        self.datos: list[int] = sorted(datos)

    @classmethod
    def desde_texto(cls, texto: str) -> "ListaNumeros":
        """Crea la lista desde '3, 8, 15'. Lanza ValueError si el texto es inválido."""
        partes = [p.strip() for p in texto.replace(";", ",").split(",") if p.strip()]
        if not partes:
            raise ValueError("La lista no puede estar vacía.")
        try:
            return cls([int(p) for p in partes])
        except ValueError:
            raise ValueError("Solo se permiten números enteros separados por comas.")

    @classmethod
    def aleatoria(cls, cantidad: int, maximo: int = 100, semilla: int | None = None) -> "ListaNumeros":
        """Lista de `cantidad` enteros distintos en [0, maximo]. Lanza ValueError si no caben."""
        if cantidad < 1:
            raise ValueError("La cantidad debe ser al menos 1.")
        if cantidad > maximo + 1:
            raise ValueError(f"No se pueden generar {cantidad} números distintos entre 0 y {maximo}.")
        return cls(random.Random(semilla).sample(range(maximo + 1), cantidad))

    def __len__(self) -> int:
        return len(self.datos)
