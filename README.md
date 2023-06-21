# Tic Tac Toe

![tic](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/1200px-Tic_tac_toe.svg.png)

Como crear el juego del gato

[source](https://www.youtube.com/watch?v=w0LqU99RRy8)

1. Crear una variable que contenga una multi lista. La multi-lista debe tener una estructura o grilla de 3x3. Esta forma imita el tablero del #gato#, (tic-tac-toe)
2. Crear una función que muestre el tablero y que imprima fila por fila del tablero. Esto quiere decir que imprima de la variable tablero, fila por fila
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
