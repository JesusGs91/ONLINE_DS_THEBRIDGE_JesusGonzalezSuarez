import numpy as np
import random
import Disparo
def start_juego(tablero_yamato, tablero_enemigo, tablero_copia):
    X_enemigas = 20
    X_yamato = 20
    while True:
        while True:
            while True:
                coordenadas_disparo = input("elige fila y columna separadas por comma para saber dodne queires disparar:")
                if (int(coordenadas_disparo.split(",")[0]) and (int(coordenadas_disparo.split(",")[1]))):
                    break
            coordenadas_disparo_x = int(coordenadas_disparo.split(",")[0])-1
            coordenadas_disparo_y = int(coordenadas_disparo.split(",")[1])-1
            if Disparo.disparo(coordenadas_disparo_x,coordenadas_disparo_y,tablero_enemigo,tablero_copia)[2] == True:
                print("Equipo Yamato")
                print(tablero_yamato)
                X_enemigas = X_enemigas -1 
                if X_enemigas == 0:
                    print("El juego ha acabado con victoria de Yamato")
                    break
            else:
                print("Equipo Yamato")
                print(tablero_yamato)
                break    
        while True:
            coordenadas_disparo_x = random.randint(0,9)
            coordenadas_disparo_y = random.randint(0,9)
            if Disparo.disparo_maquina(coordenadas_disparo_x,coordenadas_disparo_y,tablero_yamato)[1] == True:
                print("Equipo Maquina")
                print(tablero_copia)
                X_yamato = X_yamato -1 
                if X_yamato == 0:
                    print("El juego ha acabado con victoria de la maquina")
                    break
            else:
                print("Equipo Maquina")
                print(tablero_copia)
                break   

                

                
                
