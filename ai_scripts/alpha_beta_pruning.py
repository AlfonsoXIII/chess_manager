#Mòduls importats
from copy import deepcopy
import time
from math import inf

#Scripts importats
import movements as mvs
import tree_dataStructure as tree

def Evaluate_Position(board):
    board_value = 0

    chess_value = {"P":1, "N":2, "B":3, "R":5, "Q":9, "K":900, "p":-1, "n":-2, "b":-3, "r":-5, "q":-9, "k":-900}

    for row in board:
        for square in row:
            if square != "":
                board_value += chess_value[square]
    
    return board_value

def add_Depth(board, colour):
    childs = []
    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if board[b][a].upper() == "P" and board[b][a].isupper() == colour:
                temp = mvs.Pawn(board, (0 if board[b][a].isupper() else 1), (b, a))
            
            elif board[b][a].upper() == "N" and board[b][a].isupper() == colour:
                temp = mvs.Knight(board, (b, a))

            elif board[b][a].upper() == "R" and board[b][a].isupper() == colour:
                temp = mvs.Rock(board, (b, a))
            
            elif board[b][a].upper() == "B" and board[b][a].isupper() == colour:
                temp = mvs.Bishop(board, (b, a))
            
            elif board[b][a].upper() == "Q" and board[b][a].isupper() == colour:
                temp = mvs.Queen(board, (b, a))
            
            elif board[b][a].upper() == "K" and board[b][a].isupper() == colour:
                temp = mvs.King(board, (0 if board[b][a].isupper() else 1), (b, a))

            for x in temp:
                temp_board = deepcopy(board)
                temp_board[x[0]][x[1]] = deepcopy(board[b][a])
                temp_board[b][a] = ""

                    
                same_king = ()
                other_king = ()

                for c in range(0, 8):
                    for d in range(0, 8):
                        if temp_board[x[0]][x[1]].upper() != "K":
                            if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() == colour:
                                same_king = (d, c)
                        
                        else:
                            same_king = x
                        
                        if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() != colour:
                            other_king = (d, c)

                
                if mvs.King_Check(temp_board, same_king) and (mvs.King_Check(board, other_king) or (mvs.King_Check(board, other_king) == False and mvs.King_Check(temp_board, other_king))):
                    childs.append(temp_board)
    
    return childs

def min_value(board, alpha, beta, colour, depth):
    v = +inf

    node = add_Depth(board, (True if colour == False else False))

    for child in node:
        if depth < 5:
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

    for child in node:
        if depth < 5:
            v = max(v, min_value(child, alpha, beta, (True if colour == False else False), depth+1))

        else:
            v = Evaluate_Position(child)

        if v >= beta:
            return v
        
        alpha = max(alpha, v)
    
    return v

def Main(board, depth, colour):
    print("##########  INIT  ##########")
    print("Depth: ", str(depth))
    print("############################")
    
    print(max_value(board, -inf, +inf, colour, 1))

Main([["", "k", "", "", "", "", "", ""],
        ["p", "", "p", "", "", "", "b", ""],
        ["", "p", "", "", "", "n", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "Q", "", "p", "", "", ""],
        ["", "", "", "", "", "P", "P", "P"],
        ["", "", "", "", "", "", "", "K"]], 
        4, 
        False)
