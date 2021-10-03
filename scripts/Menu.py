#Diversas librerias, y parámetros de estas, importadas
import pygame

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
 
        menu = pieces.Button("images/tirante.png", 
                            (0, 0, 141, 347), 
                            (0, 0, 141, 347), 
                            (int(30*self.proportion), int(110*self.proportion)), 
                            4)
        menu.rect.x = int(20*self.proportion)
        menu.rect.y = int(-6*self.proportion)

        arrow = pieces.Arrow_Button("images/menu_flecha.png", 
                                    (0, 0, 105, 96), 
                                    (int(20*self.proportion), int(20*self.proportion)), 
                                    5, 
                                    self.proportion)
        arrow.rect.x = int(25*self.proportion)
        arrow.rect.y = int(82*self.proportion)

        config = pieces.Button("images/menu_pressed.bmp", 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143), 
                                (int(65*self.proportion), int(65*self.proportion)), 
                                6)
        config.rect.x = int(90*self.proportion)
        config.rect.y = int(10*self.proportion)

        export = pieces.Button("images/export.bmp", 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(70*self.proportion), int(30*self.proportion)), 
                                9)
        export.rect.x = int(200*self.proportion)
        export.rect.y = int(10*self.proportion)

        import_ = pieces.Button("images/import.bmp", 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(70*self.proportion), int(30*self.proportion)), 
                                10)
        import_.rect.x = int(200*self.proportion)
        import_.rect.y = int(10*self.proportion)+int(35*self.proportion)

        rubish = pieces.Button("images/rubish_pressed.bmp", 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(30*self.proportion), int(30*self.proportion)), 
                                11)
        rubish.rect.x = int(310*self.proportion)
        rubish.rect.y = int(10*self.proportion)

        switch = pieces.Button("images/change_pressed.bmp", 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(30*self.proportion), int(30*self.proportion)), 
                                12)
        switch.rect.x = int(310*self.proportion)
        switch.rect.y = int(10*self.proportion) + int(35*self.proportion)

        folder = pieces.Button("images/folder_pressed.bmp", 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(65*self.proportion), int(65*self.proportion)), 
                                13)
        folder.rect.x = int(450*self.proportion)
        folder.rect.y = int(10*self.proportion)

        github = pieces.Button("images/github_pressed.bmp", 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(65*self.proportion), int(65*self.proportion)), 
                                14)
        github.rect.x = int(550*self.proportion)
        github.rect.y = int(10*self.proportion)

        self.buttons.add(menu)
        self.buttons.add(arrow)
        self.buttons.add(config)
        self.buttons.add(export)
        self.buttons.add(import_)
        self.buttons.add(rubish)
        self.buttons.add(switch)
        self.buttons.add(folder)
        self.buttons.add(github)
    
    def draw(self): #Funció per a dibuixar en pantalla el Menú
        width, height = self.screen.get_size()

        #Dibuixat del fons del Menú
        pygame.draw.rect(self.screen,(43,55,63),[0,0,width, self.coord_y], 10, border_radius=10)
        pygame.draw.rect(self.screen, (54,69,79), [0, 0, width, self.coord_y-int(7*self.proportion)])

        self.buttons.draw(self.screen) #Dibuixat en pantalla dels botons
    
    def Animation(self): #Funció per a controlar l'animació d'aparició/sortida del menú
        self.pos = (1 if self.pos == 0 else 0)

        return self.pos
    
    def Config_Window(self):
        pass