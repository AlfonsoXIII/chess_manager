#Mòduls importats
from copy import deepcopy
import numpy as np

def Pawn(board, colour, pos):
    mv = []
    k = (-1 if colour == 0 else 1)
    #if self.fliped == True: k = k*(-1)

    if 0 <= pos[0]+k <= 7:
        if board[pos[0]+k, pos[1]] == "":
            mv.append((pos[0]+k, pos[1]))
        
            if pos[0] == (1 if k == 1 else 6) and board[pos[0]+(k*2), pos[1]] == "":
                mv.append((pos[0]+(k*2), pos[1]))

        if 0 <= pos[1]+1 <= 7 and board[pos[0]+k, pos[1]+1] != "" and board[pos[0]+k, pos[1]+1].isupper() != board[pos[0], pos[1]].isupper():
            mv.append((pos[0]+k, pos[1]+1))
            
        if 0 <= pos[1]-1 <= 7 and board[pos[0]+k, pos[1]-1] != "" and board[pos[0]+k, pos[1]-1].isupper() != board[pos[0], pos[1]].isupper():
            mv.append((pos[0]+k, pos[1]-1))

    return mv

def Queen(board, pos):
    mv = []
    
    for x in range(1, 8):
        if (pos[0]+x <= 7 and pos[1]+x <= 7) and board[pos[0]+x, pos[1]+x] == "":
            mv.append((pos[0]+x, pos[1]+x))
        
        else:
            if (pos[0]+x <= 7 and pos[1]+x <= 7) and board[pos[0]+x, pos[1]+x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]+x, pos[1]+x))
            break

    for x in range(1, 8):
        if (pos[0]+x <= 7 and pos[1]-x >= 0) and board[pos[0]+x][pos[1]-x] == "":
            mv.append((pos[0]+x, pos[1]-x))
        
        else:
            if (pos[0]+x <= 7 and pos[1]-x >= 0) and board[pos[0]+x, pos[1]-x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]+x, pos[1]-x))
            break

    for x in range(1, 8):
        if (pos[0]-x >= 0 and pos[1]-x >= 0) and board[pos[0]-x, pos[1]-x] == "":
            mv.append((pos[0]-x, pos[1]-x))
        
        else:
            if (pos[0]-x >= 0 and pos[1]-x >= 0) and board[pos[0]-x, pos[1]-x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]-x, pos[1]-x))
            break

    for x in range(1, 8): 
        if (pos[0]-x >= 0 and pos[1]+x <= 7) and board[pos[0]-x, pos[1]+x] == "":
            mv.append((pos[0]-x, pos[1]+x))
        
        else:
            if (pos[0]-x >= 0 and pos[1]+x <= 7) and board[pos[0]-x, pos[1]+x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]-x, pos[1]+x))
            break

    for x in range(pos[0]+1, 8):
        if board[x, pos[1]] == "":
            mv.append((x, pos[1]))
        
        else:
            if board[x, pos[1]].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((x, pos[1]))
            break

    for x in range(pos[0]-1, -1, -1):
        if board[x, pos[1]] == "":
            mv.append((x, pos[1]))
        
        else:
            if board[x, pos[1]].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((x, pos[1]))
            break

    for x in range(pos[1]+1, 8):
        if board[pos[0]][x] == "":
            mv.append((pos[0], x))
        
        else:
            if board[pos[0], x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0], x))
            break

    for x in range(pos[1]-1, -1, -1):
        if board[pos[0], x] == "":
            mv.append((pos[0], x))
        
        else:
            if board[pos[0], x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0], x))
            break

    return mv 

def Knight(board, pos):
    mv = []
    
    if pos[0]+2 <= 7 and pos[1]+1 <= 7:
        if board[pos[0]+2, pos[1]+1] == "" or (board[pos[0]+2, pos[1]+1].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]+2, pos[1]+1))

    if pos[0]+2 <= 7 and pos[1]-1 >= 0:
        if board[pos[0]+2, pos[1]-1] == "" or (board[pos[0]+2, pos[1]-1].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]+2, pos[1]-1))
    
    if pos[0]-2 >= 0 and pos[1]+1 <= 7:
        if board[pos[0]-2, pos[1]+1] == "" or (board[pos[0]-2, pos[1]+1].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]-2, pos[1]+1))

    if pos[0]-2 >= 0 and pos[1]-1 >= 0:
        if board[pos[0]-2, pos[1]-1] == "" or (board[pos[0]-2, pos[1]-1].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]-2, pos[1]-1))

    if pos[0]+1 <= 7 and pos[1]+2 <= 7:
        if board[pos[0]+1, pos[1]+2] == "" or (board[pos[0]+1, pos[1]+2].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]+1, pos[1]+2))

    if pos[0]+1 <= 7 and pos[1]-2 >= 0:
        if board[pos[0]+1, pos[1]-2] == "" or (board[pos[0]+1, pos[1]-2].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]+1, pos[1]-2))
    
    if pos[0]-1 >= 0 and pos[1]+2 <= 7:
        if board[pos[0]-1, pos[1]+2] == "" or (board[pos[0]-1, pos[1]+2].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]-1, pos[1]+2))

    if pos[0]-1 >= 0 and pos[1]-2 >= 0:
        if board[pos[0]-1, pos[1]-2] == "" or (board[pos[0]-1, pos[1]-2].isupper() != board[pos[0], pos[1]].isupper()):   mv.append((pos[0]-1, pos[1]-2))

    return mv

