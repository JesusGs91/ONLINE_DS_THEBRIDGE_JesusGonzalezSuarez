
import hundir_la_flota
import numpy as np
import Juego


nombre_jugador = input("El nombre del participante es:")

partida = hundir_la_flota.Tablero(nombre_jugador)
print("Equipo Yamato")
print(partida.tablero_equipo_Yamato)
print("Equipo Maquina")
print(partida.tablero_enemigo_copy)
print("Equipo Maquina2")
print(partida.tablero_enemigo)

Juego.start_juego(partida.tablero_equipo_Yamato, partida.tablero_enemigo, partida.tablero_enemigo_copy)

print("Equipo Yamato")
print(partida.tablero_equipo_Yamato)
print("Equipo Maquina")
print(partida.tablero_enemigo_copy)



