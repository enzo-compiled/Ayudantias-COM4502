"""Experimentos: mismas instancias para ambos algoritmos"""
import io

import matplotlib
matplotlib.use("Agg")  #genera imágenes sin abrir ventanas
import matplotlib.pyplot as plt
from src.algorithms import ALGORITMOS

TAMANOS = [1_000, 10_000, 100_000, 500_000]
REPETICIONES = 5


def medir(tamanos=TAMANOS, repeticiones=REPETICIONES) -> dict[str, list[float]]:
    """Peor caso: buscar un valor que NO está. Devuelve {algoritmo: [tiempo promedio por tamaño]}."""
    tiempos = {nombre: [] for nombre in ALGORITMOS}
    for n in tamanos:
        datos = list(range(0, 2 * n, 2)) # pares ordenados
        objetivo = 1 # impar: nunca está
        for nombre, buscador in ALGORITMOS.items():
            total = sum(buscador.buscar(datos, objetivo).tiempo for _ in range(repeticiones))
            tiempos[nombre].append(total / repeticiones)
    return tiempos


def grafico_png(tamanos=TAMANOS, tiempos=None) -> bytes:
    """Devuelve el gráfico como bytes PNG."""
    tiempos = tiempos or medir(tamanos)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    for nombre, ts in tiempos.items():
        ax.plot(tamanos, [t * 1e6 for t in ts], marker="o", label=nombre)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tamaño de la lista (n)")
    ax.set_ylabel("Tiempo promedio (µs)")
    ax.set_title("Búsqueda lineal vs binaria (peor caso)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    buffer = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buffer, format="png", dpi=120)
    plt.close(fig)
    return buffer.getvalue()


if __name__ == "__main__":
    # Se puede correr solo: python -m src.experiments.benchmark
    with open("resultados.png", "wb") as f:
        f.write(grafico_png())
    print("Gráfico guardado en resultados.png")
