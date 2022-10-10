import random
import copy
import time

#Constants for checking whose turn it is
HUMAN = 0
BOT = 1



def min_max(board, depth):
    """
    The min max that just uses an analysis of whether it has won or not.
    It will always go the full depth of the tree. 
    """
    if len(board.available) == 0 or board.better_win_check() == True:
        if board.player == HUMAN and board.better_win_check() == True:
            return -1
        elif board.player == BOT and board.better_win_check() == True:
            
            return 1
            
        else:
            
            return 0

    if board.player == HUMAN:
        max_eval = -100
        max_move = board.available[0]
        for child in board.available:
            form = child
            row, col = form.split(",")

            new_board = copy.deepcopy(board)

            
            new_board.board[int(row) - 1][int(col) - 1] = new_board.get_x_or_o()
            new_board.available.remove("{0},{1}".format(row, col))
            new_board.change_players()
            

            eval = min_max(new_board, depth + 1)
            max_eval = max(eval, max_eval)
            if eval > max_eval: 
                max_move = child
                print(child)

        if depth == 0: return max_move
        return max_eval
    
    if board.player == BOT:
        min_eval = 10
        min_move = 0
        for child in board.available:
            form = child
            row, col = form.split(",")

            new_board = copy.deepcopy(board)

            
            new_board.board[int(row) - 1][int(col) - 1] = new_board.get_x_or_o()
            new_board.available.remove("{0},{1}".format(row, col))
            new_board.change_players()

            eval = min_max(new_board, depth + 1)

            if eval < min_eval and depth == 0: 
                min_move = child
                print(child)

            min_eval = copy.copy(min(eval, min_eval))
            if depth == 0:
                print(f"eval is: {eval} and min_eval is: {min_eval}")

            

        if depth == 0: return min_move
        return min_eval

        



#=======================================
class ticTacToe:
    def __init__(self):
        """
        Initialize new ticTacToe game
        """
        self.player = HUMAN
        self.has_won = False
        self.board = []
        self.available = []
    #=======================================
    def create_board(self):
        """
        Creates empty ticTacToe board
        """
        # for i in range(3):
        #     row = []
        #     for j in range(3):
        #          row.append('-')
        #     self.board.append(row)
        self.board = [["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]

        for i in range(1, 4):
            for j in range(1, 4):
                self.available.append("{0},{1}".format(i,j))

    #=======================================
    def display(self):
        """
        Displays current board in the command line
        """

        for x in self.board:
            for y in x:
                print(y, end=" ")
            print("")

    #=======================================
    def change_players(self):
        """
        Changes from PLAYER -> BOT and vice versa
        """
        if self.player == HUMAN:
            self.player = BOT
        elif self.player == BOT:
            self.player = HUMAN

    #=======================================
    def get_x_or_o(self):
        """
        Obtains whose current turn it is

        Returns (char): A character representing turn either X or O
        """
        if self.player == HUMAN:
            return 'X'
        elif self.player == BOT:
            return 'O'

    #=======================================
    def turn(self):
        """
        Prompts the user for row and column input and then places mark X or O in spot
        """
        if(self.player == HUMAN):
            valid = False
            while valid == False:
                try:
                    row, col = input("Please enter the row and column to place your {0}: ".format(self.get_x_or_o())).split()
                except:
                    print("Not valid entry format")
                    continue
                if self.available.__contains__("{0},{1}".format(row, col)):
                    valid = True
                else:
                    print("Not a valid spot")

            self.board[int(row) - 1][int(col) - 1] = self.get_x_or_o()
            self.available.remove("{0},{1}".format(row, col))

        # Bot will pick a random move from the available moves
        elif(self.player == BOT):
            pick = random.randrange(len(self.available))
            form = self.available[pick]
            row, col = form.split(",")
            self.board[int(row) - 1][int(col) - 1] = self.get_x_or_o()
            self.available.remove("{0},{1}".format(row, col))
            print("Opponent Placed")



    #===================================================================================
    def min_max_turn(self):
        """
        Prompts the user for row and column input and then places mark X or O in spot
        """
        if(self.player == HUMAN):
            valid = False
            while valid == False:
                try:
                    row, col = input("Please enter the row and column to place your {0}: ".format(self.get_x_or_o())).split()
                except:
                    print("Not valid entry format")
                    continue
                if self.available.__contains__("{0},{1}".format(row, col)):
                    valid = True
                else:
                    print("Not a valid spot")

            self.board[int(row) - 1][int(col) - 1] = self.get_x_or_o()
            self.available.remove("{0},{1}".format(row, col))

        # Bot performs minmax
        elif(self.player == BOT):
            form = min_max(self, 0)
            row, col = form.split(",")
            self.board[int(row) - 1][int(col) - 1] = self.get_x_or_o()
            self.available.remove("{0},{1}".format(row, col))
            print("Opponent Placed")

    

    #=======================================
    def win_check(self):
        """
        Determines whether or not any player has won.
        """

        piece = self.get_x_or_o()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != piece:
                    break
                if j == 2:
                    self.has_won = True
                    return True

        for i in range(3):
            for j in range(3):
                if self.board[j][i] != piece:
                    break
                if j == 2:
                    self.has_won = True
                    return True

        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            self.has_won = True
            return True

        if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
            self.has_won = True
            return True

        return False


    #=======================================
    def better_win_check(self):
        """
        Determines whether or not any player has won.
        """
        pieces = ['X','O']
        for piece in pieces:

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != piece:
                        break
                    if j == 2:
                        self.has_won = True
                        return True

            for i in range(3):
                for j in range(3):
                    if self.board[j][i] != piece:
                        break
                    if j == 2:
                        self.has_won = True
                        return True

            if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
                self.has_won = True
                return True

            if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
                self.has_won = True
                return True

        return False





    #=======================================
    def run(self):
        """
        Runs ticTacToe game
        """
        #Continue so long as there are available moves
        self.create_board()
        while len(self.available) > 0:
            self.display()
            self.turn()
            if self.win_check():
                break
            self.change_players()

        self.display()
        if self.has_won == True:
            print("\n\n{0} has won!".format(self.get_x_or_o()))
        else:
            print("\n\nIt was a draw!")
        print("*****Game Over*****")


    #================================================
    def run_min_max(self):
        """
        Runs a ticTacToe game against a min max player
        """
        #Continue so long as there are available moves
        self.create_board()
        while len(self.available) > 0:
            self.display()
            #self.turn()  replace with minmax algorithm
            self.min_max_turn()
            if self.win_check():
                break
            self.change_players()

        self.display()
        if self.has_won == True:
            print("\n\n{0} has won!".format(self.get_x_or_o()))
        else:
            print("\n\nIt was a draw!")
        print("*****Game Over*****")



#=======================================
def main(choice):
    """
    Run ticTacToe game instance
    One for random bot
    Two for minMax bot
    """
    game = ticTacToe()
    if choice == 1:
        game.run()
    elif choice == 2:
        game.run_min_max()
    else:
        print("Invalid input")


#it is going to take a game state then spit back the spot to place the move



#=======================================
if __name__ == '__main__':
    main(2)


