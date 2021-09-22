#Diversas librerias, y parámetros de estas, importadas
import pygame
from pygame.locals import *
from pygame.constants import RESIZABLE
from PIL import Image
import sys
import math
from copy import deepcopy

#Importación de otros scripts
import pieces
import chess_notations

class Menu():
    def __init__(self, screen):
        self.screen = screen

        self.botones = pygame.sprite.Group()

        menu = pieces.Menu()
        menu.rect.x = 20
        menu.rect.y = 8

        self.botones.add(menu)
    
    def draw(self):

        pygame.draw.rect(self.screen,(43,55,63),[0,0,700, 91],10, border_radius=10)
        pygame.draw.rect(self.screen, (54,69,79), [0, 0, 700, 84])

        self.botones.draw(self.screen)

class Text(): #Clase para manejar
    def __init__(self, screen):
        self.mov_list = []
        self.board_list = []
        self.screen = screen
    
    def draw(self, jugada):
        arial = pygame.font.SysFont('Arial', 15)
        #seguisym = pygame.font.Font("seguisym.ttf", 15)

        for x in self.mov_list:
            self.screen.blit(arial.render(chess_notations.algebraic_de(x.text, x.pos, x.capture, x.pos_or, str(str(int((self.mov_list.index(x)+1)/2)+1)+ ". ") if (self.mov_list.index(x))%2 == 0 else ""), True, (0, 0, 0)),(390+((self.mov_list.index(x) if self.mov_list.index(x)<6 else self.mov_list.index(x) - math.trunc(self.mov_list.index(x)/6)*6)*45),30*(1 if self.mov_list.index(x)<6 else math.trunc(self.mov_list.index(x)/6)+1)+110))
            
            if jugada >= 0 and self.mov_list.index(x)+1 == jugada:
                pygame.draw.circle(self.screen, (255, 0, 0), (390+((self.mov_list.index(x) if self.mov_list.index(x)<6 else self.mov_list.index(x) - math.trunc(self.mov_list.index(x)/6)*6)*45),30*(1 if self.mov_list.index(x)<6 else math.trunc(self.mov_list.index(x)/6)+1)+110), 2)

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

        self.botones = pygame.sprite.Group()

        boton = pieces.Button()
        boton.rect.x = 230
        boton.rect.y = 455

        boton1 = pieces.Button1()
        boton1.rect.x = 55
        boton1.rect.y = 455

        rem = pieces.Remove()
        rem.rect.x = 170
        rem.rect.y = 455
        
        self.botones.add(boton)
        self.botones.add(boton1)
        self.botones.add(rem)
    
    def draw(self, white_t): #Constructor de Objeto
        cnt = 0

        self.screen.fill((243,239,239)) #Establecer pantalla con fondo blanco

        #Generador de Casillas
        for i in range(1,self.b_len+1):
            for z in range(1,self.b_len+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, self.yellow,[30+self.b_size*(z-1),120+self.b_size*(i-1),self.b_size,self.b_size])
                else:
                    pygame.draw.rect(self.screen, self.green, [30+self.b_size*(z-1),120+self.b_size*(i-1),self.b_size,self.b_size])
                cnt +=1
            cnt-=1
        #Borde de tablero
        pygame.draw.rect(self.screen,self.charcoal,[20,110,self.b_len*self.b_size+18,self.b_len*self.b_size+20],10, border_radius=10)

        pygame.draw.circle(self.screen, (0, 0, 0), (375, 110), 8)
        pygame.draw.circle(self.screen, (255, 255, 255), (375, 110), 6) if white_t == True else pygame.draw.circle(self.screen, (0, 0, 0), (375, 110), 6)

        self.botones.draw(self.screen)

