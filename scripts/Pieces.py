#Llibreries importades
import pygame

#Scripts importats
import scripts.Objects as pieces

#Classe que compren i gestiona totes les peces del taulell
class Pieces():
    def __init__(self, screen, b_size, b_len, position):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.b_size = b_size #
        self.b_len = b_len #
        self.position = position[-1] #Array amb la posició a visualitzar del taulell

        self.c_g = pygame.sprite.Group() #Grup pygame per a emmagatzemar un conjunt de sprites
        self.mp = [] #Llistat amb les caselles a les que pot anar la peça seleccionada

    def draw(self, reverse): #Dibuixat en pantalla de les peces
        #Neteja dels sprites prèvis
        self.c_g = []
        self.c_g = pygame.sprite.Group()

        #Creació de les peces i disposició de les seves coordenades
        for i in range(0, 8):
            for z in range(0 ,8):
                #Determinació de l'atribut color de les peces
                cl = 0 if self.position[z][i].isupper() else 1

                #Creació de la peça Peó
                if self.position[z][i].capitalize() == "P":
                    pawn = pieces.Pawn(cl, (z, i), reverse)

                    pawn.rect.x = 30+self.b_size*(i)
                    pawn.rect.y = 120+self.b_size*(z)

                    self.c_g.add(pawn)
                
                #Creació de la peça Rei
                elif self.position[z][i].capitalize() == "K":
                    king = pieces.King(cl, (z, i), reverse)

                    king.rect.x = 30+self.b_size*(i)
                    king.rect.y = 120+self.b_size*(z)

                    self.c_g.add(king)
                
                #Creació de la peça Dama
                elif self.position[z][i].capitalize() == "Q":
                    queen = pieces.Queen(cl, (z, i))

                    queen.rect.x = 30+self.b_size*(i)
                    queen.rect.y = 120+self.b_size*(z)

                    self.c_g.add(queen)
                
                #Creació de la peça Àlfil
                elif self.position[z][i].capitalize() == "B":
                    bishop = pieces.Bishop(cl, (z, i))

                    bishop.rect.x = 30+self.b_size*(i)
                    bishop.rect.y = 120+self.b_size*(z)

                    self.c_g.add(bishop)
                
                #Creació de la peça Cavall
                elif self.position[z][i].capitalize() == "N":
                    knight = pieces.Knight(cl, (z, i))

                    knight.rect.x = 30+self.b_size*(i)
                    knight.rect.y = 120+self.b_size*(z)

                    self.c_g.add(knight)
                
                #Creació de la peça Torre
                elif self.position[z][i].capitalize() == "R":
                    rock = pieces.Rock(cl, (z, i))

                    rock.rect.x = 30+self.b_size*(i)
                    rock.rect.y = 120+self.b_size*(z)

                    self.c_g.add(rock)

                #Dibuixat en pantalla de les posibilitats de joc per a la peça seleccionada
                if (i, z) in self.mp:
                    if self.position[i][z] == "":
                        pygame.draw.circle(self.screen, (97,97,97), (30+self.b_size*(z)+20, 120+self.b_size*(i)+20), 5)

                    else:
                        pygame.draw.rect(self.screen, (97,97,97),[30+self.b_size*(z), 120+self.b_size*(i), 40, 40], 2, border_radius = 10)
                     
        self.c_g.draw(self.screen) #Dibuixat en pantalla de totes les peces