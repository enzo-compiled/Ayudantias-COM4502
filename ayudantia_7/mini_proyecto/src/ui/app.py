"""Interfaz en flet. No contiene lógica de búsqueda: solo llama a src.algorithms."""
import asyncio

import flet as ft

from src.algorithms import ALGORITMOS
from src.experiments.benchmark import grafico_png
from src.models.lista import ListaNumeros

GRIS, AMARILLO, VERDE = ft.Colors.GREY_300, ft.Colors.AMBER_300, ft.Colors.GREEN_400
AMBOS = "Ambos"
MAX_CELDAS = 200  # evita congelar la UI con listas enormes


def _celda(valor: int, indice: int, color: str) -> ft.Control:
    return ft.Container(
        content=ft.Text(str(valor), color=ft.Colors.BLACK_87),
        padding=ft.Padding.symmetric(horizontal=10, vertical=8),
        border_radius=6, bgcolor=color, tooltip=f"índice {indice}",
    )


def _leyenda(color: str, texto: str) -> ft.Control:
    return ft.Row([ft.Container(width=14, height=14, bgcolor=color, border_radius=3), ft.Text(texto, size=12)],
                  spacing=6)


def _tarjeta(buscador, lista: ListaNumeros, r) -> ft.Control:
    visitados = set(r.recorridos)
    celdas = [
        _celda(v, i, VERDE if i == r.indice else AMARILLO if i in visitados else GRIS)
        for i, v in enumerate(lista.datos[:MAX_CELDAS])
    ]
    estado = f"encontrado en el índice {r.indice}" if r.encontrado else "no encontrado"
    icono = ft.Icon(ft.Icons.CHECK_CIRCLE if r.encontrado else ft.Icons.CANCEL,
                    color=ft.Colors.GREEN if r.encontrado else ft.Colors.RED)
    contenido = [
        ft.Row([icono, ft.Text(f"{r.algoritmo} · {buscador.complejidad}", weight=ft.FontWeight.BOLD, size=16)]),
        ft.Text(f"{estado} | {r.comparaciones} comparaciones | {r.tiempo * 1e6:.1f} µs"),
        ft.Row(celdas, wrap=True, spacing=6, run_spacing=6),
    ]
    if len(lista) > MAX_CELDAS:
        contenido.append(ft.Text(f"Mostrando los primeros {MAX_CELDAS} de {len(lista)} elementos.",
                                 size=12, italic=True))
    return ft.Card(content=ft.Container(ft.Column(contenido, spacing=10), padding=16))


def main(page: ft.Page):
    page.title = "Búsqueda lineal vs binaria"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 24

    entrada_lista = ft.TextField(label="Lista de números", value="2, 5, 8, 12, 16, 23, 38, 56, 72, 91",
                                 expand=True)
    entrada_objetivo = ft.TextField(label="Valor a buscar", value="23", width=150)
    entrada_cantidad = ft.TextField(label="Cantidad", value="20", width=110)
    selector = ft.Dropdown(
        label="Algoritmo", value=AMBOS, width=170,
        options=[ft.DropdownOption(AMBOS)] + [ft.DropdownOption(nombre) for nombre in ALGORITMOS],
    )
    mensaje = ft.Text()
    resultados = ft.Column(spacing=12)
    grafico = ft.Container()
    progreso = ft.ProgressRing(visible=False, width=22, height=22)

    def error(texto: str):
        mensaje.value, mensaje.color = f"Error: {texto}", ft.Colors.RED
        resultados.controls.clear()
        page.update()

    def entero(campo: ft.TextField, nombre: str) -> int:
        try:
            return int(campo.value)
        except ValueError:
            raise ValueError(f"{nombre} debe ser un número entero.")

    def buscar(e):
        try:
            lista = ListaNumeros.desde_texto(entrada_lista.value)
            objetivo = entero(entrada_objetivo, "El valor a buscar")
        except ValueError as ex:
            error(str(ex))
            return

        nombres = list(ALGORITMOS) if selector.value == AMBOS else [selector.value]
        resultados.controls = [
            _tarjeta(ALGORITMOS[n], lista, ALGORITMOS[n].buscar(lista.datos, objetivo, registrar=True))
            for n in nombres
        ]
        resultados.controls.append(ft.Row(
            [_leyenda(VERDE, "encontrado"), _leyenda(AMARILLO, "visitado"), _leyenda(GRIS, "no visitado")],
            spacing=16))
        mensaje.color = None
        mensaje.value = f"Lista ordenada de {len(lista)} elementos."
        page.update()

    def generar(e):
        try:
            lista = ListaNumeros.aleatoria(entero(entrada_cantidad, "La cantidad"), maximo=999)
        except ValueError as ex:
            error(str(ex))
            return
        entrada_lista.value = ", ".join(map(str, lista.datos))
        entrada_objetivo.value = str(lista.datos[len(lista) // 2])
        buscar(e)

    async def experimento(e):
        boton_exp.disabled, progreso.visible = True, True
        mensaje.color, mensaje.value = None, "Midiendo..."
        page.update()
        png = await asyncio.to_thread(grafico_png)  # no bloquea la ventana
        grafico.content = ft.Image(src=png, width=640)
        boton_exp.disabled, progreso.visible = False, False
        mensaje.value = "Experimento listo (mismas listas para ambos algoritmos)."
        page.update()

    boton_exp = ft.OutlinedButton(content="Correr experimento", icon=ft.Icons.SHOW_CHART, on_click=experimento)

    page.add(
        ft.Text("Búsqueda lineal vs binaria", size=26, weight=ft.FontWeight.BOLD),
        ft.Text("La lista se ordena automáticamente. Prueba un valor que no esté para ver el peor caso.",
                size=13, color=ft.Colors.ON_SURFACE_VARIANT),
        ft.Row([entrada_lista, entrada_objetivo, selector]),
        ft.Row([
            ft.Button(content="Buscar", icon=ft.Icons.SEARCH, on_click=buscar),
            entrada_cantidad,
            ft.OutlinedButton(content="Lista aleatoria", icon=ft.Icons.SHUFFLE, on_click=generar),
            boton_exp, progreso,
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
        mensaje, resultados, grafico,
    )