#Clase para manejar las piezas como un objeto
class Pieces(Text):
    def __init__(self, screen, b_size, b_len, position):
        super().__init__(self)

        #Atributos de clase
        self.screen = screen
        self.b_size = b_size
        self.b_len = b_len
        self.pieces = Image.open("images/chess_pieces.png")
        self.position = position[-1]

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

                    pawn.rect.x = 30+self.b_size*(i)
                    pawn.rect.y = 120+self.b_size*(z)

                    self.c_g.add(pawn)
                
                #Creación de objeto "Rey"
                elif self.position[z][i].capitalize() == "K":
                    king = pieces.King(cl, (z, i))

                    king.rect.x = 30+self.b_size*(i)
                    king.rect.y = 120+self.b_size*(z)

                    self.c_g.add(king)
                
                #Creación de objeto "Dama"
                elif self.position[z][i].capitalize() == "Q":
                    queen = pieces.Queen(cl, (z, i))

                    queen.rect.x = 30+self.b_size*(i)
                    queen.rect.y = 120+self.b_size*(z)

                    self.c_g.add(queen)
                
                #Creación de objeto "Álfil"
                elif self.position[z][i].capitalize() == "B":
                    bishop = pieces.Bishop(cl, (z, i))

                    bishop.rect.x = 30+self.b_size*(i)
                    bishop.rect.y = 120+self.b_size*(z)

                    self.c_g.add(bishop)
                
                #Creación de objeto "Caballo"
                elif self.position[z][i].capitalize() == "N":
                    knight = pieces.Knight(cl, (z, i))

                    knight.rect.x = 30+self.b_size*(i)
                    knight.rect.y = 120+self.b_size*(z)

                    self.c_g.add(knight)
                
                #Creación de objeto "Torre"
                elif self.position[z][i].capitalize() == "R":
                    rock = pieces.Rock(cl, (z, i))

                    rock.rect.x = 30+self.b_size*(i)
                    rock.rect.y = 120+self.b_size*(z)

                    self.c_g.add(rock)

                #Dibujado en pantalla de las posibilidades de movimiento, en caso de que se haya seleccionado una pieza                
                if (i, z) in self.mp:
                    pygame.draw.rect(self.screen, (220,20,60),[30+self.b_size*(z), 120+self.b_size*(i), 40, 40], 2)
            
        self.c_g.draw(self.screen) #Dibujado en pantalla de todas las piezas

