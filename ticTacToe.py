import random


#Constants for checking whose turn it is
HUMAN = 0
BOT = 1

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

#=======================================
def main():
    """
    Run ticTacToe game instance
    """
    game = ticTacToe()
    game.run()


#=======================================
if __name__ == '__main__':
    main()