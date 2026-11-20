# Mini Proyecto: búsqueda lineal vs binaria

## Ejecutar
    python main.py  # abre la app en flet
    python -m unittest discover tests  # corre los tests
    python -m src.experiments.benchmark  # genera resultados.png sin UI

## Estructura
    main.py                 punto de entrada (solo arranca la UI)
    src/models/             clases del problema (ListaNumeros, Resultado)
    src/algorithms/         base.py (clase abstracta) + lineal.py + binaria.py
    src/experiments/        mediciones y gráfico (matplotlib)
    src/ui/                 interfaz flet, sin lógica de búsqueda
    tests/                  pruebas unitarias con unittest

## Sobre flet
### ¿Qué es?
Flet es un framework para crear aplicaciones con interfaz gráfica usando **solo Python**: no hace falta saber HTML, CSS, JavaScript ni Dart. Con el mismo código se puede abrir una ventana de escritorio (Windows, Linux, macOS), servirlo como página web o empaquetarlo para móvil. Su interfaz está construida sobre Flutter (el toolkit de Google), por eso se ve moderna sin esfuerzo.
 
### ¿Cómo funciona?
1. **Tu programa Python** crea y modifica *controles* (botones, campos de texto, filas, imágenes...).
2. **Flet los envía a un cliente Flutter** (la ventana que ves), que es quien dibuja la interfaz.
3. Cuando el usuario hace clic o escribe, **el cliente avisa a Python** y se ejecuta tu función (*event handler*).
4. Si cambias algo en un control, llamas a `page.update()` y el cambio se refleja en pantalla.
#### Conceptos:
- `page` (`ft.Page`): la ventana/página donde se agregan los controles.
- **Controles**: objetos Python (`ft.TextField`, `ft.Button`, `ft.Row`, `ft.Container`, `ft.Image`...). Los de layout (`Row`, `Column`) contienen a otros.
- **Eventos**: `on_click=funcion`. La función recibe un parámetro `e` (el evento).
- **Modelo imperativo**: modificas el valor (`texto.value = "hola"`) y luego `page.update()`. Si olvidas el `update()`, no se ve nada.
### Instalación
Requiere Python 3.10 o superior. Se recomienda un entorno virtual para no mezclar librerías.
 
**Windows (PowerShell)**
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
**Linux / macOS**
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Verificar: `flet --version`. Este proyecto se probó con Flet 1.1.2.
 
> Flet cambia bastante entre versiones (por ejemplo `ft.app(target=main)` pasó a `ft.run(main)`). Si algo del código falla, revisa primero tu versión con `pip show flet`.
 
### Ejecutar
```
python main.py            # ventana de escritorio
flet run main.py          # igual, pero se recarga sola al guardar (hot reload)
flet run --web main.py    # en el navegador
```
Ejecuta siempre desde la carpeta raíz del proyecto, o los imports (`from src...`) no se encontrarán.
 
### Ejemplo mínimo: contador
```python
import flet as ft
 
def main(page: ft.Page):
    contador = ft.Text("0", size=30)
 
    def sumar(e):
        contador.value = str(int(contador.value) + 1)
        page.update()           # sin esto no se ve el cambio
 
    page.add(contador, ft.Button(content="Sumar", on_click=sumar))
 
ft.run(main)
```
 
### Cómo lo usamos en este proyecto
- `src/ui/app.py` define `main(page)` con la interfaz; `main.py` solo la lanza con `ft.run`.
- La UI **no contiene lógica de búsqueda**: llama a `src.algorithms` y muestra el `Resultado`.
- Los errores de entrada (`ValueError`) se capturan en la UI y se muestran en un `ft.Text` rojo.
- El gráfico de matplotlib se genera como bytes PNG y se muestra con `ft.Image(src=bytes)`.
### Errores comunes
| Síntoma | Causa probable |
|---|---|
| Hago clic y no cambia nada | Falta `page.update()` |
| `AttributeError: module 'flet' has no attribute ...` | Versión distinta a la del ejemplo (`pip show flet`) |
| `ModuleNotFoundError: src` | Ejecutaste desde otra carpeta; vuelve a la raíz |
| `on_click` falla al hacer clic | La función debe recibir un parámetro (`def f(e):`) |
 
### Recursos
- Documentación oficial: https://docs.flet.dev
- Repositorio: https://github.com/flet-dev/flet

## Otras opciones de interfaz gráfica

El enunciado dice que **no es obligatorio** desarrollar una interfaz gráfica completa: la consola también es válida. Si quieren una interfaz, estas son las alternativas más usadas en Python.

| Librería | Tipo | Instalación | Ideal para | Punto a considerar |
|---|---|---|---|---|
| **Tkinter** | Escritorio | Viene con Python | Proyectos simples sin instalar nada | Aspecto antiguo por defecto |
| **CustomTkinter** | Escritorio | `pip install customtkinter` | Tkinter con aspecto moderno | Depende de Tkinter |
| **PyQt6 / PySide6** | Escritorio | `pip install PySide6` | Aplicaciones grandes y profesionales | Curva de aprendizaje más alta |
| **NiceGUI** | Web (navegador) | `pip install nicegui` | Interfaces web solo con Python | Requiere navegador |
| **Streamlit** | Web (navegador) | `pip install streamlit` | Dashboards y gráficos rápidos | Modelo de ejecución distinto: el script se vuelve a correr en cada interacción |
| **Gradio** | Web (navegador) | `pip install gradio` | Demos rápidas con entradas y salidas | Poco control del diseño |
| **Dear PyGui** | Escritorio | `pip install dearpygui` | Visualizaciones y herramientas interactivas | Comunidad más pequeña |
| **Pygame** | Escritorio | `pip install pygame` | Animaciones y juegos (laberintos, N reinas) | Los botones y campos de texto hay que dibujarlos a mano |
| **Textual** | Terminal | `pip install textual` | Interfaces en la terminal | No es una ventana gráfica |

### ¿Cuál elegir?
- **Quiero lo más simple y sin instalar nada:** Tkinter.
- **Quiero algo moderno con poco código:** Flet o CustomTkinter.
- **Quiero algo muy visual (tableros, laberintos, animaciones):** Pygame.
- **Quiero mostrar gráficos y resultados rápido:** Streamlit o NiceGUI.

