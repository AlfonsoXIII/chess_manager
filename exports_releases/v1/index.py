#Diversas librerias, y parámetros de estas, importadas
import pygame
from pygame.locals import *
from pygame.constants import RESIZABLE
from PIL import Image
import sys

#Importación de otros scripts
import pieces

#Clase para manejar el tablero como un objeto
class Board():
    def __init__(self, green, yellow, charcoal, white, screen, window_size, b_size, b_len):
        #Atributos de clase
        self.window_size = window_size
        self.screen = screen
        self.b_size = b_size
        self.b_len = b_len
        self.green = green
        self.yellow = yellow
        self.charcoal = charcoal
        self.white = white
    
    def draw(self, window_size): #Constructor de Objeto
        cnt = 0

        self.screen.fill(self.white) #Establecer pantalla con fondo blanco

        #Generador de Casillas
        for i in range(1,self.b_len+1):
            for z in range(1,self.b_len+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, self.yellow,[((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(z-1),10+self.b_size*(i-1),self.b_size,self.b_size])
                else:
                    pygame.draw.rect(self.screen, self.green, [((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(z-1),10+self.b_size*(i-1),self.b_size,self.b_size])
                cnt +=1
            cnt-=1
        #Borde de tablero
        pygame.draw.rect(self.screen,self.charcoal,[((window_size[0]-(self.b_size*self.b_len))/2),10,self.b_len*self.b_size,self.b_len*self.b_size],5)

#Clase para manejar las piezas como un objeto
class Pieces():
    def __init__(self, screen, b_size, b_len):
        #Atributos de clase
        self.screen = screen
        self.b_size = b_size
        self.b_len = b_len
        self.pieces = Image.open("images/chess_pieces.png")
        self.position = [["r", "n", "b", "q", "k", "b", "n", "r"],
                        ["p", "p", "p", "p", "p", "p", "p", "p"],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", ""],
                        ["P", "P", "P", "P", "P", "P", "P", "P"],
                        ["R", "N", "B", "Q", "K", "B", "N", "R"]]

        #Identificadores según piezas:
            #1. Cada pieza se marcará con su inicial inglesa; nótese la excepción con Knight -> (N), en vez de K. 
            #2. Para discernir el color, siguiendo los criterios de la notación FEN una mayúscula para blancas y minúscula para negras.

        self.c_g = pygame.sprite.Group() #Grupo de Sprites (Piezas)
        self.mp = [] #Lista con las casillas de jugada disponible según pieza seleccionada

    def draw(self, window_size): #Constructor de Objeto
        self.c_g = pygame.sprite.Group() #Limpiar array de sprites para redibujado

        #Deployment de piezas
        for i in range(0, 8):
            for z in range(0 ,8):
                #Determinar el color de las piezas
                cl = 0 if self.position[z][i].isupper() else 1

                #Creación de objeto "Peón"
                if self.position[z][i].capitalize() == "P":
                    pawn = pieces.Pawn(cl, (z, i))

                    pawn.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    pawn.rect.y = 10+self.b_size*(z)

                    self.c_g.add(pawn)
                
                #Creación de objeto "Rey"
                elif self.position[z][i].capitalize() == "K":
                    king = pieces.King(cl, (z, i))

                    king.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    king.rect.y = 10+self.b_size*(z)

                    self.c_g.add(king)
                
                #Creación de objeto "Dama"
                elif self.position[z][i].capitalize() == "Q":
                    queen = pieces.Queen(cl, (z, i))

                    queen.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    queen.rect.y = 10+self.b_size*(z)

                    self.c_g.add(queen)
                
                #Creación de objeto "Álfil"
                elif self.position[z][i].capitalize() == "B":
                    bishop = pieces.Bishop(cl, (z, i))

                    bishop.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    bishop.rect.y = 10+self.b_size*(z)

                    self.c_g.add(bishop)
                
                #Creación de objeto "Caballo"
                elif self.position[z][i].capitalize() == "N":
                    knight = pieces.Knight(cl, (z, i))

                    knight.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    knight.rect.y = 10+self.b_size*(z)

                    self.c_g.add(knight)
                
                #Creación de objeto "Torre"
                elif self.position[z][i].capitalize() == "R":
                    rock = pieces.Rock(cl, (z, i))

                    rock.rect.x = ((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(i)
                    rock.rect.y = 10+self.b_size*(z)

                    self.c_g.add(rock)

                #Dibujado en pantalla de las posibilidades de movimiento, en caso de que se haya seleccionado una pieza                
                if (i, z) in self.mp:
                    pygame.draw.rect(self.screen, (220,20,60),[((window_size[0]-(self.b_size*self.b_len))/2)+self.b_size*(z), 10+self.b_size*(i), 40, 40], 2)
            
        self.c_g.draw(self.screen) #Dibujado en pantalla de todas las piezas

def Main(): #Función principal del programa
    pygame.init()

    #Declaración de la paleta de colores que usaré para la interfaz
    yellow, green, white, charcoal = (231,231,216),(131, 175, 155),(255,255,255), (54,69,79)

    image = Image.open("images/chess_pieces.png") #Path del conjunto de sprites de piezas.
    images = image.crop((120, 0, 160, 40)) #Selección de icono para la ventana
    icon = pygame.image.fromstring(images.tobytes(), images.size, images.mode) #Determino icono para la ventana

    #Inicialización de la ventana & primera configuración
    BoardDisplay = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    pygame.display.set_caption("Tablero de Ajedrez")
    pygame.display.set_icon(icon)
    BoardDisplay.fill(white)
    
    end = False #Variable para controlar el fin del bucle principal del programa
    pressed = False #Variable para controlar el sistema de selección de piezas
    white_t = True #Variable para controlar el sistema de turnos, white_t -> "Turno de Blancas"

    #Información para la construcción del tablero en ventana
    size = 40
    boardLength = 8

    #Creación del objeto Tablero y primer dibujado en pantalla
    tablero = Board(green, yellow, charcoal, white, BoardDisplay, pygame.display.get_surface().get_size(), size, boardLength)
    piezas = Pieces(BoardDisplay, size, boardLength)
    tablero.draw(pygame.display.get_surface().get_size())
    piezas.draw(pygame.display.get_surface().get_size())
    
    while end != True: #Loop principal de eventos en ventana
        for event in pygame.event.get():
                #Configuración del botón de cerrar ventana
                if event.type == pygame.QUIT:
                    end = True
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN: #Evento que se ejecuta cuando el Mouse hace click en la ventana
                    if pressed == False: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                        #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                        for x in piezas.c_g:
                            if x.rect.collidepoint(event.pos[0], event.pos[1]) and piezas.position[x.pos[0]][x.pos[1]].isupper() == white_t:
                                movimientos = x.Movement(piezas.position)
                                piezas.mp = movimientos
                                pressed = True
                                break

                    else: #Se ejecuta en caso de que si se haya seleccionado una pieza
                        #Se revisa si la segunda selección en pantalla corresponde a una pieza y se actualiza el tablero&variables en función de ello
                        if ((pygame.display.get_surface().get_size()[0]-(size*boardLength))/2) <= event.pos[0] <= (pygame.display.get_surface().get_size()[0]-((pygame.display.get_surface().get_size()[0]-(size*boardLength))/2)) and 10 <= event.pos[1] <=330: 
                            target = ([a for a in range(1, 9) if size*a+10 > event.pos[1]][0]-1, [a for a in range(1, 9) if size*a+((pygame.display.get_surface().get_size()[0]-(size*boardLength))/2) > event.pos[0]][0]-1)
                            if x.rect.collidepoint(event.pos[0], event.pos[1]):
                                piezas.mp = []
                                pressed = False

                            elif target in movimientos:
                                piezas.position[target[0]][target[1]] = x.id if piezas.position[x.pos[0]][x.pos[1]].isupper() == True else x.id.lower()
                                piezas.position[x.pos[0]][x.pos[1]] = ""
                                piezas.mp = []
                                pressed = False
                                white_t = True if white_t == False else False
                                pygame.image.save(BoardDisplay, "1.jpg")

                        piezas.mp = []
                        pressed = False                 

                #Evitamos que el usuario pueda modificar el tamaño de la ventana fuera de nuestros parámetros
                elif event.type == VIDEORESIZE:
                    width, height = event.size
                    if width < 400:     width = 400 #Límites mínimos de altura
                    if height < 400:    height = 400 #Límites mínimos de anchura

                    BoardDisplay = pygame.display.set_mode((width, height), pygame.RESIZABLE) #Actualización de ventana con los parámetros ajustados.

        tablero.draw(pygame.display.get_surface().get_size()) #Actualización del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        piezas.draw(pygame.display.get_surface().get_size()) #Actualización del contenido del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        pygame.display.update() #Refrescar la visualización en pantalla. 

if __name__ == '__main__': #Inicio de ejecución del programa
    Main() #Llamada a la función principal