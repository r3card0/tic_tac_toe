from collections import deque

class Tictactoe:
    def __init__(self) -> None:
        self.board = [
            ["","",""],
            ["","",""],
            ["","",""],
        ]

    def show_board(self):
        print("") # lefting a space
        
        for line in self.board: # print line by line
            print(line)

        print("") # lefting a space

    def game(self): 
        self.show_board() # call show_board function


        # infinite while loop, unless the user types the word 'salir'
        while True: 
            option = str(input(''))
            if option == 'salir':
                break