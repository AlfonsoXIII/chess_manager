#Llibreries importades
import pygame
import math

class Text(): #Classe de l'historial de jugades
    def __init__(self, screen, proportion, center_x):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.board_list = [] #Llistat amb totes les posicions

        self.proportion = proportion
        self.center = center_x

    def draw(self, jugada, text_data, fps, center):
        #arial = pygame.font.SysFont('Arial', int(15*self.proportion)) #Font per a renderitzar text
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(20.23*self.proportion)) #Font per a renderitzar text

        #Dibuixat del fons del bloc historial en finestra
        pygame.draw.rect(self.screen, (220, 220, 220),[int(512.456*self.proportion)+center,int(155.085*self.proportion),int(397.83*self.proportion), (math.trunc(len(text_data)/6)+1)*int(40.457*self.proportion)])
        pygame.draw.rect(self.screen,(189,189,189),[int(508.41*self.proportion)+center, int(151.0398*self.proportion),int(405.919*self.proportion),6+((math.trunc(len(text_data)/6)+1)*int(40.457*self.proportion))],int(4.046*self.proportion), border_radius=int(13.485*self.proportion))

        text_pos = 0
        text_period = 1

        #Renderitzat de text (moviments) & Indicador de jugada
        #self.screen.blit(arial.render(str(fps), True, (0, 0, 0)),(800, 250))

        for x in text_data:
            k = (0 if text_pos+arial.size(str(x[0]))[0] > int(397.828*self.proportion) else ((self.proportion*26.97) if text_data.index(x)%2 != 0 else (self.proportion*13.485)))

            if jugada >= 0 and text_data.index(x)+1 == jugada:
                #Indicador circular
                pygame.draw.rect(self.screen, (0, 0, 0), ((525.94*self.proportion)+center+text_pos,
                                (40.457*self.proportion)*text_period+(126.765*self.proportion),
                                arial.size(str(x[0]))[0],
                                26.97*self.proportion))

                #Text
                self.screen.blit(arial.render(x[0], True, (255, 255, 255)),((525.94*self.proportion)+center+text_pos,
                                (40.457*self.proportion)*text_period+(126.765*self.proportion)))
        
            else:
                #Text
                self.screen.blit(arial.render(x[0], True, (0, 0, 0)),((525.94*self.proportion)+center+text_pos,
                                (40.457*self.proportion)*text_period+(126.765*self.proportion)))

            text_pos += arial.size(str(x[0]))[0] + k

            if text_pos+arial.size(str(x[0]))[0] > int(397.828*self.proportion):
                text_pos = 0
                text_period += 1

    def Reverse(self): #Funció per a rotar, girar, totes les posicions emmagatzemades de l'historial
        for x in self.board_list:
            x.reverse() #Invertim l'array sencer
            for y in x:
                y.reverse() #Invertim cadascuna de les fileres