# I had an interview to implement a tic tac toe
# Had to use 2 D array - couldn't make it work. 


import os
os.system("clear")
class Game():
    def __init__(self):
        self.board_game = [" ", " ", " ", " "," ", " ", " ", " "," ", " " ]

    def display_board(self):
        print(self.board_game[1], "|", self.board_game[2], "|", self.board_game[3] )
        print("---------")
        print(self.board_game[4], "|", self.board_game[5], "|", self.board_game[6] )
        print("---------")
        print(self.board_game[7], "|", self.board_game[8], "|", self.board_game[9] )


    def update_board(self,box_num, player):
        if self.board_game[box_num] == " ":
            self.board_game[box_num] = player

    def refresh_board(self):
        os.system("clear")
        print("Welcome to the Tic-Tac-Toe Game!")
        board.display_board()

    def is_winner(self, player):
        win_conditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for win in win_conditions:
            result = True
            for cell in win:
                if self.board_game[cell] != player:
                    result = False
            if result == True:
                return True
        return False

    def is_board_full(self):
        pass
        used_box = 0
        for box in self.board_game:
            if box != " ":
                used_box += 1
        if used_box == 9:
            return True
        else:
            return False

    def get_input(self):
        while True:
            board.refresh_board()
            # get X input
            player_x = int(input("Player X, choose a number between 1-9 -> "))
            board.update_board(player_x, "X")
            board.refresh_board()  
            if board.is_winner("X"): 
                print("X, Won")
                break
            board.refresh_board()  

            if board.is_board_full():
                print("Board is full! Tie Game!")
                break
            # get O input
            player_o = int(input("Player O, choose a number between 1-9 -> "))
            board.update_board(player_o, "O")
            if board.is_winner("O"): 
                print("O, Won")
                break
            board.refresh_board()  
            if board.is_board_full():
                print("Board is full! Tie Game!")
                break


            

board = Game()
board.get_input()






















### Step 1
# Create a way to represent an instance of the game. 
# Be sure to capture the state of the game as well as whose turn it is.

# class Game():
#     def __init__(self):

#         self.board_game = [ ["-", "-","-"], 
#                             ["-", "-","-"],
#                             ["-", "-", "-"] ]

#     def display_board(self):
#         print(self.board_game[0][0], self.board_game[0][1], self.board_game[0][2])
#         print(self.board_game[1][0], self.board_game[1][1], self.board_game[1][2])
#         print(self.board_game[2][0], self.board_game[2][1], self.board_game[2][2])

#     def get_user_input(self):

#         player_input = input("Player, choose column and row -> ")
#         board.update_board("X", )
        


#     def update_board(self, player, position):
#         if self.board_game[0][0] == "-":
#             self.board_game[0][0] = player



# board = Game() 
# board.display_board() 
# board.get_user_input()   


### Step 2
# Visually print the state of the board to stdout in a readable format.

### Step 3
# Create a way to prompt the user for input (stdin), and update the corresponding board state based on their input.

### Step 4
# Build a check that determines if the board is full. If the board is full, print to stdout that the game has ended.

### Step 5
# Build a check that determines if a player has won, and prints to stdout the winner if there is one.

### Step 6
# Put it together! Combine the previous pieces of logic to play a game of tic tac toe on the command line. The program should exit once an end state is reached, as well as print the corresponding state and result (if applicable) each time the state changes.

### Bonus (Open ended)
# Design and impement a computer player that replaces one of the existing human players. Optimize the computer's move choices so that the computer never loses.
