#Constants for checking whose turn it is
TURN_X = 0
TURN_O = 1

#=======================================
class ticTacToe:
    def __init__(self):
        """
        Initialize new ticTacToe game
        """
        self.player = TURN_X
        self.board = []

    #=======================================
    def create_board(self):
        """
        Creates empty ticTacToe board
        """
        for i in range(3):
            row = []
            for j in range(3):
                 row.append('-')
            self.board.append(row)

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
        Changes from X -> O and vice versa
        """
        if self.player == TURN_X:
            self.player = TURN_O
        elif self.player == TURN_O:
            self.player = TURN_X

    #=======================================
    def get_player(self):
        """
        Obtains whose current turn it is

        Returns (char): A character representing turn either X or O
        """
        if self.player == TURN_X:
            return 'X'
        elif self.player == TURN_O:
            return 'O'

    #=======================================
    def turn(self):
        """
        Prompts the user for row and column input and then places mark X or O in spot
        """
        row, col = input("Please enter the row and column to place your {0}: ".format(self.get_player())).split()
        self.board[int(row) - 1][int(col) - 1] = self.get_player()

    #=======================================
    def run(self):
        """
        Runs ticTacToe game
        """
        self.create_board()
        for x in range(9):
            self.display()
            self.turn()
            self.change_players()

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