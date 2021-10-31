#Llibreries importades
import pygame
from PIL import Image
from copy import deepcopy
import numpy as np

#Classe per a la construcció de la peça Peó
class Pawn(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, fliped, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite
        self.image = self.image.resize(size, resample=Image.BILINEAR , box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.fliped = fliped

        self.pos = pos #Posició de la peça
        self.id = "P" #ID de la peça

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Movement(self, board): #Funció que retorna una llista amb les caselles jugables per a la peça en concret
        mv = []
        k = (-1 if self.colour == 0 else 1)
        if self.fliped == True: k = k*(-1)

        if self.pos[0]+k <= 7:
            if board[self.pos[0]+k][self.pos[1]] == "":
                mv.append((self.pos[0]+k, self.pos[1]))
            
                if self.pos[0] == (1 if k == 1 else 6) and board[self.pos[0]+(k*2)][self.pos[1]] == "":
                    mv.append((self.pos[0]+(k*2), self.pos[1]))

            if self.pos[1]+1 <= 7 and board[self.pos[0]+k][self.pos[1]+1] != "" and board[self.pos[0]+k][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                mv.append((self.pos[0]+k, self.pos[1]+1))
                
            if self.pos[1]-1 <= 7 and board[self.pos[0]+k][self.pos[1]-1] != "" and board[self.pos[0]+k][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                mv.append((self.pos[0]+k, self.pos[1]-1))

        return mv

#Classe per a la construcció de la peça Dama
class Queen(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite
        self.image = self.image.resize(size, resample=Image.BILINEAR, box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)

        self.pos = pos #Posició de la peça
        self.id = "Q" #ID de la peça

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Movement(self, board): #Funció que retorna una llista amb les caselles jugables per a la peça en concret
        mv = []

        for x in range(1, 8):
            if (self.pos[0]+x <= 7 and self.pos[1]+x <= 7) and board[self.pos[0]+x][self.pos[1]+x] == "":
                mv.append((self.pos[0]+x, self.pos[1]+x))
            
            else:
                if (self.pos[0]+x <= 7 and self.pos[1]+x <= 7) and board[self.pos[0]+x][self.pos[1]+x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]+x, self.pos[1]+x))
                break
        
        for x in range(1, 8):
            if (self.pos[0]+x <= 7 and self.pos[1]-x >= 0) and board[self.pos[0]+x][self.pos[1]-x] == "":
                mv.append((self.pos[0]+x, self.pos[1]-x))
            
            else:
                if (self.pos[0]+x <= 7 and self.pos[1]-x >= 0) and board[self.pos[0]+x][self.pos[1]-x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]+x, self.pos[1]-x))
                break
        
        for x in range(1, 8):
            if (self.pos[0]-x >= 0 and self.pos[1]-x >= 0) and board[self.pos[0]-x][self.pos[1]-x] == "":
                mv.append((self.pos[0]-x, self.pos[1]-x))
            
            else:
                if (self.pos[0]-x >= 0 and self.pos[1]-x >= 0) and board[self.pos[0]-x][self.pos[1]-x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]-x, self.pos[1]-x))
                break

        for x in range(1, 8): 
            if (self.pos[0]-x >= 0 and self.pos[1]+x <= 7) and board[self.pos[0]-x][self.pos[1]+x] == "":
                mv.append((self.pos[0]-x, self.pos[1]+x))
            
            else:
                if (self.pos[0]-x >= 0 and self.pos[1]+x <= 7) and board[self.pos[0]-x][self.pos[1]+x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]-x, self.pos[1]+x))
                break
        
        for x in range(self.pos[0]+1, 8):
            if board[x][self.pos[1]] == "":
                mv.append((x, self.pos[1]))
            
            else:
                if board[x][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((x, self.pos[1]))
                break
        
        for x in range(self.pos[0]-1, -1, -1):
            if board[x][self.pos[1]] == "":
                mv.append((x, self.pos[1]))
            
            else:
                if board[x][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((x, self.pos[1]))
                break
        
        for x in range(self.pos[1]+1, 8):
            if board[self.pos[0]][x] == "":
                mv.append((self.pos[0], x))
            
            else:
                if board[self.pos[0]][x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0], x))
                break
        
        for x in range(self.pos[1]-1, -1, -1):
            if board[self.pos[0]][x] == "":
                mv.append((self.pos[0], x))
            
            else:
                if board[self.pos[0]][x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0], x))
                break

        return mv  

