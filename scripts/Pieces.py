#Llibreries importades
import pygame
from pygame import surface

#Scripts importats
import scripts.Objects as pieces

#Classe que compren i gestiona totes les peces del taulell
class Pieces():
    def __init__(self, screen, b_size, b_len, position, proportion, sprites):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.proportion = proportion #Proporció dels elements en finestra per a escalar-los
        self.b_size = b_size #Longitud dels segments que formen els quadrats del taulell
        self.b_len = b_len #Número de caselles al taulell
        self.position = position[-1] #Array amb la posició a visualitzar del taulell

        self.sprite = sprites
        self.c_g = pygame.sprite.Group() #Grup pygame per a emmagatzemar un conjunt de sprites
        self.mp = [] #Llistat amb les caselles a les que pot anar la peça seleccionada

        self.surface = []
        
        self.Promotion_Window = False
    
    def Update(self):
        #Dibuixat en pantalla de les posibilitats de joc per a la peça seleccionada
        for i in range(0, 8):
            for z in range(0 ,8):
                if (i, z) in self.mp:
                    if self.position[i][z] == "":
                        pygame.draw.circle(self.screen, (97,97,97), (int(40.457*self.proportion)+self.b_size*(z)+(26.97*self.proportion), int(161.83*self.proportion)+self.b_size*(i)+(26.97*self.proportion)), 5)

                    else:
                        pygame.draw.rect(self.screen, (97,97,97),[int(40.457*self.proportion)+self.b_size*(z), int(161.83*self.proportion)+self.b_size*(i), (53.94*self.proportion), (53.94*self.proportion)], 2, border_radius = 10)

            self.c_g.draw(self.screen) #Dibuixat en pantalla de totes les peces

    def draw(self, reverse): #Dibuixat en pantalla de les peces
        #Neteja dels sprites prèvis
        for x in self.c_g:
            x.kill()

        #Creació de les peces i disposició de les seves coordenades
        for i in range(0, 8):
            for z in range(0 ,8):
                #Determinació de l'atribut color de les peces
                cl = 0 if self.position[z][i].isupper() else 1
                size = (int(44.5*self.proportion), int(44.5*self.proportion))

                #Creació de la peça Peó
                if self.position[z][i].capitalize() == "P":
                    pawn = pieces.Pawn(self.sprite[("P" if cl == 0 else "p")], cl, (z, i), reverse, size)

                    pawn.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(pawn)
                
                #Creació de la peça Rei
                elif self.position[z][i].capitalize() == "K":
                    king = pieces.King(self.sprite[("K" if cl == 0 else "k")], cl, (z, i), reverse, size)

                    king.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(king)
                
                #Creació de la peça Dama
                elif self.position[z][i].capitalize() == "Q":
                    queen = pieces.Queen(self.sprite[("Q" if cl == 0 else "q")], cl, (z, i), size)

                    queen.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(queen)
                
                #Creació de la peça Àlfil
                elif self.position[z][i].capitalize() == "B":
                    bishop = pieces.Bishop(self.sprite[("B" if cl == 0 else "b")], cl, (z, i), size)

                    bishop.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(bishop)
                
                #Creació de la peça Cavall
                elif self.position[z][i].capitalize() == "N":
                    knight = pieces.Knight(self.sprite[("N" if cl == 0 else "n")], cl, (z, i), size)

                    knight.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(knight)
                
                #Creació de la peça Torre
                elif self.position[z][i].capitalize() == "R":
                    rock = pieces.Rock(self.sprite[("R" if cl == 0 else "r")], cl, (z, i), size)

                    rock.rect.center = ((40.457*self.proportion)+self.b_size*(i)+(26.97*self.proportion),
                                        (161.83*self.proportion)+self.b_size*(z)+(26.97*self.proportion))

                    self.c_g.add(rock)

        self.c_g.draw(self.screen) #Dibuixat en pantalla de totes les peces