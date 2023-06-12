# Tic Tac Toe

Como crear el juego del gatos

[source](https://www.youtube.com/watch?v=w0LqU99RRy8)

1. Crear una variable que contenga una multi lista
2. Crear una funciòn que muestre el tablero y que imprima fila por fila del tablero.
3. Crear una funciòn que mande llamar a la funcion *mostrar_tablero*. En esta función, implementar un ciclo *while* que permita que corra infinitavmente la función a menos de que se escriba la palabra *salir* o uno de los jugadores gane.
4. importar la libreria: ```deque```, esta libreria permite rotar el turno de cada jugador.
5. Crear un objeto deque, llamado *turno* que permitira el cambio de turno. Este objeto tendrá dos elementos que representarán los dos jugadores participantes. 
    ```
    turno = deque(["0","X"])
    ```
6. Crear la función para ejecutar el cambio de turno
7. Dentro de la función 3, (juego), crear una variable llamada *jugador* y guardar la función 6 (cambiar_turno)
8. En la variable *posicion* implementar el formato para indicar por medio de la pantalla, que jugador esta jugando, si es "0" o el jugador "X".
9. En la linea posterior a la *salir*, copiar y pegar la variable *jugador*

En este punto, en la pantalla del juego, se puede escribir cualquier caracter y el programa lo acepta, para corregir esto, implementar un bloque try-except, con el objetivo de verificar y ejecutar cuando la opción sea la correcta.

10. ped
11. Crear una función para procesar la posición.