#Classe per a la construcció de la peça Cavall
class Knight(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite
        self.image = self.image.resize(size, resample=Image.BILINEAR, box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        
        self.pos = pos #Posició de la peça
        self.id = "N" #ID de la peça

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []

        if self.pos[0]+2 <= 7 and self.pos[1]+1 <= 7:
            if board[self.pos[0]+2][self.pos[1]+1] == "" or (board[self.pos[0]+2][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]+2, self.pos[1]+1))

        if self.pos[0]+2 <= 7 and self.pos[1]-1 >= 0:
            if board[self.pos[0]+2][self.pos[1]-1] == "" or (board[self.pos[0]+2][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]+2, self.pos[1]-1))
        
        if self.pos[0]-2 >= 0 and self.pos[1]+1 <= 7:
            if board[self.pos[0]-2][self.pos[1]+1] == "" or (board[self.pos[0]-2][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]-2, self.pos[1]+1))

        if self.pos[0]-2 >= 0 and self.pos[1]-1 >= 0:
            if board[self.pos[0]-2][self.pos[1]-1] == "" or (board[self.pos[0]-2][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]-2, self.pos[1]-1))

        if self.pos[0]+1 <= 7 and self.pos[1]+2 <= 7:
            if board[self.pos[0]+1][self.pos[1]+2] == "" or (board[self.pos[0]+1][self.pos[1]+2].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]+1, self.pos[1]+2))

        if self.pos[0]+1 <= 7 and self.pos[1]-2 >= 0:
            if board[self.pos[0]+1][self.pos[1]-2] == "" or (board[self.pos[0]+1][self.pos[1]-2].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]+1, self.pos[1]-2))
        
        if self.pos[0]-1 >= 0 and self.pos[1]+2 <= 7:
            if board[self.pos[0]-1][self.pos[1]+2] == "" or (board[self.pos[0]-1][self.pos[1]+2].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]-1, self.pos[1]+2))

        if self.pos[0]-1 >= 0 and self.pos[1]-2 >= 0:
            if board[self.pos[0]-1][self.pos[1]-2] == "" or (board[self.pos[0]-1][self.pos[1]-2].isupper() != board[self.pos[0]][self.pos[1]].isupper()):   mv.append((self.pos[0]-1, self.pos[1]-2))

        return mv

#Classe per a la construcció de la peça Àlfil
class Bishop(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite
        self.image = self.image.resize(size, resample=Image.BILINEAR, box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        
        self.pos = pos #Posició de la peça
        self.id = "B" #ID de la peça

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []

        for x in range(1, 8):
            if (self.pos[0]+x <= 7 and self.pos[1]+x <= 7) and board[self.pos[0]+x][self.pos[1]+x] == "":
                mv.append((self.pos[0]+x, self.pos[1]+x))
            
            else:
                if (self.pos[0]+x <= 7 and self.pos[1]+x <= 7) and board[self.pos[0]+x][self.pos[1]+x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]+x, self.pos[1]+x))
                break
        
        for x in range(1, 8):
            if (self.pos[0]+x <= 7 and self.pos[1]-x >= 0) and board[self.pos[0]+x][self.pos[1]-x] == "":
                mv.append((self.pos[0]+x, self.pos[1]-x))
            
            else:
                if (self.pos[0]+x <= 7 and self.pos[1]-x >= 0) and board[self.pos[0]+x][self.pos[1]-x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]+x, self.pos[1]-x))
                break
        
        for x in range(1, 8):
            if (self.pos[0]-x >= 0 and self.pos[1]-x >= 0) and board[self.pos[0]-x][self.pos[1]-x] == "":
                mv.append((self.pos[0]-x, self.pos[1]-x))
            
            else:
                if (self.pos[0]-x >= 0 and self.pos[1]-x >= 0) and board[self.pos[0]-x][self.pos[1]-x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]-x, self.pos[1]-x))
                break

        for x in range(1, 8): 
            if (self.pos[0]-x >= 0 and self.pos[1]+x <= 7) and board[self.pos[0]-x][self.pos[1]+x] == "":
                mv.append((self.pos[0]-x, self.pos[1]+x))
            
            else:
                if (self.pos[0]-x >= 0 and self.pos[1]+x <= 7) and board[self.pos[0]-x][self.pos[1]+x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0]-x, self.pos[1]+x))
                break

        return mv     

