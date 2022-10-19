import random
import copy
import time

#Constants for checking whose turn it is
X = 0
O = 1


#this function needs the available function, the win check, and the eval changed. It also needs to be able to pass a depth like normal. 
def min_max(board, depth):
    """
    Here I need to give it the eval function that we are looking for
    """
    if len(board.available) == 0 or board.better_win_check() == True:
        if board.player == X and board.better_win_check() == True:
            return -1
        elif board.player == O and board.better_win_check() == True:
            
            return 1
            
        else:
            
            return 0

    if board.player == X:
        max_eval = -1000
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

        if depth == 0: return max_move
        return max_eval
    
    if board.player == O:
        min_eval = 1000
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

            min_eval = copy.copy(min(eval, min_eval))

        if depth == 0: return min_move
        return min_eval





#=======================================
class ticTacToe:
    def __init__(self):
        """
        Initialize new ticTacToe game
        """
        self.player = X
        self.has_won = False #Not sure if this is needed I think just a win check function could be better
        self.board = [] 
        self.available = [] #not sure if this is needed anymore
        self.moves = [] #This will be an array of 4 valued tuples: (Turn, The move, CPU Execution time, # of nodes searched)
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
        
        #Should this board just be populated in this way in the constructor
        #Or should I create this board using for statements and a row and col variable so that the size can be changed? I think that's too much as the win check would have to be changed too
        self.board = [["-","-","-","-","-","-"],
                        ["-","-","-","-","-","-"],
                        ["-","-","-","-","-","-"], 
                        ["-","-","-","-","-","-"], 
                        ["-","-","-","-","-","-"]]


        #As the available squares are now only adjacent squares I don't think this is usable any longer
        # for i in range(1, 5):
        #     for j in range(1, 7):
        #         self.available.append("{0},{1}".format(i,j))
        

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
        if self.player == X:
            self.player = O
        elif self.player == O:
            self.player = X

    #=======================================
    def get_x_or_o(self):
        """
        Obtains whose current turn it is

        Returns (char): A character representing turn either X or O
        """
        if self.player == X:
            return 'X'
        elif self.player == O:
            return 'O'


    #=======================================
    def successor_function(self):
        """
        Will determine what moves are valid for the player
        """
        available = []
        for row in range(0, 5):
            for col in range(0, 6):
                if(self.board[row][col] != "-"):
                    #Check above, below, to the right, and to the left of the non empty square
                    if(((row - 1) >= 0) and self.board[row - 1][col] == "-" and (row - 1, col) not in available):
                        available.append((row - 1, col))

                    if(((row + 1) < 5) and self.board[row + 1][ col] == "-" and (row + 1, col) not in available):
                        available.append((row + 1, col))

                    if(((col - 1) >= 0) and self.board[row][ col - 1] == "-" and (row, col - 1) not in available):
                        available.append((row, col - 1))

                    if(((col + 1) < 6) and self.board[row][ col + 1] == "-" and (row, col + 1) not in available):
                        available.append((row, col + 1))    

                    #diaganols (is that how you spell it?)
                    if(((row - 1) >= 0) and ((col + 1) < 6) and self.board[row - 1][col + 1] == "-" and (row - 1, col + 1) not in available):
                        available.append((row - 1, col + 1))

                    if(((row - 1) >= 0) and ((col - 1) >= 0) and self.board[row - 1][col - 1] == "-" and (row - 1, col - 1) not in available):
                        available.append((row - 1, col - 1))

                    if(((row + 1) < 5) and ((col + 1) < 6) and self.board[row + 1][col + 1] == "-" and (row + 1, col + 1) not in available):
                        available.append((row + 1, col + 1))

                    if(((row + 1) < 5) and ((col - 1) >= 0) and self.board[row + 1][col - 1] == "-" and (row + 1, col - 1) not in available):
                        available.append((row + 1, col - 1))

        return available

    

    #=======================================
    def win_check(self):
        """
        Determines whether or not any player has won.
        """
        #I need to check every row and every column then check the 8 diagonals
        player = self.get_x_or_o() #the currentPlayer? Or will this need to be the last played #lets just make it universal


        #check rows
        for row in range(0, 5):
            count = 0
            for col in range(0, 6):
                if(self.board[row][col] == player):
                    count += 1
                else:
                    count = 0
                if(count >= 4):
                    return True

        #check columns
        for col in range(0, 6):
            count = 0
            for row in range(0, 5):
                if(self.board[row][col] == player):
                    count += 1
                else:
                    count = 0
                if(count >= 4):
                    return True


        # need to check diagonals


        return False




    


    


#=======================================
# def main(choice):
    


#it is going to take a game state then spit back the spot to place the move



#=======================================
if __name__ == '__main__':
    ticGame = ticTacToe()
    ticGame.create_board()
    ticGame.board[2][3] = "X"
    ticGame.board[2][2] = "O"
    start = time.process_time()
    start2 = time.time()
    moves = ticGame.successor_function()
    t = 0
    for x in range(100000):
        t += x
    end = time.process_time()
    end2 = time.time()
    exec_time = end - start
    exec_time2 = end2 - start2
    ticGame.display()
    print(f"\n{moves}")
    print(f"\n{exec_time}")
    print(f"\n{exec_time2}")
    print(f"\n{t}")
    print(f"\n{ticGame.win_check()}")