def Bishop(board, pos):
    mv = []

    for x in range(1, 8):
        if (pos[0]+x <= 7 and pos[1]+x <= 7) and board[pos[0]+x, pos[1]+x] == "":
            mv.append((pos[0]+x, pos[1]+x))
        
        else:
            if (pos[0]+x <= 7 and pos[1]+x <= 7) and board[pos[0]+x, pos[1]+x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]+x, pos[1]+x))
            break
    
    for x in range(1, 8):
        if (pos[0]+x <= 7 and pos[1]-x >= 0) and board[pos[0]+x][pos[1]-x] == "":
            mv.append((pos[0]+x, pos[1]-x))
        
        else:
            if (pos[0]+x <= 7 and pos[1]-x >= 0) and board[pos[0]+x, pos[1]-x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]+x, pos[1]-x))
            break
    
    for x in range(1, 8):
        if (pos[0]-x >= 0 and pos[1]-x >= 0) and board[pos[0]-x, pos[1]-x] == "":
            mv.append((pos[0]-x, pos[1]-x))
        
        else:
            if (pos[0]-x >= 0 and pos[1]-x >= 0) and board[pos[0]-x, pos[1]-x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]-x, pos[1]-x))
            break

    for x in range(1, 8): 
        if (pos[0]-x >= 0 and pos[1]+x <= 7) and board[pos[0]-x, pos[1]+x] == "":
            mv.append((pos[0]-x, pos[1]+x))
        
        else:
            if (pos[0]-x >= 0 and pos[1]+x <= 7) and board[pos[0]-x, pos[1]+x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0]-x, pos[1]+x))
            break

    return mv 

def Rock(board, pos):
    mv = [] 

    for x in range(pos[0]+1, 8):
        if board[x, pos[1]] == "":
            mv.append((x, pos[1]))
        
        else:
            if board[x, pos[1]].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((x, pos[1]))
            break
    
    for x in range(pos[0]-1, -1, -1):
        if board[x, pos[1]] == "":
            mv.append((x, pos[1]))
        
        else:
            if board[x, pos[1]].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((x, pos[1]))
            break
    
    for x in range(pos[1]+1, 8):
        if board[pos[0], x] == "":
            mv.append((pos[0], x))
        
        else:
            if board[pos[0], x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0], x))
            break
    
    for x in range(pos[1]-1, -1, -1):
        if board[pos[0], x] == "":
            mv.append((pos[0], x))
        
        else:
            if board[pos[0], x].isupper() != board[pos[0], pos[1]].isupper():
                mv.append((pos[0], x))
            break

    return mv

