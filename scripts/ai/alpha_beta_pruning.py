#Mòduls importats
from copy import deepcopy
import time
from math import inf
from numba import jit
import multiprocessing as mp
import concurrent.futures

#Scripts importats
import scripts.ai.movements as movements
#import movements

def Evaluate_Position(board):
    board_value = 0

    chess_value = {"P":1, "N":2, "B":3, "R":5, "Q":9, "K":900, "p":-1, "n":-2, "b":-3, "r":-5, "q":-9, "k":-900}

    pieces_position_value = {"P":[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                                [0.2, 0.2, 0.3, 0.4, 0.4, 0.3, 0.2, 0.2],
                                [0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, 0.1],
                                [0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, 0.1],
                                [0.2, 0.2, 0.3, 0.4, 0.4, 0.3, 0.2, 0.2],
                                [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                            "N":[[-1.0, -0.5, -0.3, -0.3, -0.3, -0.3, -0.5, -1.0],
                                [-0.5, -0.2, 0.0, 0.2, 0.2, 0.0, -0.2, -0.3],
                                [-0.3, 0.0, 0.4, 0.3, 0.3, 0.4, 0.0, -0.3],
                                [-0.3, 0.1, 0.5, 0.6, 0.6, 0.5, 0.1, -0.3],
                                [-0.3, 0.1, 0.5, 0.6, 0.6, 0.5, 0.1, -0.3],
                                [-0.3, 0.0, 0.4, 0.3, 0.3, 0.4, 0.0, -0.3],
                                [-0.5, 0.0, 0.0, 0.2, 0.2, 0.0, -0.2, -0.5],
                                [-1.0, -0.5, -0.3, -0.3, -0.3, -0.3, -0.5, -1.0]],
                                
                            "B":[[-0.3, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, -0.3],
                                [-0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, -0.2],
                                [-0.1, 0.1, 0.3, 0.4, 0.4, 0.3, 0.1, -0.1],
                                [-0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, -0.1],
                                [-0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, -0.1],
                                [-0.1, 0.1, 0.3, 0.4, 0.4, 0.3, 0.1, -0.1],
                                [-0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, -0.2],
                                [-0.3, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, -0.3]],
                            
                            "R":[[0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0],
                                [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
                                [-0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.3],
                                [-0.3, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, -0.3],
                                [-0.3, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, -0.3],
                                [-0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.3],
                                [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
                                [0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0]],

                            "Q":[[-0.3, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, -0.3],
                                [-0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, -0.2],
                                [-0.1, 0.1, 0.3, 0.4, 0.4, 0.3, 0.1, -0.1],
                                [-0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, -0.1],
                                [-0.1, 0.1, 0.4, 0.5, 0.5, 0.4, 0.1, -0.1],
                                [-0.1, 0.1, 0.3, 0.4, 0.4, 0.3, 0.1, -0.1],
                                [-0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, -0.2],
                                [-0.3, -0.2, -0.1, -0.1, -0.1, -0.1, -0.2, -0.3]],
                            
                            "K":[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [-0.1, -0.1, -0.2, -0.2, -0.2, -0.2, -0.1, -0.1],
                                [-0.1, -0.1, -0.4, -0.5, -0.5, -0.4, -0.1, -0.1],
                                [-0.1, -0.1, -0.4, -0.5, -0.5, -0.4, -0.1, -0.1],
                                [-0.1, -0.1, -0.2, -0.2, -0.2, -0.2, -0.1, -0.1],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]}

    for row in board:
        for square in row:
            if square != "":
                board_value += chess_value[square]

            '''
                if square.isupper() == False:
                    board_value += ((pieces_position_value[square.upper()])[board.index(row)][row.index(square)])*-1
                
                else:
                    board_value += (pieces_position_value[square])[board.index(row)][row.index(square)]
            '''    

    return board_value

def add_Depth(board, colour):
    childs = []
    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if board[b][a].upper() == "P" and board[b][a].isupper() == colour:
                temp = movements.Pawn(board, (0 if board[b][a].isupper() else 1), (b, a))
            
            elif board[b][a].upper() == "N" and board[b][a].isupper() == colour:
                temp = movements.Knight(board, (b, a))

            elif board[b][a].upper() == "R" and board[b][a].isupper() == colour:
                temp = movements.Rock(board, (b, a))
            
            elif board[b][a].upper() == "B" and board[b][a].isupper() == colour:
                temp = movements.Bishop(board, (b, a))
            
            elif board[b][a].upper() == "Q" and board[b][a].isupper() == colour:
                temp = movements.Queen(board, (b, a))
            
            elif  board[b][a].upper() == "K" and board[b][a].isupper() == colour:
                temp = movements.King(board, (0 if board[b][a].isupper() else 1), (b, a))

            for x in temp:
                temp_board = board
                temp_board[x[0]][x[1]] = board[b][a]
                temp_board[b][a] = ""

                '''
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

                
                if movements.King_Check(temp_board, same_king) and (movements.King_Check(board, other_king) or (movements.King_Check(board, other_king) == False and movements.King_Check(temp_board, other_king))):
                '''
                childs.append(temp_board)
    
    return childs

def min_value(board, alpha, beta, colour, depth):
    v = +inf

    node = add_Depth(board, (True if colour == False else False))


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

    for child in node:
        if depth < 3:
            v = max(v, min_value(child, alpha, beta, (True if colour == False else False), depth+1))

        else:
            v = Evaluate_Position(child)

        if v >= beta:
            return v
        
        alpha = max(alpha, v)
    
    return v

def root(board, alpha, beta, colour, depth, Queue):
    if colour == True:
        Queue.put("Depth: 4 | "+str(max_value(board, alpha, beta, colour, depth)))

    else:
        Queue.put("Depth: 4 | "+str(min_value(board, alpha, beta, colour, depth)))

def main(board, depth, colour):
    '''
    print("##########  INIT  ##########")
    print("Depth: ", str(depth))
    print("############################")

    pool = mp.Pool(4)
    image_list = [1]

    #p1 = pool.Process(target=max_value, args=[board, -inf, +inf, colour, 1])
    temp = partial(max_value, board, -inf, +inf, colour)
    result = pool.map(func=temp, iterable=image_list)
    #p1.start()
    #p1.join()
    pool.close()
    pool.join()

    print(result)

    '''

    print("##########  INIT  ##########")
    print("Depth: ", str(depth))
    print("############################")

    '''
    p1 = mp.Process(target=max_value, args=[board, -inf, +inf, colour, 1])
    p1.start()
    print(p1.get())
    p1.join()
    '''

    with concurrent.futures.ProcessPoolExecutor() as executor:
        p1 = executor.submit(max_value, board, -inf, +inf, colour, 1)
        print(p1.result())
    
    #print(max_value(board, -inf, +inf, colour, 1))


if __name__ == "__main__":
    main([["", "", "", "", "k", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "P"],
        ["", "", "", "", "K", "", "", ""]], 
        4, 
        False)

