#Llibreries importades
from window_behaviour import Proportion
import pygame
import math

#Scripts importats
import scripts.Objects as pieces

class config_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion

        self.ico = "images/icos/conig.png"
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(25*self.proportion))
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(15*self.proportion))

        self.screen.blit(arial_big.render("Config", True, (255, 255, 255)),(10, 180))
        self.screen.blit(arial.render("Animacions:", True, (255, 255, 255)),(10, 250))
        self.screen.blit(arial.render("Animacions:", True, (255, 255, 255)),(10, 280))

class test_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion
    
    def draw(self):
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(15*self.proportion))

        self.screen.blit(arial.render("wawa", True, (255, 255, 255)),(5, 180))

class side_Menu(): #Classe del menú lateral
    def __init__(self, screen):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.content = []
        self.content_shown = 0

        self.menus_active = [False, False]
        
        self.buttons = []
        self.buttons_1 = pygame.sprite.Group()
    
    def Build(self):
        apply = pieces.Button("images/apply_pressed.bmp", 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 142),
                                (80, 40),
                                7)
        apply.rect.center = (100, 650)

        close = pieces.Button("images/close_pressed.bmp", 
                                (0, 146, 149, 292), 
                                (0, 0, 149, 146),
                                (30, 30),
                                7)
        close.rect.center = (170, 150)

        #self.buttons_1.add(apply)
        self.buttons_1.add(close)
    
    def Draw(self, activate):
        if activate == True:
            pygame.draw.rect(self.screen, (38, 50, 56), (0, 0, 200, 1000))
            self.buttons_1.draw(self.screen)

            for x in self.content:
                if x == self.content[self.content_shown]:
                    pygame.draw.rect(self.screen, (38, 50, 56), [200, 180+(50*self.content.index(x)), 20, 50])
                    self.buttons.append(pygame.Rect([200, 180+(50*self.content.index(x)), 20, 50]))
                    x.draw()
                
                else:
                    pygame.draw.rect(self.screen, (69, 90, 100), [200, 180+(50*self.content.index(x)), 20, 50])
                    self.buttons.append(pygame.Rect([200, 180+(50*self.content.index(x)), 20, 50]))

    def Add(self, menu):
        self.content.append(menu)

    def Switch(self, menu):
        self.content_shown = menu