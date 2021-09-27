#Llibreries importades
from window_behaviour import Proportion
import pygame
import math

#Scripts importats
import chess_notations

class Text(): #Classe de l'historial de jugades
    def __init__(self, screen, proportion, center_x):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.mov_list = [] #Llistat de jugades per a visualitzar
        self.board_list = [] #Llistat amb totes les posicions

        self.proportion = proportion
        self.center = center_x

    def draw(self, jugada, text_data):
        #arial = pygame.font.SysFont('Arial', int(15*self.proportion)) #Font per a renderitzar text
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(15*self.proportion)) #Font per a renderitzar text

        #Dibuixat del fons del bloc historial en finestra
        pygame.draw.rect(self.screen, (220, 220, 220),[int(380*self.proportion)+self.center,int(115*self.proportion),int(295*self.proportion), (math.trunc(len(self.mov_list)/6)+1)*int(30*self.proportion)])
        pygame.draw.rect(self.screen,((189,189,189)),[int(377*self.proportion)+self.center, int(112*self.proportion),int(301*self.proportion),6+((math.trunc(len(self.mov_list)/6)+1)*int(30*self.proportion))],int(3*self.proportion), border_radius=int(10*self.proportion))

        print(text_data)

        #Renderitzat de text (moviments) & Indicador de jugada
        for x in text_data:
            #Text
            self.screen.blit(arial.render(x[0], True, (0, 0, 0)),((390*self.proportion)+self.center+((text_data.index(x) if text_data.index(x)<6 else text_data.index(x) - math.trunc(text_data.index(x)/6)*6)*(50*self.proportion)),(30*self.proportion)*(1 if text_data.index(x)<6 else math.trunc(text_data.index(x)/6)+1)+(94*self.proportion)))
            #self.screen.blit(arial.render(x, True, (0, 0, 0)),((390*self.proportion)+self.center))

            #if jugada >= 0 and self.mov_list.index(x)+1 == jugada:
                #Indicador circular
                #pygame.draw.circle(self.screen, (255, 0, 0), ((390*self.proportion)+self.center+((self.mov_list.index(x) if self.mov_list.index(x)<6 else self.mov_list.index(x) - math.trunc(self.mov_list.index(x)/6)*6)*(50*self.proportion)),(30*self.proportion)*(1 if self.mov_list.index(x)<6 else math.trunc(self.mov_list.index(x)/6)+1)+(94*self.proportion)), 2)

    def Reverse(self): #Funció per a rotar, girar, totes les posicions emmagatzemades de l'historial
        for x in self.board_list:
            x.reverse() #Invertim l'array sencer
            for y in x:
                y.reverse() #Invertim cadascuna de les fileres