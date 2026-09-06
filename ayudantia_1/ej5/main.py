import operaciones
from interfaz import mostrar_menu

def procesar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()
        
        if opcion == "1":
            nombre = input("Nombre del juego: ")
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                operaciones.agregar_producto(nombre, precio, stock)
                print("Producto agregado con exito!.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Nombre del juego a borrar: ")
            try:
                operaciones.borrar_producto(nombre)
                print("Producto borrado con exito.")
            except KeyError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            nombre = input("Nombre del juego a actualizar: ")
            try:
                precio = float(input("Nuevo precio: "))
                stock = int(input("Nuevo stock: "))
                operaciones.actualizar_producto(nombre, precio, stock)
                print("Producto actualizado con exito.")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
                
        elif opcion == "4":
            operaciones.mostrar_disponibles()

        elif opcion == "5":
            print("Hasta pronto!")
            break
            
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    procesar()