#Classe per a la construcció de la peça Torre
class Rock(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite
        self.image = self.image.resize(size, resample=Image.BILINEAR, box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        
        self.pos = pos #Posició de la peça
        self.id = "R" #ID de la peça
        self.h_moved = False #Atribut per a emmagatzemar si s'ha mogut

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = [] 

        for x in range(self.pos[0]+1, 8):
            if board[x][self.pos[1]] == "":
                mv.append((x, self.pos[1]))
            
            else:
                if board[x][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((x, self.pos[1]))
                break
        
        for x in range(self.pos[0]-1, -1, -1):
            if board[x][self.pos[1]] == "":
                mv.append((x, self.pos[1]))
            
            else:
                if board[x][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((x, self.pos[1]))
                break
        
        for x in range(self.pos[1]+1, 8):
            if board[self.pos[0]][x] == "":
                mv.append((self.pos[0], x))
            
            else:
                if board[self.pos[0]][x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0], x))
                break
        
        for x in range(self.pos[1]-1, -1, -1):
            if board[self.pos[0]][x] == "":
                mv.append((self.pos[0], x))
            
            else:
                if board[self.pos[0]][x].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                    mv.append((self.pos[0], x))
                break

        return mv

#Classe per a la construcció de la peça Rei
class King(pygame.sprite.Sprite):
    def __init__(self, sprite, colour, pos, fliped, size):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.colour = colour #Color de peça

        #Selecció i escalatge de l'imatge per a composar el seu sprite
        self.image = sprite.resize(size, resample=Image.BILINEAR, box=None)
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        
        self.pos = pos #Posició de la peça
        self.id = "K" #ID de la peça
        self.h_moved = False #Atribut per a emmagatzemar si s'ha mogut
        self.fliped = fliped #Atribut per a emmagatzemar si el taulell està rotat

        self.rect = self.image.get_rect() #Posició del collider del sprite en funció de les dimensions de la seva imatge
    
    def Check(self, board, pos):
        local_id = board[pos[0]][pos[1]]

        modificadores_diagonales = [(-1 , -1), (1, 1), (-1, 1), (1, -1)]
        modificadores_lineales = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        agressiveKnight = 0

        for x in range(1, 8):
            temp_vectorlist_1 = deepcopy(modificadores_diagonales)

            for y in range(0, len(modificadores_diagonales)):
                temp_vect = np.array(pos)+(x*np.array(modificadores_diagonales[y]))

                if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0]][temp_vect[1]].isupper() != board[pos[0]][pos[1]].isupper() or board[temp_vect[0]][temp_vect[1]] == ""):
                    if board[temp_vect[0]][temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                        if x == 1 and (modificadores_diagonales[y] == ((-1, -1) if local_id.islower() else (-1, 1)) or modificadores_diagonales[y] == ((1, 1) if local_id.islower() else (1, -1))):
                            #print("Gate: 1 (DIAGONAL_1)")
                            return False

                        else:
                            temp_vectorlist_1.remove(modificadores_diagonales[y])
                            break
                    
                    if (0 < x <= 2) and board[temp_vect[0]][temp_vect[1]] == ("n" if local_id.isupper() else "N"):
                        agressiveKnight += 1
                        temp_vectorlist_1.remove(modificadores_diagonales[y])
                        break
                    
                    if x == 1 and board[temp_vect[0]][temp_vect[1]] == ("k" if local_id.isupper() else "K"):
                        #print("Gate: 1 (DIAGONAL_2)")
                        return False

                    if board[temp_vect[0]][temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0]][temp_vect[1]] == ("b" if local_id.isupper() else "B"):
                        #print("Gate: 1 (DIAGONAL)")
                        return False
                
                else:
                    temp_vectorlist_1.remove(modificadores_diagonales[y])

            modificadores_diagonales = deepcopy(temp_vectorlist_1)
            temp_vectorlist_2 = deepcopy(modificadores_lineales)
            
            for y in range(0, len(modificadores_lineales)):
                temp_vect = np.array(pos)+(x*np.array(modificadores_lineales[y]))

                if 0 <= temp_vect[0] <= 7 and 0 <= temp_vect[1] <= 7 and (board[temp_vect[0]][temp_vect[1]].isupper() != board[pos[0]][pos[1]].isupper() or board[temp_vect[0]][temp_vect[1]] == ""):                    
                    if board[temp_vect[0]][temp_vect[1]] == ("p" if local_id.isupper() else "P"):
                        if x == 1 and 0 <= temp_vect[0]+(modificadores_lineales[y])[0] <= 7 and 0 <= temp_vect[1]+(modificadores_lineales[y])[1] <= 7:
                            if board[temp_vect[0]+(modificadores_lineales[y])[0]][temp_vect[1]+(modificadores_lineales[y])[1]] == ("n" if local_id.isupper() else "N"):
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
                        #print("Gate: 2 (LINEAL_1)")
                        return False

                    if board[temp_vect[0]][temp_vect[1]] == ("q" if local_id.isupper() else "Q") or board[temp_vect[0]][temp_vect[1]] == ("r" if local_id.isupper() else "R"):
                        #print("Gate: 2 (LINEAL)")
                        return False
                
                else:
                    temp_vectorlist_2.remove(modificadores_lineales[y])

            modificadores_lineales = deepcopy(temp_vectorlist_2)

        local_knights = 0
        for a in range(0, 8):
            for b in range(0, 8):
                if board[b][a] == ("n" if local_id.isupper() else "N") and pos[0]-2 <= b <= pos[0]+2 and pos[1]-2 <= a <= pos[1]+2:
                    local_knights += 1

        if local_knights != agressiveKnight:
            #print("Gate: 2 (HORSE)")
            return False                

        #print("Gate: 3 (No check)")
        return True

    
    def Castling(self, board, h_moved):
        local_castling = (False, False)
        k = (1 if self.fliped == False else -1)

        if h_moved == False and 0 <= self.pos[1]+(2*k) <= 7:
            f_board_1 = deepcopy(board)
            f_board_1[self.pos[0]][self.pos[1]+(1*k)] = "K" if self.colour == 0 else "k"
            f_board_1[self.pos[0]][self.pos[1]] = ""

            f_board_2 = deepcopy(board)
            f_board_2[self.pos[0]][self.pos[1]+(2*k)] = "K" if self.colour == 0 else "k"
            f_board_2[self.pos[0]][self.pos[1]] = ""

            if (board[self.pos[0]][self.pos[1]+(1*k)] == "" and King.Check(self, f_board_1, (self.pos[0], self.pos[1]+(1*k)))) and (board[self.pos[0]][self.pos[1]+(2*k)] == "" and King.Check(self, f_board_2, (self.pos[0], self.pos[1]+(2*k)))) and board[self.pos[0]][self.pos[1]+(3*k)] == ("R" if board[self.pos[0]][self.pos[1]].isupper() else "r"):
                local_castling = (True, local_castling[1])
        
        if h_moved == False and 0 <= self.pos[1]+(-3*k) <= 7:
            f_board = deepcopy(board)
            f_board[self.pos[0]][self.pos[1]-1*k] = "K" if self.colour == 0 else "k"
            f_board[self.pos[0]][self.pos[1]] = ""

            f_board_1 = deepcopy(board)
            f_board_1[self.pos[0]][self.pos[1]-2*k] = ("K" if self.colour == 0 else "k")
            f_board_1[self.pos[0]][self.pos[1]] = ""

            f_board_2 = deepcopy(board)
            f_board_2[self.pos[0]][self.pos[1]-3*k] = "K" if self.colour == 0 else "k"
            f_board_2[self.pos[0]][self.pos[1]] = ""

            if (board[self.pos[0]][self.pos[1]-1*k] == "" and King.Check(self, f_board, (self.pos[0], self.pos[1]-1*k))) and (board[self.pos[0]][self.pos[1]-2*k] == "" and King.Check(self, f_board_1, (self.pos[0], self.pos[1]-2*k))) and (board[self.pos[0]][self.pos[1]-3*k] == "" and King.Check(self, f_board_2, (self.pos[0], self.pos[1]-3*k))) and board[self.pos[0]][self.pos[1]-4*k] == ("R" if board[self.pos[0]][self.pos[1]].isupper() else "r"):
                local_castling = (local_castling[0], True)

        return local_castling

    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []
        k = 1 if self.colour == 1 else -1

        if self.pos[0]+1 <= 7 and (board[self.pos[0]+1][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]+1][self.pos[1]] == ""):          

            mv.append((self.pos[0]+1, self.pos[1]))
                
        if self.pos[0]-1 >= 0 and (board[self.pos[0]-1][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]-1][self.pos[1]] == ""):

            mv.append((self.pos[0]-1, self.pos[1]))
        
        if self.pos[1]+1 <= 7 and (board[self.pos[0]][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]][self.pos[1]+1] == ""):

            mv.append((self.pos[0], self.pos[1]+1))
        
        if self.pos[1]-1 >= 0 and (board[self.pos[0]][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]][self.pos[1]-1] == ""):

            mv.append((self.pos[0], self.pos[1]-1))
        
        if self.pos[0]+1 <= 7 and self.pos[1]+1 <= 7 and (board[self.pos[0]+1][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]+1][self.pos[1]+1] == ""):

            mv.append((self.pos[0]+1, self.pos[1]+1))
        
        if self.pos[0]+1 <= 7 and self.pos[1]-1 >= 0 and (board[self.pos[0]+1][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]+1][self.pos[1]-1] == ""):

            mv.append((self.pos[0]+1, self.pos[1]-1))
        
        if self.pos[0]-1 >= 0 and self.pos[1]+1 <= 7 and (board[self.pos[0]-1][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]-1][self.pos[1]+1] == ""):

            mv.append((self.pos[0]-1, self.pos[1]+1))
        
        if self.pos[0]-1 >= 0 and self.pos[1]-1 >= 0 and (board[self.pos[0]-1][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper() or board[self.pos[0]-1][self.pos[1]-1] == ""):

            mv.append((self.pos[0]-1, self.pos[1]-1))

        return mv

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.status = []
        self.im = 0

        images = Image.open("images/manu_pressed.png")
        self.image1 = images.crop((0, 146.5, 150, 293))
        self.image1 = self.image1.resize((70, 70), resample=Image.BILINEAR, box=None)
        self.image1 = pygame.image.fromstring(self.image1.tobytes(), self.image1.size, self.image1.mode)
        self.status.append(self.image1)

        self.image2 = images.crop((0, 0, 150, 144))
        self.image2 = self.image2.resize((70, 70), resample=Image.BILINEAR, box=None)
        self.image2 = pygame.image.fromstring(self.image2.tobytes(), self.image2.size, self.image2.mode)
        self.status.append(self.image2)

        self.image = self.status[self.im]

        self.k = 2

        self.rect = self.image.get_rect()
    
    def Update(self):
        self.im = 1 if self.im == 0 else 0
        self.image = self.status[self.im]

class Render_Image(pygame.sprite.Sprite):
    def __init__(self, image_path, image_size, k):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.status = [] #Llista per a recollir les dues imatges del botó (encés/apagat)
        self.im = 0 #Posició (encés/apagat) del botó

        image = Image.open(image_path) #Obrim l'imatge amb el mòdul PIL

        #Selecció i escalatge de l'imatge 1
        self.image1 = image.resize(image_size, resample=Image.BILINEAR, box=None)
        self.image1 = pygame.image.fromstring(self.image1.tobytes(), self.image1.size, self.image1.mode)
        self.status.append(self.image1)

        self.image = self.image1 #Determinem la imatge en funció del seu estatus o posició
        self.id = k #ID del botó
        self.rect = self.image.get_rect() #Posició del collider del botó

#Classe per a la construcció d'un botó
class Button(pygame.sprite.Sprite):
    def __init__(self, image_object, image1_crop, image2_crop, image_size, k):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.status = [] #Llista per a recollir les dues imatges del botó (encés/apagat)
        self.im = 0 #Posició (encés/apagat) del botó

        image = image_object

        #Selecció i escalatge de l'imatge 1
        self.image1 = image.crop(image1_crop)
        self.image1 = self.image1.resize(image_size, resample=Image.BILINEAR, box=None)
        self.image1 = pygame.image.fromstring(self.image1.tobytes(), self.image1.size, self.image1.mode)
        self.status.append(self.image1)

        #Selecció i escalatge de l'imatge 1
        self.image2 = image.crop(image2_crop)
        self.image2 = self.image2.resize(image_size, resample=Image.BILINEAR, box=None)
        self.image2 = pygame.image.fromstring(self.image2.tobytes(), self.image2.size, self.image2.mode)
        self.status.append(self.image2)

        self.image = self.status[self.im] #Determinem la imatge en funció del seu estatus o posició
        self.id = k #ID del botó
        self.rect = self.image.get_rect() #Posició del collider del botó

    def Update(self): #Funció per a actualitzar la posició de la imatge (encés/apagat)
        self.im = 1 if self.im == 0 else 0
        self.image = self.status[self.im]

class Arrow_Button(pygame.sprite.Sprite):
    def __init__(self, sprite, image1_crop, image_size, k, proportion):
        super().__init__() #Herència dels atributs de la classe Sprite de pygame
        #Atributs de classe
        self.status = {} #Llista per a recollir les dues imatges del botó (encés/apagat)
        self.im = 0 #Posició (encés/apagat) del botó

        image = sprite

        temp_list = []
        for a in range(0, 21):
            #Selecció i escalatge de l'imatge 1
            self.image1 = image.crop(image1_crop)
            self.image1 = self.image1.resize(image_size, resample=Image.BILINEAR, box=None)
            self.image1 = self.image1.rotate(a*9, expand=False)
            self.image1 = pygame.image.fromstring(self.image1.tobytes(), self.image1.size, self.image1.mode)
            temp_list.append(self.image1)
        
        self.status["0"] = temp_list

        self.image = (self.status["0"])[self.im] #Determinem la imatge en funció del seu estatus o posició
        self.id = k #ID del botó
        self.rect = self.image.get_rect() #Posició del collider del botó
        #self.rect.center = (pos[0]+(image_size[0]/2), pos[1]+(image_size[1]/2))

    def Update(self, direction): #Funció per a actualitzar la posició de la imatge (encés/apagat)
        if 0 <= self.im <= 20:
            self.im += (direction)
            self.image = self.status["0"][self.im]