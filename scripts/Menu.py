#Diversas librerias, y parámetros de estas, importadas
from window_behaviour import Proportion
import pygame
from pygame.cursors import arrow

#Importación de otros scripts
import scripts.Objects as pieces

#Classe del Menú
class Menu():
    def __init__(self, screen, proportion):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.coord_y = int(91*proportion) #91
        self.proportion = proportion

        self.buttons = pygame.sprite.Group() #Llista de pygame amb els objectes dels botons
    
    def Generate_Buttons(self): #Funció per a crear els botons i afegir-los a la finestra
 
        menu = pieces.Button("images/tirante.png", (0, 0, 141, 347), (0, 0, 141, 347), (int(30*self.proportion), int(110*self.proportion)), 4)
        menu.rect.x = int(20*self.proportion)
        menu.rect.y = int(-6*self.proportion)

        arrow = pieces.Arrow_Button("images/menu_flecha.png", (0, 0, 105, 96), (int(20*self.proportion), int(20*self.proportion)), 5)
        arrow.rect.x = int(25*self.proportion)
        arrow.rect.y = int(82*self.proportion)
        #arrow.rect.center = (35, 92)

        self.buttons.add(menu)
        self.buttons.add(arrow)
    
    def draw(self): #Funció per a dibuixar en pantalla el Menú
        width, height = self.screen.get_size()

        #Dibuixat del fons del Menú
        pygame.draw.rect(self.screen,(43,55,63),[0,0,width, self.coord_y], 10, border_radius=10)
        pygame.draw.rect(self.screen, (54,69,79), [0, 0, width, self.coord_y-int(7*self.proportion)])

        self.buttons.draw(self.screen) #Dibuixat en pantalla dels botons
    
    def Animation(self): #Funció per a controlar l'animació d'aparició/sortida del menú
        self.pos = (1 if self.pos == 0 else 0)

        return self.pos