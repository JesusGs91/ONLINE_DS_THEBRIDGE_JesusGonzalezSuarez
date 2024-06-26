import numpy as np

def disparo(x, y, tablero, tablero_copia):
    efectivo = True
    atributo = np.where(tablero[x,y] == 'O', 'X', '-')
    tablero[x,y] = atributo
    tablero_copia[x,y] = atributo
    if atributo == 'X':
        efectivo = True
        print("Has acertado, sigue disparando")
        print("Equipo Maquina")
        print(tablero_copia)
    else:
        efectivo = False
        print("Has Falladao, turno de la maquina")
        print("Equipo Maquina")
        print(tablero_copia)
    return tablero, tablero_copia, efectivo

def disparo_maquina(x, y, tablero):
    efectivo = True
    atributo = np.where(tablero[x,y] == 'O', 'X', '-')
    tablero[x,y] = atributo
    if atributo == 'X':
        efectivo = True
        print("Has acertado, sigue disparando")
        print("Equipo Yamato")
        print(tablero)
    else:
        efectivo = False
        print("Has Falladao, turno de el jugador")
        print("Equipo Yamato")
        print(tablero)
    return tablero, efectivo
        