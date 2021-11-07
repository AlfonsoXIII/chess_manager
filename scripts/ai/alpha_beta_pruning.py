#Mòduls importats
from copy import deepcopy
from math import inf
import numpy
import concurrent.futures

from numpy.core.defchararray import asarray

#Scripts importats
import scripts.ai.movements as movements
#import movements

def Evaluate_Position(board):
    board_value = 0

    chess_value = {"P":1000, "N":2000, "B":3000, "R":5000, "Q":9000, "K":900000, "p":-1000, "n":-2000, "b":-3000, "r":-5000, "q":-9000, "k":-900000}

    pieces_position_value = {"P":[[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                                [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
                                [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
                                [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
                                [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
                                [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
                                [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
                                [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]],
                            
                            "p":[[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                                [-0.5,  -1.0, -1.0,  2.0, 2.0,  -1.0,  -1.0,  -0.5],
                                [-0.5, 0.5, 1.0,  0.0,  0.0, 1.0, 0.5,  -0.5],
                                [0.0,  0.0,  0.0,  -2.0,  -2.0,  0.0,  0.0,  0.0],
                                [-0.5,  -0.5,  -1.0,  -2.5,  -2.5,  -1.0,  -0.5,  -0.5],
                                [-1.0,  -1.0,  -2.0,  -3.0,  -3.0,  -2.0,  -1.0,  -1.0],
                                [-5.0,  -5.0,  -5.0,  -5.0,  -5.0,  -5.0,  -5.0,  -5.0],
                                [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]],

                            "N":[[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
                                [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
                                [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
                                [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
                                [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
                                [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
                                [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
                                [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]],
                            
                            "n":[[5.0, 4.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0],
                                [4.0, 2.0,  0.0,  -0.5,  -0.5,  0.0, 2.0, 4.0],
                                [3.0,  -0.5,  -1.0,  -1.5,  -1.5,  -1.0,  -0.5, 3.0],
                                [3.0,  0.0,  -1.5,  -2.0,  -2.0,  -1.5,  0.0, 3.0],
                                [3.0,  -0.5,  -1.5,  -2.0,  -2.0,  -1.5,  -0.5, 3.0],
                                [3.0,  0.0,  -1.0,  -1.5,  -1.5,  -1.0,  0.0, 3.0],
                                [4.0, 2.0,  0.0,  0.0,  0.0,  0.0, 2.0, 4.0],
                                [5.0, 4.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0]],
                                
                            "B":[[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
                                [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                                [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
                                [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
                                [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
                                [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
                                [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
                                [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]],
                            
                            "b":[[ 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0],
                                [ 1.0,  -0.5,  0.0,  0.0,  0.0,  0.0,  -0.5, 1.0],
                                [ 1.0,  -1.0,  -1.0,  -1.0,  -1.0,  -1.0,  -1.0, 1.0],
                                [ 1.0,  0.0,  -1.0,  -1.0,  -1.0,  -1.0,  0.0, 1.0],
                                [ 1.0,  -0.5,  -0.5,  -1.0,  -1.0,  -0.5,  -0.5, 1.0],
                                [ 1.0,  0.0,  -0.5,  -1.0,  -1.0,  -0.5,  0.0, 1.0],
                                [ 1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 1.0],
                                [ 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0]],
                            
                            "R":[[  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
                                [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
                                [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
                                [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
                                [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
                                [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
                                [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
                                [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]],
                            
                            "r":[[  0.0,   0.0, 0.0,  -0.5,  -0.5,  0.0,  0.0,  0.0],
                                [ 0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.5],
                                [ 0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.5],
                                [ 0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.5],
                                [ 0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.5],
                                [ 0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 0.5],
                                [  -0.5,  -1.0,  -1.0,  -1.0,  -1.0,  -1.0,  -1.0,  -0.5],
                                [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]],

                            "Q":[[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                                [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                                [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                                [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                                [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                                [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                                [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
                                [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]],
                            
                            "q":[[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
                                [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
                                [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                                [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                                [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
                                [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
                                [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
                                [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]],
                            
                            "K":[[ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
                            
                            "k":[[ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]}

    for a in range(0, 8):
        for b in range(0, 8):
            if board[b, a] != "":
                board_value += chess_value[board[b, a]]
                
                
                #if board[b, a].isupper():

                board_value += (pieces_position_value[board[b, a]])[b][a]

                #else:
                #    board_value += ((pieces_position_value[board[b, a].upper()])[b][a])*-1.0


    return board_value

def add_Depth(board, colour):
    childs = []
    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if board[b, a].isupper() == colour:

                if board[b, a].upper() == "P":
                    temp = movements.Pawn(board, (0 if board[b, a].isupper() else 1), (b, a))
                
                elif board[b, a].upper() == "N":
                    temp = movements.Knight(board, (b, a))

                elif board[b, a].upper() == "R":
                    temp = movements.Rock(board, (b, a))
                
                elif board[b, a].upper() == "B":
                    temp = movements.Bishop(board, (b, a))
                
                elif board[b, a].upper() == "Q":
                    temp = movements.Queen(board, (b, a))
                
                elif board[b, a].upper() == "K":
                    temp = movements.King(board, (0 if board[b, a].isupper() else 1), (b, a))

                for x in temp:
                    temp_board = deepcopy(board)
                    temp_board[x[0], x[1]] = deepcopy(board[b, a])
                    temp_board[b, a] = ""

                    childs.append(temp_board)
    
    return childs

def min_value(board, alpha, beta, colour, depth):
    v = +inf

    node = add_Depth(board, (True if colour == False else False))

    if len(node) == 0:
        if colour == True:
            return 900
        
        else:
            return -900


    for child in node:
        if depth < 3:
            v = min(v, max_value(child, alpha, beta, (True if colour == False else False), depth+1))

        else:
            v = Evaluate_Position(child)

        if v <= alpha:  
            return v
        
        beta = min(beta, v)

    return v

def max_value(board, alpha, beta, colour, depth):
    v = -inf

    node = add_Depth(board, (True if colour == False else False))

    if len(node) == 0:
        if colour == True:
            return 900
        
        else:
            return -900

    for child in node:
        if depth < 3:
            v = max(v, min_value(child, alpha, beta, (True if colour == False else False), depth+1))

        else:
            v = Evaluate_Position(child)

        if v >= beta:
            return v
        
        alpha = max(alpha, v)
    
    return v

def inmin_value(board, alpha, beta, colour, depth):
    v = +inf

    node = add_Depth(board, (True if colour == False else False))
    values = {}


    for child in node:
        temp = max_value(child, alpha, beta, (True if colour == False else False), depth+1)

        if v > temp:
            values[temp] = child

        v = min(v, temp)

        if v <= alpha:
            return v, values
        
        beta = min(beta, v)

    return v, values

def inmax_value(board, alpha, beta, colour, depth):
    v = -inf

    node = add_Depth(board, (True if colour == False else False))
    values = {}

    for child in node:
        temp = min_value(child, alpha, beta, (True if colour == False else False), depth+1)
        if v < temp:
            values[temp] = child

        v = max(v, temp)

        if v >= beta:
            return v, values
        
        alpha = max(alpha, v)
    
    return v, values

def root_an(board, alpha, beta, colour, depth, Queue):
    board = numpy.asarray(board)

    if colour == True:
        temp = inmax_value(board, alpha, beta, False, depth)
        Queue.put(str(temp[0]))

    else:
        temp = inmin_value(board, alpha, beta, True, depth)
        Queue.put(str(temp[0]))

def root_play(board, alpha, beta, colour, depth, Queue):
    board = numpy.asarray(board)

    if colour == True:
        temp = inmax_value(board, alpha, beta, False, depth)
        Queue.put(temp[1][temp[0]])

    else:
        temp = inmin_value(board, alpha, beta, True, depth)
        Queue.put(temp[1][temp[0]])

def main(board, depth, colour):
    print("##########  INIT  ##########")
    print("Depth: ", str(depth))
    print("############################")

    board = asarray(board)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        p1 = executor.submit(inmin_value, board, -inf, +inf, colour, 1)
        temp = p1.result()

        print(temp)


if __name__ == "__main__":
    '''
    main([["n", "n", "b", "q", "k", "b", "n", "r"],
        ["R", "p", "p", "", "p", "", "p", "p"],
        ["", "", "n", "", "", "", "", ""],
        ["", "B", "", "p", "P", "p", "", ""],
        ["", "", "", "P", "", "", "", ""],
        ["", "", "P", "", "", "", "", ""],
        ["P", "", "P", "", "", "P", "P", "P"],
        ["R", "", "B", "Q", "K", "", "", "R"]], 
        4, 
        True)
    '''
    main([["", "", "", "", "", "k", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "R", "", "", "q", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "P", "P", "P"],
        ["", "", "", "", "", "", "K", ""]], 
        4, 
        True)