#Diversas librerias, y parámetros de estas, importadas
import pygame

#Importación de otros scripts
import scripts.Objects as pieces

#Classe del Menú
class Menu():
    def __init__(self, screen):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra

        self.buttons = pygame.sprite.Group() #Llista de pygame amb els objectes dels botons
    
    def Generate_Buttons(self): #Funció per a crear els botons i afegir-los a la finestra
        pass

    '''
    menu = pieces.Menu()
    menu.rect.x = 20
    menu.rect.y = 8

    self.botones.add(menu)
    '''
    
    def draw(self): #Funció per a dibuixar en pantalla el Menú
        #Dibuixat del fons del Menú
        pygame.draw.rect(self.screen,(43,55,63),[0,0,700, 91],10, border_radius=10)
        pygame.draw.rect(self.screen, (54,69,79), [0, 0, 700, 84])

        self.buttons.draw(self.screen) #Dibuixat en pantalla dels botons