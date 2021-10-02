'''
Classe encarregada de l'emmagatzenament i gestió de les dades 
principals del taulell d'escacs en els seus diferents mòdes.
'''

class Data(): #Funció on s'emmagatzemen diferents variables
    def __init__(self):
        self.proportion = 1 #Variable que controla la proporció dels objectes en relació a la nativa original de desenvolupament pel seu escalat
        self.static_relative_center = [0, 0]

        self.end = False #Variable per a controlar la fi del programa
        self.menu_open = False #Variable que controla si el menú s'ha activat o no
        self.menu_pos_y = 0 #Variable que determina la posició en l'eix y del menú
        self.board_pos_y = 0 #Variable que determina la posició en l'eix y del taulell i altres objectes
        self.relative_center = 0 #Variable que determina el centre relatiu per a centrar els objectes aliens al menú en pantalla
        self.text_relative_center = 0
        self.catch_button = None #Variable que captura el botó que s'ha pres
        self.menu_counter = [0, 4]
        self.side_menu_on = False

        self.freeze = False
        self.pressed = False #Variable encarregada d'emmagatzemar si s'ha pressionat, seleccionat, una peça
        self.white_t = True #Variable per a controlar quin torn es en funció de les peces blanques
        self.reverse = False #Variable per a controlar si el taulell es troba rotat
        self.jugada = 0 #Variable que controla la jugada visualitzada
        self.check = False #Variable per a emmagatzemar si s'està en una posició d'escac
        self.check_mate = False #Variable per a emmagatzemar si s'està en una posició d'escac i mat
        self.wk_moved = True #Variable per a emmagatzemar si el rei blanc s'ha desplaçat prèviament
        self.bk_moved = True #Variable per a emmagatzemar si el rei negre s'ha desplaçat prèviament
        self.castling = [] #Variable per a emmagatzemar localment les coordenades d'enroc

        self.text_data = [] #Informació sobre les jugades a visualitzar en format text