def King_Check(board, pos):
    local_id = board[pos[0], pos[1]]

    modificadores_diagonales = [(-1 , -1), (1, 1), (-1, 1), (1, -1)]
    modificadores_lineales = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    agressiveKnight = 0

    for x in range(1, 8):
        temp_vectorlist_1 = deepcopy(modificadores_diagonales)

        for y in range(0, len(modificadores_diagonales)):
            temp_vect = np.array(pos)+(x*np.array(modificadores_diagonales[y]))

            if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0], temp_vect[1]].isupper() != board[pos[0], pos[1]].isupper() or board[temp_vect[0], temp_vect[1]] == ""):
                if board[temp_vect[0], temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                    if x == 1 and (modificadores_diagonales[y] == ((-1, -1) if local_id.islower() else (-1, 1)) or modificadores_diagonales[y] == ((1, 1) if local_id.islower() else (1, -1))):
                        #print("Gate: 1 (DIAGONAL_1)")
                        return False

                    else:
                        temp_vectorlist_1.remove(modificadores_diagonales[y])
                        break
                
                if (0 < x <= 2) and board[temp_vect[0], temp_vect[1]] == ("n" if local_id.isupper() else "N"):
                    agressiveKnight += 1
                    temp_vectorlist_1.remove(modificadores_diagonales[y])
                    break
                
                if x == 1 and board[temp_vect[0], temp_vect[1]] == ("k" if local_id.isupper() else "K"):
                    #print("Gate: 1 (DIAGONAL_2)")
                    return False

                if board[temp_vect[0], temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0], temp_vect[1]] == ("b" if local_id.isupper() else "B"):
                    #print("Gate: 1 (DIAGONAL)")
                    return False
            
            else:
                temp_vectorlist_1.remove(modificadores_diagonales[y])

        modificadores_diagonales = deepcopy(temp_vectorlist_1)
        temp_vectorlist_2 = deepcopy(modificadores_lineales)
        
        for y in range(0, len(modificadores_lineales)):
            temp_vect = np.array(pos)+(x*np.array(modificadores_lineales[y]))

            if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0], temp_vect[1]].isupper() != board[pos[0], pos[1]].isupper() or board[temp_vect[0], temp_vect[1]] == ""):                    
                if board[temp_vect[0], temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                    if x == 1 and 0 <= temp_vect[0]+(modificadores_lineales[y])[0] <= 7 and 0 <= temp_vect[1]+(modificadores_lineales[y])[1] <= 7:
                        if board[temp_vect[0]+(modificadores_lineales[y])[0], temp_vect[1]+(modificadores_lineales[y])[1]] == ("n" if local_id.isupper() else "N"):
                            agressiveKnight += 1
                            temp_vectorlist_2.remove(modificadores_lineales[y])
                            break

                        else:
                            temp_vectorlist_2.remove(modificadores_lineales[y])
                            break
                
                if (x != 0 and x <= 2) and board[temp_vect[0], temp_vect[1]] == ("n" if local_id.isupper() else "N"):
                    agressiveKnight += 1
                    temp_vectorlist_2.remove(modificadores_lineales[y])
                    break

                if x == 1 and board[temp_vect[0], temp_vect[1]] == ("k" if local_id.isupper() else "K"):
                    #print("Gate: 2 (LINEAL_1)")
                    return False

                if board[temp_vect[0], temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0], temp_vect[1]] == ("r" if local_id.isupper() else "R"):
                    #print("Gate: 2 (LINEAL)")
                    return False
            
            else:
                temp_vectorlist_2.remove(modificadores_lineales[y])

        modificadores_lineales = deepcopy(temp_vectorlist_2)

    local_knights = 0
    for a in range(0, 8):
        for b in range(0, 8):
            if board[b, a] == ("n" if local_id.isupper() else "N") and pos[0]-2 <= b <= pos[0]+2 and pos[1]-2 <= a <= pos[1]+2:
                local_knights += 1

    if local_knights != agressiveKnight:
        #print("Gate: 2 (HORSE)")
        return False                

    #print("Gate: 3 (No check)")
    return True

def King(board, colour, pos):
    mv = []
    k = (1 if colour == 1 else -1)

    if pos[0]+1 <= 7 and (board[pos[0]+1, pos[1]].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]+1, pos[1]] == ""):          

        mv.append((pos[0]+1, pos[1]))
            
    if pos[0]-1 >= 0 and (board[pos[0]-1, pos[1]].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]-1, pos[1]] == ""):

        mv.append((pos[0]-1, pos[1]))
    
    if pos[1]+1 <= 7 and (board[pos[0], pos[1]+1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0], pos[1]+1] == ""):

        mv.append((pos[0], pos[1]+1))
    
    if pos[1]-1 >= 0 and (board[pos[0], pos[1]-1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0], pos[1]-1] == ""):

        mv.append((pos[0], pos[1]-1))
    
    if pos[0]+1 <= 7 and pos[1]+1 <= 7 and (board[pos[0]+1, pos[1]+1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]+1, pos[1]+1] == ""):

        mv.append((pos[0]+1, pos[1]+1))
    
    if pos[0]+1 <= 7 and pos[1]-1 >= 0 and (board[pos[0]+1, pos[1]-1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]+1, pos[1]-1] == ""):

        mv.append((pos[0]+1, pos[1]-1))
    
    if pos[0]-1 >= 0 and pos[1]+1 <= 7 and (board[pos[0]-1, pos[1]+1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]-1, pos[1]+1] == ""):

        mv.append((pos[0]-1, pos[1]+1))
    
    if pos[0]-1 >= 0 and pos[1]-1 >= 0 and (board[pos[0]-1, pos[1]-1].isupper() != board[pos[0], pos[1]].isupper() or board[pos[0]-1, pos[1]-1] == ""):

        mv.append((pos[0]-1, pos[1]-1))

    return mv