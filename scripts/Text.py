#Llibreries importades
import pygame

#Scripts importats
import scripts.Objects as objects

class Text(): #Classe de l'historial de jugades
    def __init__(self, screen, proportion, center_x):
        #Atributs de classe
        self.screen = screen #Objecte pygame de finestra
        self.board_list = [] #Llistat amb totes les posicions
        self.buttons = pygame.sprite.Group() #Llista que emmagatzema els objectes dels botons per a aquest apartat

        self.proportion = proportion
        self.center = center_x
        self.btn_dimensions = [int(885.286*self.proportion), 855.286*self.proportion]
    
    def build(self, sprites, center):
        right_button = objects.Button(sprites["little_buttons_1"], 
                                    (0, 146, 149, 292), 
                                    (0, 0, 149, 146), 
                                    (int(25*self.proportion), int(25*self.proportion)),
                                    17)
        right_button.rect.x = self.btn_dimensions[0]+center
        right_button.rect.y = int(442*self.proportion)

        left_button = objects.Button(sprites["little_buttons_2"], 
                                    (0, 146, 149, 292), 
                                    (0, 0, 149, 146), 
                                    (int(25*self.proportion), int(25*self.proportion)),
                                    18)
        left_button.rect.x = self.btn_dimensions[1]+center
        left_button.rect.y = int(442*self.proportion)

        self.buttons.add(right_button)
        self.buttons.add(left_button)

    def draw(self, jugada, text_data, fps, center, data):
        #arial = pygame.font.SysFont('Arial', int(15*self.proportion)) #Font per a renderitzar text
        arial = pygame.font.Font('fonts/arial_unicode_ms.ttf', int(20.23*self.proportion)) #Font per a renderitzar text

        #Dibuixat del fons del bloc historial en finestra
        pygame.draw.rect(self.screen, (220, 220, 220),[int(512.456*self.proportion)+center,int(155.085*self.proportion),int(397.83*self.proportion), 7*int(40.457*self.proportion)])
        pygame.draw.rect(self.screen,(189,189,189),[int(508.41*self.proportion)+center, int(151.0398*self.proportion),int(405.919*self.proportion),7*int(41.457*self.proportion)],int(4.046*self.proportion), border_radius=int(13.485*self.proportion))

        text_pos = 0
        text_period = 1
        local_counter = 0

        #Renderitzat de text (moviments) & Indicador de jugada
        #self.screen.blit(arial.render(str(fps), True, (0, 0, 0)),(800, 250))

        for x in text_data[data.page]:
            local_counter += 1
            k = (0 if text_pos+arial.size(str(x[0]))[0] > int(397.828*self.proportion) else ((self.proportion*26.97) if local_counter%2 != 0 else (self.proportion*13.485)))

            if text_pos+arial.size(str(x[0]))[0] > int(385*self.proportion):
                text_pos = 0
                text_period += 1

            if jugada >= 0 and local_counter == jugada:
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

        self.buttons.sprites()[0].rect.x = self.btn_dimensions[0]+center
        self.buttons.sprites()[1].rect.x = self.btn_dimensions[1]+center

        self.buttons.draw(self.screen)

    def Reverse(self): #Funció per a rotar, girar, totes les posicions emmagatzemades de l'historial
        for x in self.board_list:
            x.reverse() #Invertim l'array sencer
            for y in x:
                y.reverse() #Invertim cadascuna de les fileres