class Jugador:
    def __init__(self, nombre, pais, elo):
        self.nombre = nombre
        self.pais = pais
        self.elo = int(elo)
        
    def __repr__(self):
        return f"{self.nombre} ({self.pais}) - ELO: {self.elo}"

    def ordenar_manual(self, lista):
        lista_ordenada = lista
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j].elo < lista_ordenada[j + 1].elo:
                    lista_ordenada[j], lista_ordenada[j+ 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j],
                    )

        return lista_ordenada

    def ordenar_sorted(self, lista):
        return sorted(lista, key=lambda jugador: jugador.elo, reverse=True)

jugadores = []
with open("jugadores.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(", ")
        jugadores.append(Jugador(datos[0], datos[1], int(datos[2])))

for jugador in jugadores[0].ordenar_manual(jugadores):
    print(jugador)


"""
python torneo.py > jugadores_ordenado.txt
time python torneo.py
"""
