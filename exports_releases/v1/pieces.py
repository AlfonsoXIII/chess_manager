#Diversas librerias, y parámetros de estas, importadas
import pygame
from PIL import Image

class Pawn(pygame.sprite.Sprite): #Clase para la construcción de un Peón
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((200, 40-self.colour*40, 240, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.pos = pos
        self.id = "P"

        self.rect = self.image.get_rect()
    
    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []
        k = 1 if self.colour == 1 else -1

        if self.pos[0]+k <= 7:
            if board[self.pos[0]+k][self.pos[1]] == "":
                    mv.append((self.pos[0]+k, self.pos[1]))
            
            if self.pos[0] == (1 if self.colour == 1 else 6) and board[self.pos[0]+(k*2)][self.pos[1]] == "":
                mv.append((self.pos[0]+(k*2), self.pos[1]))

            if self.pos[1]+1 <= 7 and board[self.pos[0]+k][self.pos[1]+1] != "" and board[self.pos[0]+k][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                mv.append((self.pos[0]+k, self.pos[1]+1))
                
            if self.pos[1]-1 <= 7 and board[self.pos[0]+k][self.pos[1]-1] != "" and board[self.pos[0]+k][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper():
                mv.append((self.pos[0]+k, self.pos[1]-1))

        return mv

        

class King(pygame.sprite.Sprite):
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((40, 40-self.colour*40, 80, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.id = "K"

        self.rect = self.image.get_rect()

    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []
        k = 1 if self.colour == 1 else -1

        if self.pos[0]+1 <= 7:
            if board[self.pos[0]+1][self.pos[1]] == "" or board[self.pos[0]+1][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]+1, self.pos[1]))
        
        if self.pos[0]-1 >= 0:
            if board[self.pos[0]-1][self.pos[1]] == "" or board[self.pos[0]-1][self.pos[1]].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]-1, self.pos[1]))
        
        if self.pos[1]+1 <= 7:
            if board[self.pos[0]][self.pos[1]+1] == "" or board[self.pos[0]][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0], self.pos[1]+1))
        
        if self.pos[1]-1 >= 0:
            if board[self.pos[0]][self.pos[1]-1] == "" or board[self.pos[0]][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0], self.pos[1]-1))
        
        if self.pos[0]+1 <= 7 and self.pos[1]+1 <= 7:
            if board[self.pos[0]+1][self.pos[1]+1] == "" or board[self.pos[0]+1][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]+1, self.pos[1]+1))
        
        if self.pos[0]+1 <= 7 and self.pos[0]-1 >= 0:
            if board[self.pos[0]+1][self.pos[1]-1] == "" or board[self.pos[0]+1][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]+1, self.pos[1]-1))
        
        if self.pos[0]-1 >= 0 and self.pos[1]+1 <= 7:
            if board[self.pos[0]-1][self.pos[1]+1] == "" or board[self.pos[0]-1][self.pos[1]+1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]-1, self.pos[1]+1))
        
        if self.pos[0]-1 >= 0 and self.pos[1]-1 >= 0:
            if board[self.pos[0]-1][self.pos[1]-1] == "" or board[self.pos[0]-1][self.pos[1]-1].isupper() != board[self.pos[0]][self.pos[1]].isupper(): mv.append((self.pos[0]-1, self.pos[1]-1))

        return mv

class Queen(pygame.sprite.Sprite):
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((0, 40-self.colour*40, 40, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.id = "Q"

        self.rect = self.image.get_rect()
    
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

class Knight(pygame.sprite.Sprite):
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((120, 40-self.colour*40, 160, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.id = "N"

        self.rect = self.image.get_rect()
    
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

class Bishop(pygame.sprite.Sprite):
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((160, 40-self.colour*40, 200, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.id = "B"

        self.rect = self.image.get_rect()
    
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

class Rock(pygame.sprite.Sprite):
    def __init__(self, colour, pos):
        super().__init__()
        #Atributos de clase
        self.colour = colour

        images = Image.open("images/chess_pieces.png")
        self.image = images.crop((80, 40-self.colour*40, 120, 80-self.colour*40))
        self.image = pygame.image.fromstring(self.image.tobytes(), self.image.size, self.image.mode)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.id = "R"

        self.rect = self.image.get_rect()
    
    def Movement(self, board): #Función que retorna las casillas disponibles para el movimiento de la pieza
        mv = []        
        #if any(board[x][self.pos[1]] != "" for x in range(self.pos[0]+1, 8)): mv.append((x, self.pos[1]))
        #if any(board[(a:=x)][self.pos[1]] == "" for x in range(self.pos[0]+1, 8)): mv.append((a, self.pos[1]))

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