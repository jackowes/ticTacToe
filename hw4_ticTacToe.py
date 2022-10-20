import random
import copy
import time

#Constants for checking whose turn it is
X = 0
O = 1

MAXIMIZING = 1
MINIMIZING = 0

#this function needs the available function, the win check, and the eval changed. It also needs to be able to pass a depth like normal. 
def min_max(curr_game, max_or_min, depth, max_depth):
    """
    Here I need to give it the eval function that we are looking for
    """
    available_moves = curr_game.successor_function()
    
    #Base case when:
    # - we have no possible moves
    # - a player has won
    # - we hit max search depth
    if len(available_moves) == 0 or curr_game.win_check() == True or depth == max_depth:
        #Check for win
        if curr_game.win_check() == True:
            if max_or_min == MAXIMIZING: #this needs to be changed to max or min I think
                return 1000
            elif max_or_min == MINIMIZING:
                return -1000       

        #Check for draw
        elif curr_game.win_check() == False and len(available_moves) == 0:
            return 0

        #Check when max depth is hit
        else:
            eval = eval_board(curr_game.board, curr_game.get_x_or_o)
            return eval
 


    
    """
    The maximizing player
    """
    if max_or_min == MAXIMIZING:
        
        max_eval = -1000
        max_move = available_moves[0]
        
        # Searches for best possible maxmizing move
        for child in available_moves:
            row, col = child.split(",") #does it modify?

            new_game = copy.deepcopy(curr_game)

            
            new_game.board[int(row) - 1][int(col) - 1] = new_game.get_x_or_o()
            #new_game.available.remove("{0},{1}".format(row, col))
            new_game.change_players()
            

            eval = min_max(new_game, MINIMIZING, depth + 1, max_depth)
            # max_eval = max(eval, max_eval)
            
            if eval > max_eval: 
                max_eval = eval
                max_move = child
            
        # Return move if we finish searching or max eval if we still need to search
        if depth == max_depth: return max_move
        return max_eval
            
    

    
    """
    Minimizing portion
    """
    if max_or_min == MINIMIZING:
        min_eval = 1000
        min_move = available_moves[0]
        for child in available_moves:
            row, col = child.split(",") #does it modify?

            new_game = copy.deepcopy(curr_game)

            
            new_game.board[int(row) - 1][int(col) - 1] = new_game.get_x_or_o()
            # new_game.available.remove("{0},{1}".format(row, col))
            new_game.change_players()

            eval = min_max(new_game, MAXIMIZING, depth + 1)

            if eval < min_eval: 
                min_eval = eval
                min_move = child

        if depth == max_depth: return min_move
        return min_eval


#################################################

def eval_row(player_char, row):
    twoWone = 0
    twoWtwo = 0
    threeWone = 0
    threeWtwo = 0
    open_spaces = 0
    occupied_spaces = 0

    def the_check():
        nonlocal twoWone, twoWtwo, threeWone, threeWtwo, open_spaces, occupied_spaces

        if occupied_spaces == 1:
            return
        if occupied_spaces == 2:
            if open_spaces == 2:
                twoWtwo += 1
            elif open_spaces == 1:
                twoWone += 1
        if occupied_spaces == 3:
            if open_spaces == 2:
                threeWtwo += 1
            elif open_spaces == 1:
                threeWone += 1
                
    for char in row:
        if char == "-":
            open_spaces += 1
            the_check()
            open_spaces = 1
            occupied_spaces = 0
        elif char == player_char:
            occupied_spaces += 1
        else:
            occupied_spaces = 0
            open_spaces = 0
            
    
    return (threeWtwo, threeWone, twoWtwo, twoWone)

def eval_board(board, player_char):
    #Eval Each board
    score = 0
    board =            [["-","X","X","X","-","-"],
                        ["-","X","X","-","X","X"],
                        ["-","X","O","X","-","-"], 
                        ["X","X","-","-","-","-"], 
                        ["-","-","-","X","X","X"]]
    player_char = "X"
    opponent_char = ""

    #Set player and opponent
    if player_char == "X":
        opponent_char = "O"
    else:
        opponent_char = "X"


    for row in board:
        #Eval current player
        (threeWtwo, threeWone, twoWtwo, twoWone) = eval_row(player_char, row)
        score += (200 * threeWtwo) + (150 * threeWone) + (20 * twoWtwo) + (5 * twoWone)
        print("Score + " + str((200 * threeWtwo) + (150 * threeWone) + (20 * twoWtwo) + (5 * twoWone)))
        #Eval opponent player
        
        (threeWtwo, threeWone, twoWtwo, twoWone) = eval_row(opponent_char, row)
        score -= (80 * threeWtwo) + (40 * threeWone) + (15 * twoWtwo) + (2 * twoWone)
    
    print("Total score= ", score)
   
#The psuedocode
# 2with 1 = 0
# 2 with 2 = 0
# 3 with 1 = 0
# 3 with 2 = 0

# open_space = 0 
# Occupied spaces = 0

# For row in rows:
# For spaces in row:
# 	If space = empty:
# 		Open_space += 1
# 		Do the check
# 		Open_space = 1 
# 		Occupied_spaces = 0
# 	If space = player:
# 		Occupied_spaces += 1
# 	Else:
# 		occupied_spaces = 0
#       open_space = 0
		



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
        self.board =   [["-","-","-","-","-","-"],
                        ["-","-","-","-","-","-"],
                        ["-","-","O","X","-","-"], 
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

                    #diagonals
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
        
        #top left to bottom right diagonals
        tl_diagonals = [(1,0), (0,0), (0,1), (0,2)]

        #top right to bottom left diagonals
        tr_diagonals = [(1,5), (0, 5), (0, 4), (0, 3)]


        #top left diagonal search
        for start in tl_diagonals:
            spot = list(start)
            count = 0
            while spot[0] < 5 and spot[1] < 6:
                if(self.board[spot[0]][spot[1]] == player):
                    count += 1
                else:
                    count = 0
                if(count >= 4):
                    return True
                spot[0] += 1
                spot[1] += 1
        
        for start in tr_diagonals:
            spot = list(start)
            count = 0
            print(spot)
            while spot[0] < 5 and spot[1] >= 0:
                
                if(self.board[spot[0]][spot[1]] == player):
                    count += 1
                else:
                    count = 0
                if(count >= 4):
                    return True
                spot[0] += 1
                spot[1] -= 1


        return False




    


    


#=======================================
# def main(choice):
    


#it is going to take a game state then spit back the spot to place the move



#=======================================
if __name__ == '__main__':
    #eval_board(None, None)
    ticGame = ticTacToe()
    ticGame.create_board()
    moves = ticGame.successor_function()
    ticGame.display()
    print(f"\n{moves}")
    print(f"\n{ticGame.win_check()}")