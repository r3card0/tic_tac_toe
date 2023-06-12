# Libreria que permite rotar los turnos de los jugadores
from collections import deque

# objeto deque, para rotar el turno
turno = deque(["0","X"])


# variable que guarda una multi -lista
tablero = [
    ['','',''],
    ['','',''],
    ['','',''],
]


# función para el cambio de turno del jugador
def cambiar_turno():
    turno.rotate()  # aplicar el módulo rotate en el objeto turno
    return turno[0] # retornar el primer elemento



# función para imprimir el tablero
def mostrar_tablero():
    print("") # deja un espacio en blanco
    # el loop for permite imprimir fila por fila del tablero
    for fila in tablero:
        print(fila)

# función para procesar la posición
def procesar_posicion(posicion):
    fila,columna = posicion.split(',') # en las variables x,y se separan los valores elegidos por el usuario, 
    return [int(fila)-1,int(columna)-1] # retorna los valores en integers y calibra los valores a las posiciones de la máquina.

# función que manda llamar a la función : mostrar_tablero
def juego():
    mostrar_tablero()
    jugador = cambiar_turno()
    while True:
        posicion = input("Juega {}. Elije una posición: (fila,columna) del 1 al 3: ".format(jugador))
        if posicion == "salir": # logica para elegir la opcion salir
            break
        jugador = cambiar_turno()
        try:
            posicion_1 = procesar_posicion(posicion)


def run():
    # print(tablero)
    juego()

if __name__ == "__main__":
    run()
