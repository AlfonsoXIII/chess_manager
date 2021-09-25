'''
Classe encarregada de l'emmagatzenament i gestió de les dades 
principals del taulell d'escacs en els seus diferents mòdes.
'''

class Data(): #Funció on s'emmagatzemen diferents variables
    def __init__(self):
        self.proportion = 1

        self.end = False #Variable per a controlar la fi del programa
        self.menu_open = False #Variable que controla si el menú s'ha activat o no
        self.menu_pos_y = -36*self.proportion
        self.board_pos_y = -20*self.proportion
        #self.center_x = 0
        self.relative_center = 0

        self.pressed = False #Variable encarregada d'emmagatzemar si s'ha pressionat, seleccionat, una peça
        self.white_t = True #Variable per a controlar quin torn es en funció de les peces blanques
        self.reverse = False #Variable per a controlar si el taulell es troba rotat
        self.jugada = 0 #Variable que controla la jugada visualitzada
        self.check = False #Variable per a emmagatzemar si s'està en una posició d'escac
        self.check_mate = False #Variable per a emmagatzemar si s'està en una posició d'escac i mat
        self.wk_moved = False #Variable per a emmagatzemar si el rei blanc s'ha desplaçat prèviament
        self.bk_moved = False #Variable per a emmagatzemar si el rei negre s'ha desplaçat prèviament
        self.castling = [] #Variable per a emmagatzemar localment les coordenades d'enroc
