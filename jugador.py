import random
from tablero import map_tablero
from utils import posibles_estados


class Jugador:
    def __init__(self, id: int) -> None:
        self.id = id
        self.ficha1 = 1
        self.ficha2 = 1
        self.map = map_tablero[self.id]

    def lanzar_mover(self, oponente):
        dado = random.randint(1, 6)

        ubicacion_f1 = self.ficha1
        ubicacion_f2 = self.ficha2

        oponente_f1 = oponente.ficha1 - 17

        oponente_f2 = oponente.ficha2 - 17

        fichas_jugador = {}

        if (
            (ubicacion_f1 != 37)
            and (ubicacion_f1 + dado != oponente_f1)
            and (ubicacion_f1 + dado != oponente_f2)
        ):
            fichas_jugador["f1"] = ubicacion_f1

        if (
            (ubicacion_f2 != 37)
            and (ubicacion_f1 != ubicacion_f2)
            and (ubicacion_f2 + dado != oponente_f1)
            and (ubicacion_f2 + dado != oponente_f2)
        ):
            fichas_jugador["f2"] = ubicacion_f2

        fichas_oponente = []

        if oponente_f1 < 30:
            fichas_oponente.append(oponente_f1)

        if oponente_f2 < 30:
            fichas_oponente.append(oponente_f2)

        estados = posibles_estados(fichas_jugador, fichas_oponente, dado)

        mejor_estado = max(estados, key=estados.get)

        if mejor_estado == "f2":
            if self.ficha2 + dado > 37:
                mejor_estado = "f1"

        if mejor_estado == "f1":
            if self.ficha1 + dado > 37:
                mejor_estado = "f2"
            else:
                self.ficha1 += dado
                if self.ficha1 == oponente_f1:
                    oponente.ficha1 = 1
                if self.ficha1 == oponente_f2:
                    oponente.ficha2 = 1

        if mejor_estado == "f2":
            self.ficha2 += dado
            if self.ficha2 == oponente_f1:
                oponente.ficha1 = 1
            if self.ficha2 == oponente_f2:
                oponente.ficha2 = 1
