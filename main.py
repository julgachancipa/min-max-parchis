from tablero import tablero_inicial, update_tablero
from jugador import Jugador

if __name__ == "__main__":
    print("_________PARCHIS__________")

    # Definir jugadores
    jugador1 = Jugador(id=1)
    jugador2 = Jugador(id=2)

    update_tablero(jugador1, jugador2)

    while not (
        (jugador1.ficha1 == 37 and jugador1.ficha2 == 37)
        or (jugador2.ficha1 == 37 and jugador2.ficha2 == 37)
    ):
        jugador1.lanzar_mover(jugador2)

        update_tablero(jugador1, jugador2)

        if (jugador1.ficha1 == 37 and jugador1.ficha2 == 37) or (
            jugador2.ficha1 == 37 and jugador2.ficha2 == 37
        ):
            break

        jugador2.lanzar_mover(jugador1)

        update_tablero(jugador1, jugador2)

    print("___________FIN____________")