def Main(): #Función principal del programa
    pygame.init()

    #Declaración de la paleta de colores que usaré para la interfaz
    yellow, green, white, charcoal = (231,231,216),(131, 175, 155),(255,255,255), (54,69,79)

    image = Image.open("images/chess_pieces.png") #Path del conjunto de sprites de piezas.
    images = image.crop((120, 0, 160, 40)) #Selección de icono para la ventana
    icon = pygame.image.fromstring(images.tobytes(), images.size, images.mode) #Determino icono para la ventana

    #Inicialización de la ventana & primera configuración
    BoardDisplay = pygame.display.set_mode((700, 525))
    pygame.display.set_caption("Tablero de Ajedrez")
    pygame.display.set_icon(icon)
    BoardDisplay.fill((243,239,239))
    
    end = False #Variable para controlar el fin del bucle principal del programa
    pressed = False #Variable para controlar el sistema de selección de piezas
    white_t = True #Variable para controlar el sistema de turnos, white_t -> "Turno de Blancas"
    jugada = 0

    #Información para la construcción del tablero en ventana
    size = 40
    boardLength = 8

    #Creación del objeto Tablero y primer dibujado en pantalla
    texto = Text(BoardDisplay)
    texto.board_list.append(chess_notations.FEN_decode("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))
    texto.draw(jugada)

    menu = Menu(BoardDisplay)
    tablero = Board(green, yellow, charcoal, white, BoardDisplay, pygame.display.get_surface().get_size(), size, boardLength)
    piezas = Pieces(BoardDisplay, size, boardLength, texto.board_list)

    tablero.draw(white_t)
    piezas.draw(pygame.display.get_surface().get_size())
    menu.draw()
    
    while end != True: #Loop principal de eventos en ventana
        for event in pygame.event.get():
                #Configuración del botón de cerrar ventana
                if event.type == pygame.QUIT:
                    end = True
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN: #Evento que se ejecuta cuando el Mouse hace click en la ventana
                    if pressed == False and jugada == len(texto.board_list)-1: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                        #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                        for x in piezas.c_g:
                            if x.rect.collidepoint(event.pos[0], event.pos[1]) and piezas.position[x.pos[0]][x.pos[1]].isupper() == white_t:
                                movimientos = x.Movement(piezas.position)
                                piezas.mp = movimientos
                                pressed = True
                                break

                    elif pressed == True: #Se ejecuta en caso de que si se haya seleccionado una pieza
                        #Se revisa si la segunda selección en pantalla corresponde a una pieza y se actualiza el tablero&variables en función de ello
                        if 30 <= event.pos[0] <= 350 and 30 <= event.pos[1] <=440: 
                            target = ([a for a in range(1, 9) if size*a+120 > event.pos[1]][0]-1, [a for a in range(1, 9) if size*a+(30) > event.pos[0]][0]-1)
                            if x.rect.collidepoint(event.pos[0], event.pos[1]):
                                piezas.mp = []
                                pressed = False

                            elif target in movimientos:
                                compr = True if piezas.position[target[0]][target[1]] != "" else False
                                pressed = False
                                white_t = True if white_t == False else False

                                texto.board_list.append(deepcopy(texto.board_list[-1]))
                                (texto.board_list[-1])[target[0]][target[1]] = x.id if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() == True else x.id.lower()
                                (texto.board_list[-1])[x.pos[0]][x.pos[1]] = ""
                                texto.mov_list.append(pieces.Position(target, piezas.position[x.pos[0]][x.pos[1]], compr, x.pos, (texto.board_list[-1])))

                                piezas.mp = []
                                jugada += 1

                        piezas.mp = []
                        pressed = False
                    
                    for a in tablero.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 1 and jugada < len(texto.board_list)-1:
                                jugada += 1
                                white_t = False if white_t == True else True

                                a.Update()

                                #tablero.botones.draw
                            
                            elif a.k == -1 and jugada > 0:
                                jugada -= 1
                                white_t = False if white_t == True else True

                                a.Update()
                            
                            elif a.k == 0 and jugada == len(texto.board_list)-1 and jugada != 0:
                                texto.board_list.remove(texto.board_list[-1])
                                texto.mov_list.remove(texto.mov_list[-1])

                                jugada -= 1
                                white_t = False if white_t == True else True

                                a.Update()
                    
                    for a in menu.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 2:
                                a.Update()

                
                elif event.type == pygame.MOUSEBUTTONUP:
                    for a in tablero.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.im == 1:
                                a.Update()
                    
                    for a in menu.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 2:
                                a.Update()

                                end = True
                                pygame.display.quit()
                                pygame.quit()
                                Main()

                #Evitamos que el usuario pueda modificar el tamaño de la ventana fuera de nuestros parámetros
                elif event.type == VIDEORESIZE:
                    width, height = event.size
                    if width < 700:     width = 700 #Límites mínimos de altura
                    if height < 400:    height = 400 #Límites mínimos de anchura

                    BoardDisplay = pygame.display.set_mode((width, height)) #Actualización de ventana con los parámetros ajustados.
                
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if jugada > 0: 
                            jugada -= 1
                            white_t = False if white_t == True else True
                    
                    if event.key == pygame.K_RIGHT:
                        if jugada < len(texto.board_list)-1: 
                            jugada += 1
                            white_t = False if white_t == True else True

        piezas.position = texto.board_list[jugada]

        tablero.draw(white_t) #Actualización del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        piezas.draw(pygame.display.get_surface().get_size()) #Actualización del contenido del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        texto.draw(jugada)
        menu.draw()
        pygame.display.update() #Refrescar la visualización en pantalla.

if __name__ == '__main__': #Inicio de ejecución del programa
    Main() #Llamada a la función principal