#Llibreries importades
import pygame
import multiprocessing
from math import inf
import concurrent.futures

#Scripts importats
import scripts.Objects as objects
import scripts.ai.test as ai

class Text(): #Classe de l'historial de jugades
    def __init__(self, screen, proportion, center_x):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.buttons = pygame.sprite.Group() #Llista que emmagatzema els objectes dels botons per a aquest apartat

        self.proportion = proportion
        self.center = center_x
    
    def build(self, sprites, center):
        on = objects.Button(sprites["suma"], 
                                    (0, 146, 149, 292), 
                                    (0, 0, 149, 146), 
                                    (int(25*self.proportion), int(25*self.proportion)),
                                    15)
        on.rect.x = int(512.286*self.proportion)+center
        on.rect.y = int(492*self.proportion)

        off = objects.Button(sprites["resta"], 
                                    (0, 146, 149, 292), 
                                    (0, 0, 149, 146), 
                                    (int(25*self.proportion), int(25*self.proportion)),
                                    16)
        off.rect.x = int(547.286*self.proportion)+center
        off.rect.y = int(492*self.proportion)

        self.buttons.add(on)
        self.buttons.add(off)
    
    def ai_call(self, board):

        with concurrent.futures.ProcessPoolExecutor() as executor:
            p1 = executor.submit(ai.test2, board, -inf, +inf, False, 1)
            print(p1.result())

        return "uwu"

            

    def draw(self, text_data, center):
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(18.23*self.proportion)) #Font per a renderitzar text

        #Dibuixat del fons del bloc historial en finestra
        pygame.draw.rect(self.screen, (220, 220, 220),[int(512.456*self.proportion)+center,int(525*self.proportion),int(397.83*self.proportion), int(40.457*self.proportion)])
        pygame.draw.rect(self.screen,(189,189,189),[int(508.456*self.proportion)+center,int(521*self.proportion),int(405.83*self.proportion), int(48.457*self.proportion)],int(4.046*self.proportion), border_radius=int(13.485*self.proportion))

        self.screen.blit(arial.render(text_data, True, (0, 0, 0)), [int(522.456*self.proportion)+center,int(530*self.proportion)])

        self.buttons.draw(self.screen)