import tablero
import barcos


class Tablero:
    def __init__(self, nombre, ):
        self.nombre = nombre
        self.barcos = ((1, 4), (2, 3), (3, 2), (4, 1))
        self.tablero_equipo_Yamato  = tablero.GeneraTablero()
        self.tablero_enemigo = tablero.GeneraTablero() 
        self.tablero_enemigo_copy = tablero.GeneraTablero() 
        self.coordenadas_de_barcos_Yamato = barcos.ColocaBarco(self.tablero_equipo_Yamato, self.barcos)
        self.coordenadas_maquina = barcos.ColocaBarco(self.tablero_enemigo, self.barcos)