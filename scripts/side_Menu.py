#Llibreries importades
import pygame

#Scripts importats
import scripts.Objects as pieces

class config_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion

        self.ico = "images/icos/conig.png"
        self.id = "Config"
        self.buttons = pygame.sprite.Group()
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(33.71*self.proportion))
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(20.228*self.proportion))
        arial_bold = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(20.228*self.proportion))
        arial_small = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(13.485*self.proportion))

        self.screen.blit(arial_big.render("INFORM.", True, (255, 255, 255)),(int(10*self.proportion), int(180*self.proportion)))
        self.screen.blit(arial_bold.render("Versió:", True, (255, 255, 255)),(int(10*self.proportion), int(250*self.proportion)))
        self.screen.blit(arial.render("1.0.0", True, (255, 255, 255)),(int(10*self.proportion), int(280*self.proportion)))
        self.screen.blit(arial_bold.render("Data Versió:", True, (255, 255, 255)),(int(10*self.proportion), int(320*self.proportion)))
        self.screen.blit(arial.render("03/11/2021", True, (255, 255, 255)),(int(10*self.proportion), int(350*self.proportion)))
        self.screen.blit(arial_bold.render("Versió mòdul:", True, (255, 255, 255)),(int(10*self.proportion), int(420*self.proportion)))
        self.screen.blit(arial.render("1.0.0", True, (255, 255, 255)),(int(10*self.proportion), int(450*self.proportion)))

        self.screen.blit(arial_small.render("© 2021 AlfonsoXIII", True, (255, 255, 255)),(int(10*self.proportion), int(580*self.proportion)))

class promotion_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion

        self.id = "Promotion"
        self.buttons = pygame.sprite.Group()

        self.catch_piece = None
        self.pos = [0, 0]
        self.selected = [0, 0, 0, 0]

    def Build(self, colour):
        bishop = pieces.Render_Image("images/2DBoardPieces/{}/B.bmp".format(colour), (int(60*self.proportion), int(60*self.proportion)), "B")
        bishop.rect.x = int(30*self.proportion)
        bishop.rect.y = int(260*self.proportion)
        self.buttons.add(bishop)

        knight = pieces.Render_Image("images/2DBoardPieces/{}/N.bmp".format(colour), (int(60*self.proportion), int(60*self.proportion)), "N")
        knight.rect.x = int(90*self.proportion)
        knight.rect.y = int(260*self.proportion)
        self.buttons.add(knight)

        queen = pieces.Render_Image("images/2DBoardPieces/{}/Q.bmp".format(colour), (int(60*self.proportion), int(60*self.proportion)), "Q")
        queen.rect.x = int(30*self.proportion)
        queen.rect.y = int(320*self.proportion)
        self.buttons.add(queen)

        rock = pieces.Render_Image("images/2DBoardPieces/{}/R.bmp".format(colour), (int(60*self.proportion), int(60*self.proportion)), "R")
        rock.rect.x = int(90*self.proportion)
        rock.rect.y = int(320*self.proportion)
        self.buttons.add(rock)
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(33.71*self.proportion))
        self.screen.blit(arial_big.render("PROM.", True, (255, 255, 255)),(int(10*self.proportion), int(180*self.proportion)))

        pygame.draw.rect(self.screen, (69, 90, 100), self.selected)

        self.buttons.draw(self.screen)

class play_mode_menu():
    def __init__(self, screen, proportion):
        self.screen = screen
        self.proportion = proportion

        self.id = "Play"
        self.buttons = pygame.sprite.Group()

        self.catch_piece = None
        self.pos = [0, 0]
        self.selected = [0, 0, 0, 0]

    def Build(self):
        bishop = pieces.Render_Image("images/2DBoardPieces/0/P.bmp", 
                                    (int(60*self.proportion), int(60*self.proportion)), 
                                    False)


        bishop.rect.x = int(30*self.proportion)
        bishop.rect.y = int(300*self.proportion)
        self.buttons.add(bishop)

        knight = pieces.Render_Image("images/2DBoardPieces/1/p.bmp", 
                                    (int(60*self.proportion), int(60*self.proportion)), 
                                    True)


        knight.rect.x = int(90*self.proportion)
        knight.rect.y = int(300*self.proportion)
        self.buttons.add(knight)
    
    def draw(self):
        arial_big = pygame.font.Font('fonts/arial_unicode_ms_bold.ttf', int(33.71*self.proportion))
        self.screen.blit(arial_big.render("Jugar", True, (255, 255, 255)),(int(10*self.proportion), int(180*self.proportion)))

        pygame.draw.rect(self.screen, (69, 90, 100), self.selected)

        self.buttons.draw(self.screen)

class side_Menu(): #Classe del menú lateral
    def __init__(self, screen, proportion):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.content = []
        self.content_shown = 0
        self.proportion = proportion

        self.menus_active = {"Config":False, "Promotion":False, "Import": False, "Export":False, "Play":False}
        
        self.buttons = []
        self.buttons_1 = pygame.sprite.Group()
    
    def Build(self, sprites):
        apply = pieces.Button(sprites["apply_pressed"], 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 142),
                                (int(80*self.proportion), int(40*self.proportion)),
                                7)
        apply.rect.center = (int(100*self.proportion), int(650*self.proportion))

        close = pieces.Button(sprites["close_pressed"], 
                                (0, 146, 149, 292), 
                                (0, 0, 149, 146),
                                (int(30*self.proportion), int(30*self.proportion)),
                                8)
        close.rect.center = (int(170*self.proportion), int(150*self.proportion))

        self.buttons_1.add(apply)
        self.buttons_1.add(close)
    
    def Draw(self, activate):
        self.buttons = []
        if activate == True:
            pygame.draw.rect(self.screen, (38, 50, 56), (0, 0, int(200*self.proportion), int(1000*self.proportion)))
            self.buttons_1.draw(self.screen)

            for x in self.content:
                if x == self.content[self.content_shown]:
                    pygame.draw.rect(self.screen, (38, 50, 56), [int(200*self.proportion), int(180*self.proportion)+(int(50*self.proportion)*self.content.index(x)), int(20*self.proportion), int(50*self.proportion)])
                    self.buttons.append(pygame.Rect([int(200*self.proportion), int(180*self.proportion)+(int(50*self.proportion)*self.content.index(x)), int(20*self.proportion), int(50*self.proportion)]))
                    x.draw()
                
                else:
                    pygame.draw.rect(self.screen, (69, 90, 100), [int(200*self.proportion), int(180*self.proportion)+(int(50*self.proportion)*self.content.index(x)), int(20*self.proportion), int(50*self.proportion)])
                    self.buttons.append(pygame.Rect([int(200*self.proportion), int(180*self.proportion)+(int(50*self.proportion)*self.content.index(x)), int(20*self.proportion), int(50*self.proportion)]))

    def Add(self, menu):
        self.content.append(menu)

    def Switch(self, menu):
        self.content_shown = menu