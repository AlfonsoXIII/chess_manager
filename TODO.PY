#TODO: Completar sistema GameOver & Reset
import chess_notations
import numpy as np
from copy import deepcopy

def Check(board, pos):
    local_id = board[pos[0]][pos[1]]

    modificadores_diagonales = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    modificadores_lineales = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    agressiveKnight = 0

    for x in range(1, 8):
        temp_vectorlist_1 = deepcopy(modificadores_diagonales)

        for y in range(0, len(modificadores_diagonales)):
            temp_vect = np.array(pos)+(x*np.array(modificadores_diagonales[y]))

            if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0]][temp_vect[1]].isupper() != board[pos[0]][pos[1]].isupper() or board[temp_vect[0]][temp_vect[1]] == ""):
                if board[temp_vect[0]][temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                    if x == 1 and (modificadores_diagonales[y] == ((-1, -1) if local_id.islower() else (-1, 1)) or modificadores_diagonales[y] == ((1, 1) if local_id.islower() else (1, -1))):
                        print("Gate: 1 (DIAGONAL_1)")
                        return False

                    else:
                        temp_vectorlist_1.remove(modificadores_diagonales[y])
                        break
                
                if (0 < x <= 2) and board[temp_vect[0]][temp_vect[1]] == ("n" if local_id.isupper() else "N"):
                    agressiveKnight += 1
                    temp_vectorlist_1.remove(modificadores_diagonales[y])
                    break
                
                if x == 1 and board[temp_vect[0]][temp_vect[1]] == ("k" if local_id.isupper() else "K"):
                    print("Gate: 1 (DIAGONAL_2)")
                    return False

                if board[temp_vect[0]][temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0]][temp_vect[1]] == ("b" if local_id.isupper() else "B"):
                    print("Gate: 1 (DIAGONAL)")
                    return False
            
            else:
                temp_vectorlist_1.remove(modificadores_diagonales[y])

        modificadores_diagonales = deepcopy(temp_vectorlist_1)
        temp_vectorlist_2 = deepcopy(modificadores_lineales)
        
        for y in range(0, len(modificadores_lineales)):
            temp_vect = np.array(pos)+(x*np.array(modificadores_lineales[y]))

            if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0]][temp_vect[1]].isupper() != board[pos[0]][pos[1]].isupper() or board[temp_vect[0]][temp_vect[1]] == ""):
                if board[temp_vect[0]][temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                    if x == 1 and board[temp_vect[0]+(modificadores_lineales[y])[0]][temp_vect[1]+(modificadores_lineales[y])[1]] == ("n" if local_id.isupper() else "N"):
                        agressiveKnight += 1
                        temp_vectorlist_2.remove(modificadores_lineales[y])
                        break

                    else:
                        temp_vectorlist_2.remove(modificadores_lineales[y])
                        break
                
                if (x != 0 and x <= 2) and board[temp_vect[0]][temp_vect[1]] == ("n" if local_id.isupper() else "N"):
                    agressiveKnight += 1
                    temp_vectorlist_2.remove(modificadores_lineales[y])
                    break

                if x == 1 and board[temp_vect[0]][temp_vect[1]] == ("k" if local_id.isupper() else "K"):
                    print("Gate: 2 (LINEAL_1)")
                    return False

                if board[temp_vect[0]][temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0]][temp_vect[1]] == ("r" if local_id.isupper() else "R"):
                    #print(board[temp_vect[0]][temp_vect[1]])
                    print("Gate: 2 (LINEAL)")
                    return False
            
            else:
                print(modificadores_lineales[y])
                temp_vectorlist_2.remove(modificadores_lineales[y])
                print(temp_vectorlist_2)

        modificadores_lineales = deepcopy(temp_vectorlist_2)
        print(modificadores_lineales)

    local_knights = 0
    for a in range(0, 8):
        for b in range(0, 8):
            if board[b][a] == ("n" if local_id.isupper() else "N") and pos[0]-2 <= b <= pos[0]+2 and pos[1]-2 <= a <= pos[1]+2:
                local_knights += 1

    if local_knights != agressiveKnight:
        print("Gate: 2 (HORSE)")
        return False                

    print("Gate: 3 (No check)")
    return True

print(Check(chess_notations.FEN_decode("8/8/3k4/4P3/8/8/8/6K1"), (2, 3)))