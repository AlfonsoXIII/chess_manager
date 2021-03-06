#Llibreries importades
import pygame

#Scripts importats
import scripts.Objects as pieces

#Classe del taulell
class Board():
    def __init__(self, green, yellow, charcoal, white, screen, window_size, b_size, b_len, proportion):
        #Atributs de classe
        self.window_size = window_size #Dimensions de la finestra
        self.screen = screen #Objecte pygame de finestra
        self.b_size = b_size #
        self.b_len = b_len #
        self.selected = () #Coordenades de selecció al taulell
        self.check_pos = () #Coordenades de "escac" al taulell

        self.green = green #Color verd
        self.yellow = yellow #Color groc
        self.charcoal = charcoal #Color carbó
        self.white = white #Color blanc

        self.proportion = proportion

        self.buttons = pygame.sprite.Group() #Llista de pygame amb els objectes dels botons
    
    def Generate_Buttons(self, sprites): #Funció per a crear els botons i afegir-los a la finestra
        #Creació del botó per a desplaçar cap a la dreta l'historial de jugades
        move_1 = pieces.Button(sprites["right_pressed"], 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(107.885*self.proportion), int(53.94*self.proportion)), 
                                1)

        move_1.rect.x = int(318.26*self.proportion)
        move_1.rect.y = int(620.34*self.proportion)

        #Creació del botó per a desplaçar cap a l'esquerra l'historial de jugades
        move_2 = pieces.Button(sprites["left_pressed"], 
                                (0, 145, 347, 290), 
                                (0, 0, 347, 140), 
                                (int(107.885*self.proportion), int(53.94*self.proportion)), 
                                -1)
        
        move_2.rect.x = int(89.005*self.proportion)
        move_2.rect.y = int(620.34*self.proportion)

        #Creació del botó per rotar el taulell
        flip = pieces.Button(sprites["flip_board"], 
                            (0, 146, 149, 292), 
                            (0, 0, 149, 146), 
                            (int(26.97*self.proportion), int(26.97*self.proportion)), 
                            3)

        flip.rect.x = int(35.06*self.proportion)
        flip.rect.y = int(620.34*self.proportion)

        #Creació del botó per a eliminar la darrera jugada de l'historial
        rem = pieces.Button(sprites["rem_pressed"], 
                            (0, 146, 149, 292), 
                            (0, 0, 149, 146), 
                            (int(53.94*self.proportion), int(53.94*self.proportion)), 
                            0)

        rem.rect.x = int(230.61*self.proportion)
        rem.rect.y = int(620.34*self.proportion)
        
        #Agefim els objectes a la llista
        self.buttons.add(move_1)
        self.buttons.add(move_2)
        self.buttons.add(flip)
        self.buttons.add(rem)
    
    def draw(self, white_t, fliped, render_buttons): #Funció per a dibuixar en pantalla el taulell
        cnt = 0
        self.screen.fill((243,239,239))

        #Generador de les caselles i dibuixat en pantalla
        for i in range(1,self.b_len+1):
            for z in range(1,self.b_len+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, self.yellow,[int(40.457*self.proportion)+self.b_size*(z-1),int(161.828*self.proportion)+self.b_size*(i-1),self.b_size,self.b_size])
                else:
                    pygame.draw.rect(self.screen, self.green, [int(40.457*self.proportion)+self.b_size*(z-1),int(161.828*self.proportion)+self.b_size*(i-1),self.b_size,self.b_size])
                cnt +=1
            cnt-=1

        #Coloració a la casella seleccionada, en cas de que hi hagi
        if len(self.selected) != 0:
            pygame.draw.rect(self.screen, (200, 200, 200), [int(40.457*self.proportion)+self.b_size*self.selected[0], int(161.828*self.proportion)+self.b_size*self.selected[1], self.b_size, self.b_size])
        
        #Coloració a la casella del rei que hagi rebut un escac, en cas de que hi hagi
        if len(self.check_pos) != 0:
            local_checkpos = (self.check_pos if fliped == False else (7-self.check_pos[0], 7-self.check_pos[1]))
            pygame.draw.rect(self.screen, (240,128,128), [int(40.457*self.proportion)+self.b_size*local_checkpos[0], int(161.828*self.proportion)+self.b_size*local_checkpos[1], self.b_size, self.b_size])

        #Dibuixat del marc del taulell
        pygame.draw.rect(self.screen,self.charcoal,[int(26.97*self.proportion)+1,int(148.343*self.proportion),self.b_len*self.b_size+(24*self.proportion),self.b_len*self.b_size+(24*self.proportion)],int(13.485*self.proportion), border_radius=int(13.485*self.proportion))

        #Dibuixat de l'indicador de torn
        pygame.draw.circle(self.screen, (0, 0, 0), (500*self.proportion, 148.343*self.proportion), 10.788*self.proportion)
        pygame.draw.circle(self.screen, ((255, 255, 255) if white_t == True else (0, 0, 0)), (500*self.proportion, 148.343*self.proportion), 8.09*self.proportion)

        if render_buttons == True:
            self.buttons.draw(self.screen) #Dibuixat dels botons en pantalla