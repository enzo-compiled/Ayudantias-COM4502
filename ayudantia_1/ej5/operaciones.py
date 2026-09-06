import data, utils

def agregar_producto(nombre, precio, stock):
    nombre_limpio = nombre.lower().strip()
    
    if precio < 0 or stock < 0:
        raise ValueError("El precio y el stock no pueden ser negativos.")
        
    if nombre_limpio in data.juegos:
        raise ValueError("El producto ya existe. Usa la opcion de actualizar.")
        
    data.juegos[nombre_limpio] = {"precio": precio, "stock": stock}

def borrar_producto(nombre):
    nombre_limpio = nombre.lower().strip()
    if nombre_limpio not in data.juegos:
        raise KeyError(f"El producto '{nombre}' no existe.")
        
    del data.juegos[nombre_limpio]

def actualizar_producto(nombre, precio, stock):
    nombre_limpio = nombre.lower().strip()
    if nombre_limpio not in data.juegos:
        raise KeyError(f"El producto '{nombre}' no existe.")
        
    if precio < 0 or stock < 0:
        raise ValueError("El precio y el stock no pueden ser negativos.")
        
    data.juegos[nombre_limpio] = {"precio": precio, "stock": stock}

def mostrar_disponibles():
    if not data.juegos:
        print("El inventario esta vacio.")
        return
        
    print(f"\n{'NOMBRE':<25} | {'PRECIO':<10} | {'STOCK':<5}") 
    print("-" * 45)
    for nombre, info in data.juegos.items():
        precio_formateado = utils.formatear_dinero(info['precio'])
        print(f"{nombre.title():<25} | {precio_formateado:<10} | {info['stock']:<5}")
    print("-" * 45)