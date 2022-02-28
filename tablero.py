import time

import numpy as np
import matplotlib.pylab as pl


tablero_inicial = [
    ["/../", "[..]", "\..\\"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["[..]", "|..|", "[..]"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "[__]", "|..|"],
    ["|..|", "[__]", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["[..]", "|..|", "[..]"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["|..|", "|..|", "|..|"],
    ["\..\\", "[..]", "/../"],
]

map_tablero = {
    1: {
        1: (4, 0),
        2: (5, 0),
        3: (6, 0),
        4: (7, 0),
        5: (8, 0),
        6: (9, 0),
        7: (10, 0),
        8: (11, 0),
        9: (12, 0),
        10: (13, 0),
        11: (14, 0),
        12: (15, 0),
        13: (15, 1),
        14: (15, 2),
        15: (14, 2),
        16: (13, 2),
        17: (12, 2),
        18: (11, 2),
        19: (10, 2),
        20: (9, 2),
        21: (8, 2),
        22: (7, 2),
        23: (6, 2),
        24: (5, 2),
        25: (4, 2),
        26: (3, 2),
        27: (2, 2),
        28: (1, 2),
        29: (0, 2),
        30: (0, 1),
        31: (1, 1),
        32: (2, 1),
        33: (3, 1),
        34: (4, 1),
        35: (5, 1),
        36: (6, 1),
        37: (7, 1),
    },
    2: {
        1: (11, 2),
        2: (10, 2),
        3: (9, 2),
        4: (8, 2),
        5: (7, 2),
        6: (6, 2),
        7: (5, 2),
        8: (4, 2),
        9: (3, 2),
        10: (2, 2),
        11: (1, 2),
        12: (0, 2),
        13: (0, 1),
        14: (0, 0),
        15: (1, 0),
        16: (2, 0),
        17: (3, 0),
        18: (4, 0),
        19: (5, 0),
        20: (6, 0),
        21: (7, 0),
        22: (8, 0),
        23: (9, 0),
        24: (10, 0),
        25: (11, 0),
        26: (12, 0),
        27: (13, 0),
        28: (14, 0),
        29: (15, 0),
        30: (15, 1),
        31: (14, 1),
        32: (13, 1),
        33: (12, 1),
        34: (11, 1),
        35: (10, 1),
        36: (9, 1),
        37: (8, 1),
    },
}

seguros = [1, 8, 13, 18, 25, 30]


def imprimir_tablero(mtx):
    print("===========================================")
    for row in mtx:
        print("".join(row))
    print("===========================================")

    time.sleep(2)


def update_tablero(jugador1, jugador2):
    mtx = [row[:] for row in tablero_inicial]

    j1_f1 = jugador1.ficha1
    m_tuple = map_tablero[1][j1_f1]
    casilla = mtx[m_tuple[0]][m_tuple[1]]
    casilla = list(casilla)
    casilla[1] = "1"
    mtx[m_tuple[0]][m_tuple[1]] = "".join(casilla)

    j1_f2 = jugador1.ficha2
    m_tuple = map_tablero[1][j1_f2]
    casilla = mtx[m_tuple[0]][m_tuple[1]]
    casilla = list(casilla)
    casilla[2] = "1"
    mtx[m_tuple[0]][m_tuple[1]] = "".join(casilla)

    j2_f1 = jugador2.ficha1
    m_tuple = map_tablero[2][j2_f1]
    casilla = mtx[m_tuple[0]][m_tuple[1]]
    casilla = list(casilla)
    casilla[1] = "2"
    mtx[m_tuple[0]][m_tuple[1]] = "".join(casilla)

    j2_f2 = jugador2.ficha2
    m_tuple = map_tablero[2][j2_f2]
    casilla = mtx[m_tuple[0]][m_tuple[1]]
    casilla = list(casilla)
    casilla[2] = "2"
    mtx[m_tuple[0]][m_tuple[1]] = "".join(casilla)

    imprimir_tablero(mtx)
