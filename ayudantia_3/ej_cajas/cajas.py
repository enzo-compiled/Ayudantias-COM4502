class Producto:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

class Caja:
    def __init__(self, contenido):
        self.contenido = contenido

def calcular_peso(elemento):
    if isinstance(elemento, Producto):
        return elemento.peso
    
    peso_total = 0
    for sub_elemento in elemento.contenido:
        peso_total += calcular_peso(sub_elemento)
        
    return peso_total

p1 = Producto("Notebook", 2.5)
p2 = Producto("Mouse", 0.2)
p3 = Producto("Teclado", 0.8)

caja_perifericos = Caja([p2, p3]) 
caja_principal = Caja([p1, caja_perifericos])

print(f"Peso total: {calcular_peso(caja_principal)} kg")


"""
time python cajas.py
"""