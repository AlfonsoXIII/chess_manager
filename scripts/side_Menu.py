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
        self.id = "Config"
        self.buttons = pygame.sprite.Group()
    
    def Build(self):
        btn_1 = pieces.Button("images/select_button.bmp", 
                            (0, 0, 307, 302), 
                            (0, 302, 307, 604), 
                            (25, 25), 
                            8)
        btn_1.rect.center = (150, 265)

        btn_2 = pieces.Button("images/select_button.bmp", 
                            (0, 0, 307, 302), 
                            (0, 302, 307, 604), 
                            (25, 25), 
                            8)
        btn_2.rect.center = (150, 295)

        btn_3 = pieces.Button("images/select_button.bmp", 
                            (0, 0, 307, 302), 
                            (0, 302, 307, 604), 
                            (25, 25), 
                            8)
        btn_3.rect.center = (150, 325)

        self.buttons.add(btn_1)
        self.buttons.add(btn_2)
        self.buttons.add(btn_3)
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(25*self.proportion))
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(15*self.proportion))

        self.screen.blit(arial_big.render("CONFIG.", True, (255, 255, 255)),(10, 180))
        self.screen.blit(arial.render("Animacions:", True, (255, 255, 255)),(10, 250))
        self.screen.blit(arial.render("Notació:", True, (255, 255, 255)),(10, 280))
        self.screen.blit(arial.render("Audio:", True, (255, 255, 255)),(10, 310))

        self.screen.blit(arial.render("Idioma:", True, (255, 255, 255)),(10, 380))

        self.buttons.draw(self.screen)

class promotion_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion

        self.ico = "images/icos/conig.png"
        self.id = "Promotion"
        self.buttons = pygame.sprite.Group()

        self.catch_piece = None
        self.pos = [0, 0]
        self.selected = [0, 0, 0, 0]

    def Build(self):
        bishop = pieces.Render_Image("images/2DBoardPieces/0/B.bmp", (60, 60), "B")
        bishop.rect.x = 30
        bishop.rect.y = 260
        self.buttons.add(bishop)

        knight = pieces.Render_Image("images/2DBoardPieces/0/N.bmp", (60, 60), "N")
        knight.rect.x = 90
        knight.rect.y = 260
        self.buttons.add(knight)

        queen = pieces.Render_Image("images/2DBoardPieces/0/Q.bmp", (60, 60), "Q")
        queen.rect.x = 30
        queen.rect.y = 320
        self.buttons.add(queen)

        rock = pieces.Render_Image("images/2DBoardPieces/0/R.bmp", (60, 60), "R")
        rock.rect.x = 90
        rock.rect.y = 320
        self.buttons.add(rock)
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(25*self.proportion))
        self.screen.blit(arial_big.render("PROM.", True, (255, 255, 255)),(10, 180))

        pygame.draw.rect(self.screen, (69, 90, 100), self.selected)

        self.buttons.draw(self.screen)

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

        self.menus_active = {"Config":False, "Promotion":False}
        
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
                                8)
        close.rect.center = (170, 150)

        self.buttons_1.add(apply)
        self.buttons_1.add(close)
    
    def Draw(self, activate):
        self.buttons = []
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