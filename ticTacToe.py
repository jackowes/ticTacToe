board = """1*2*3
*****
4*5*6
*****
7*8*9"""

turn = 0
TURN_X = 0
TURN_O = 1

player = TURN_X
tile = 0



while turn <= 9:
    print(board)
    if player == TURN_X:
        tile = input("Enter tile to place X: ")
    else:
        tile = input("Enter tile to place O: ")

    for x in board:
        print("The place is:{0}\nAnd the tile is{1}\n".format(x,tile))
        if str(x) == str(tile):
            print("Wwowowwwowowowowwow it works")
        if str(x) == str(tile):
            if player == TURN_X:
                x = 'X'
            else:
                x = 'O'
    if player == TURN_X:
        player = TURN_O
    else:
        player = TURN_X
    turn += 1

print("Game over sorry this was terribly made!")



#maybe make it up of some sort of node so that it can have an algorithm to check all the possible ways.
#a board made of nodes then?