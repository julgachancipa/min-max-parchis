from tablero import seguros


def heuristica(sig_f_jugador, f_oponente):

    if (sig_f_jugador == f_oponente) and (f_oponente not in seguros):
        return 100

    if (sig_f_jugador == f_oponente) and (f_oponente in seguros):
        return -100

    dif = sig_f_jugador - f_oponente

    return dif


def posibles_estados(fichas_jugador: dict, fichas_oponente: list, dado: int):
    dict_heuristica = {}

    for f, ubicacion in fichas_jugador.items():
        sig_f_jugador = ubicacion + dado

        dict_heuristica[f] = 0

        for u_oponente in fichas_oponente:
            # No es posible ocupar el mismo seguro que el oponente
            if (sig_f_jugador == u_oponente) and (u_oponente in seguros):
                continue

            h = heuristica(sig_f_jugador, u_oponente)
            dict_heuristica[f] = dict_heuristica[f] + h

    return dict_heuristica
