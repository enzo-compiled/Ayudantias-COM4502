transacciones = list(range(50000))
lista_negra = list(range(45000,55000))
fraudes=0

def m1(transacciones, lista_n):
    global fraudes
    for t in transacciones:
        for f in lista_n:
            if f == t:
                fraudes+=1
    print(f"fraudes: {fraudes}")

def m2(transacciones, lista_n):
    global fraudes
    for t in transacciones:
        if t in lista_n:
            fraudes+=1
    print(f"fraudes: {fraudes}")

def m3(transacciones, lista_n):
    global fraudes
    cjto = set(lista_n)
    for t in transacciones:
        if t in cjto:
            fraudes+=1
    print(f"fraudes: {fraudes}")


m1(transacciones, lista_negra)
#m2(transacciones, lista_negra)
#m3(transacciones, lista_negra)

"""
time python fraudes.py
"""
