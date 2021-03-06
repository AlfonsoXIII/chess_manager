#Llibreries importades
import pygame

#Scripts importats
import scripts.Objects as pieces

#Classe del Menú
class Menu():
    def __init__(self, screen, proportion):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.coord_y = int(122.719*proportion)
        self.proportion = proportion

        self.buttons = pygame.sprite.Group() #Llista de pygame amb els objectes dels botons
    
    def Generate_Buttons(self, sprites): #Funció per a crear els botons i afegir-los a la finestra
 
        menu = pieces.Button(sprites["tirante"], 
                            (0, 0, 141, 347), 
                            (0, 0, 141, 347), 
                            (int(40.457*self.proportion), int(148.34*self.proportion)), 
                            4)
        menu.rect.x = int(26.97*self.proportion)
        menu.rect.y = int(-8.09*self.proportion)

        arrow = pieces.Arrow_Button(sprites["menu_flecha"], 
                                    (0, 0, 105, 96), 
                                    (int(26.97*self.proportion), int(26.97*self.proportion)), 
                                    5, 
                                    self.proportion)
        arrow.rect.x = int(33.71*self.proportion)
        arrow.rect.y = int(110.58*self.proportion)

        config = pieces.Button(sprites["menu_pressed"], 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143), 
                                (int(87.66*self.proportion), int(87.66*self.proportion)), 
                                6)
        config.rect.x = int(121.37*self.proportion)
        config.rect.y = int(13.485*self.proportion)

        export = pieces.Button(sprites["export"], 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(94.39*self.proportion), int(40.46*self.proportion)), 
                                9)
        export.rect.x = int(269.71*self.proportion)
        export.rect.y = int(13.485*self.proportion)

        import_ = pieces.Button(sprites["import"], 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(94.39*self.proportion), int(40.46*self.proportion)), 
                                10)
        import_.rect.x = int(269.71*self.proportion)
        import_.rect.y = int(13.485*self.proportion)+int(47.19*self.proportion)

        rubish = pieces.Button(sprites["rubish_pressed"], 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(40.457*self.proportion), int(40.457*self.proportion)), 
                                11)
        rubish.rect.x = int(418.057*self.proportion)
        rubish.rect.y = int(13.485*self.proportion)

        switch = pieces.Button(sprites["change_pressed"], 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(40.457*self.proportion), int(40.457*self.proportion)), 
                                12)
        switch.rect.x = int(418.057*self.proportion)
        switch.rect.y = int(13.485*self.proportion) + int(47.19*self.proportion)

        folder = pieces.Button(sprites["folder_pressed"], 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(87.657*self.proportion), int(87.657*self.proportion)), 
                                13)
        folder.rect.x = int(606.857*self.proportion)
        folder.rect.y = int(13.485*self.proportion)

        github = pieces.Button(sprites["github_pressed"], 
                                (0, 146.5, 150, 293), 
                                (0, 0, 150, 143),
                                (int(87.657*self.proportion), int(87.657*self.proportion)), 
                                14)
        github.rect.x = int(741.71*self.proportion)
        github.rect.y = int(13.485*self.proportion)

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
        pygame.draw.rect(self.screen, (54,69,79), [0, 0, width, self.coord_y-int(9.44*self.proportion)])

        self.buttons.draw(self.screen) #Dibuixat en pantalla dels botons
    
    def Animation(self): #Funció per a controlar l'animació d'aparició/sortida del menú
        self.pos = (1 if self.pos == 0 else 0)

        return self.pos