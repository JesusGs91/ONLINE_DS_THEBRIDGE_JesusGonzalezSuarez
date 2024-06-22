import numpy as np

# Crea tablero 10x10
def GeneraTablero():
    columnas = " -------------------"
    print(" ", end="")
    for letra in columnas:
        print(letra, end=" ")
    print()
    tablero = np.full([10,10]," ")
    print(tablero)
    return tablero