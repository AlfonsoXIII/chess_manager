#Diversas librerias, y parámetros de estas, importadas
import pygame
from pygame.locals import *
from pygame.constants import RESIZABLE
from PIL import Image
import sys
import math
from copy import deepcopy

from pygame.version import rev

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
        #arial = pygame.font.Font("fonts/free-serif.ttf", 35)

        pygame.draw.rect(self.screen, (220, 220, 220),[380,115,295, (math.trunc(len(self.mov_list)/6)+1)*30])
        pygame.draw.rect(self.screen,((189,189,189)),[377,112,301,6+((math.trunc(len(self.mov_list)/6)+1)*30)],3, border_radius=10)

        for x in self.mov_list:
            self.screen.blit(arial.render(chess_notations.algebraic_de(x.text, x.pos, x.capture, x.pos_or, str(str(int((self.mov_list.index(x)+1)/2)+1)+ ". ") if (self.mov_list.index(x))%2 == 0 else "", x.check, x.check_mate, x.castling), True, (0, 0, 0)),(390+((self.mov_list.index(x) if self.mov_list.index(x)<6 else self.mov_list.index(x) - math.trunc(self.mov_list.index(x)/6)*6)*50),30*(1 if self.mov_list.index(x)<6 else math.trunc(self.mov_list.index(x)/6)+1)+94))
            
            if jugada >= 0 and self.mov_list.index(x)+1 == jugada:
                pygame.draw.circle(self.screen, (255, 0, 0), (390+((self.mov_list.index(x) if self.mov_list.index(x)<6 else self.mov_list.index(x) - math.trunc(self.mov_list.index(x)/6)*6)*50),30*(1 if self.mov_list.index(x)<6 else math.trunc(self.mov_list.index(x)/6)+1)+94), 2)

    def Reverse(self):
        for x in self.board_list:
            x.reverse()
            for y in x:
                y.reverse()

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
        self.selected = ()
        self.check_pos = ()

        self.botones = pygame.sprite.Group()

        flip = pieces.Button("images/flip_board.png", (0, 146, 149, 292), (0, 0, 149, 146), (20, 20), 3)
        flip.rect.x = 26
        flip.rect.y = 460

        move_1 = pieces.Button("images/right_pressed_.png", (0, 145, 347, 290), (0, 0, 347, 142), (80, 40), 1)
        move_1.rect.x = 236
        move_1.rect.y = 460

        move_2 = pieces.Button("images/left_pressed.png", (0, 145, 347, 290), (0, 0, 347, 142), (80, 40), -1)
        move_2.rect.x = 66
        move_2.rect.y = 460

        rem = pieces.Button("images/rem_pressed.png", (0, 146, 149, 292), (0, 0, 149, 146), (40, 40), 0)
        rem.rect.x = 171
        rem.rect.y = 460
        
        self.botones.add(move_1)
        self.botones.add(move_2)
        self.botones.add(rem)
        self.botones.add(flip)
    
    def draw(self, white_t, fliped): #Constructor de Objeto
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

        if len(self.selected) != 0:
            pygame.draw.rect(self.screen, (200, 200, 200), [30+self.b_size*self.selected[0], 120+self.b_size*self.selected[1], self.b_size, self.b_size])
        
        if len(self.check_pos) != 0:
            local_checkpos = (self.check_pos if fliped == False else (7-self.check_pos[0], 7-self.check_pos[1]))
            pygame.draw.rect(self.screen, (240,128,128), [30+self.b_size*local_checkpos[0], 120+self.b_size*local_checkpos[1], self.b_size, self.b_size])

        pygame.draw.rect(self.screen,self.charcoal,[20,110,self.b_len*self.b_size+18,self.b_len*self.b_size+20],10, border_radius=10)

        pygame.draw.circle(self.screen, (0, 0, 0), (367.5, 110), 8)
        pygame.draw.circle(self.screen, (255, 255, 255), (367.5, 110), 6) if white_t == True else pygame.draw.circle(self.screen, (0, 0, 0), (367.5, 110), 6)

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

    def draw(self, reverse): #Constructor de Objeto
        self.c_g = [] #Limpiar array de sprites para redibujado
        self.c_g = pygame.sprite.Group()

        #Deployment de piezas
        for i in range(0, 8):
            for z in range(0 ,8):
                #Determinar el color de las piezas
                cl = 0 if self.position[z][i].isupper() else 1

                #Creación de objeto "Peón"
                if self.position[z][i].capitalize() == "P":
                    pawn = pieces.Pawn(cl, (z, i), reverse)

                    pawn.rect.x = 30+self.b_size*(i)
                    pawn.rect.y = 120+self.b_size*(z)

                    self.c_g.add(pawn)
                
                #Creación de objeto "Rey"
                elif self.position[z][i].capitalize() == "K":
                    king = pieces.King(cl, (z, i), reverse)

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
                    if self.position[i][z] == "":
                        pygame.draw.circle(self.screen, (97,97,97), (30+self.b_size*(z)+20, 120+self.b_size*(i)+20), 5)

                    else:
                        pygame.draw.rect(self.screen, (97,97,97),[30+self.b_size*(z), 120+self.b_size*(i), 40, 40], 2, border_radius = 10)
                     
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
    pygame.display.set_caption("Chess Manager")
    pygame.display.set_icon(icon)
    BoardDisplay.fill((243,239,239))
    
    end = False #Variable para controlar el fin del bucle principal del programa
    pressed = False #Variable para controlar el sistema de selección de piezas
    white_t = True #Variable para controlar el sistema de turnos, white_t -> "Turno de Blancas"
    reverse = False
    jugada = 0
    check = False
    check_mate = False
    wk_moved = False
    bk_moved = False
    castling = []

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

    tablero.draw(white_t, reverse)
    piezas.draw(pygame.display.get_surface().get_size())
    menu.draw()

    clock = pygame.time.Clock()
    
    while end != True: #Loop principal de eventos en ventana
        clock.tick(60)
        for event in pygame.event.get():
                #Configuración del botón de cerrar ventana
                if event.type == pygame.QUIT:
                    end = True
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN: #Evento que se ejecuta cuando el Mouse hace click en la ventana
                    if pressed == False and jugada == len(texto.board_list)-1 and check_mate == False: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                        #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                        for x in piezas.c_g:                               
                            if x.rect.collidepoint(event.pos[0], event.pos[1]) and piezas.position[x.pos[0]][x.pos[1]].isupper() == white_t:
                                if x.id == "K":
                                    castling = [] 
                                    movimientos = x.Movement(piezas.position)
                                    if_castling = x.Castling(texto.board_list[-1], (wk_moved if x.colour == 0 else bk_moved))
                                    if if_castling[0]: 
                                        castling.append((x.pos[0], x.pos[1]+(2*(1 if reverse == False else -1))))
                                        movimientos.append((x.pos[0], x.pos[1]+(2*(1 if reverse == False else -1))))
                                    else: castling.append((0, 0))
                                    if if_castling[1]: 
                                        castling.append((x.pos[0], x.pos[1]+(-2*(1 if reverse == False else -1))))
                                        movimientos.append((x.pos[0], x.pos[1]+(-2*(1 if reverse == False else -1))))
                                    else: castling.append((0, 0))
                                    
                                else:   movimientos = x.Movement(piezas.position)

                                other_king = [b for b in piezas.c_g if b.id == "K" and b.colour == (0 if white_t == True else 1)]

                                for a in piezas.c_g:
                                    if a.id == "K" and a.colour == (1 if white_t == True else 0):
                                        for b in movimientos:
                                            temp_board = deepcopy(texto.board_list[-1])
                                            
                                            temp_board[b[0]][b[1]] = x.id if temp_board[x.pos[0]][x.pos[1]].isupper() == True else x.id.lower()
                                            temp_board[x.pos[0]][x.pos[1]] = ""
                                                                       
                                            if (other_king[0]).Check(temp_board, (b if x.id == "K" else (other_king[0]).pos)) and (a.Check(texto.board_list[-1], a.pos) or (a.Check(texto.board_list[-1], a.pos) == False and a.Check(temp_board, b))):
                                                tablero.selected = (x.pos[1], x.pos[0])
                                                piezas.mp.append(b)
                                                pressed = True
                                                
                                        break
                                break

                    elif pressed == True: #Se ejecuta en caso de que si se haya seleccionado una pieza
                        #Se revisa si la segunda selección en pantalla corresponde a una pieza y se actualiza el tablero&variables en función de ello
                        if 30 <= event.pos[0] <= 350 and 30 <= event.pos[1] <=440: 
                            target = ([a for a in range(1, 9) if size*a+120 > event.pos[1]][0]-1, [a for a in range(1, 9) if size*a+(30) > event.pos[0]][0]-1)
                            if x.rect.collidepoint(event.pos[0], event.pos[1]):
                                piezas.mp = []
                                tablero.selected = ()
                                pressed = False

                            elif target in piezas.mp:
                                compr = True if piezas.position[target[0]][target[1]] != "" else False
                                white_t = (True if white_t == False else False)
                                tablero.selected = ()
                                pressed = False
                                texto.board_list.append(deepcopy(texto.board_list[-1]))

                                local_castling = (False, False)
                                print(castling)
                                
                                if x.id == "K" and castling[0] != (0, 0) and castling[0] == target:
                                    k = (1 if reverse == False else -1)
                                    (texto.board_list[-1])[target[0]][target[1]+(-1*k)] = "R" if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else "r"
                                    (texto.board_list[-1])[x.pos[0]][x.pos[1]+(3*k)] = ""

                                    (texto.board_list[-1])[target[0]][target[1]] = x.id if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
                                    (texto.board_list[-1])[x.pos[0]][x.pos[1]] = ""

                                    local_castling = (True, False)
                                
                                elif x.id == "K" and castling[1] != (0, 0) and castling[1] == target:
                                    k = (1 if reverse == False else -1)
                                    (texto.board_list[-1])[target[0]][target[1]+(1*k)] = "R" if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else "r"
                                    (texto.board_list[-1])[x.pos[0]][x.pos[1]+(-4*k)] = ""

                                    (texto.board_list[-1])[target[0]][target[1]] = x.id if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
                                    (texto.board_list[-1])[x.pos[0]][x.pos[1]] = ""

                                    local_castling = (False, True)
                                
                                else:
                                    (texto.board_list[-1])[target[0]][target[1]] = x.id if (texto.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
                                    (texto.board_list[-1])[x.pos[0]][x.pos[1]] = ""

                                if x.id == "K":
                                    if x.colour == 0: wk_moved = True
                                    else: bk_moved = True
                                
                                piezas.position = texto.board_list[-1]
                                piezas.draw(reverse)

                                check = False

                                for a in piezas.c_g:
                                    if a.id == "K" and a.colour == (0 if white_t == True else 1):
                                        if a.Check(texto.board_list[-1], a.pos) == False:
                                            can_move = False
                                            for b in piezas.c_g:
                                                if b.colour == (0 if white_t == True else 1):
                                                    if b.id == "K": movimientos = b.Movement(piezas.position)
                                                    else:   movimientos = b.Movement(piezas.position)
                                                    
                                                    for c in movimientos:
                                                        temp_board = deepcopy(texto.board_list[-1])
                                                        temp_board[c[0]][c[1]] = temp_board[b.pos[0]][b.pos[1]]
                                                        temp_board[b.pos[0]][b.pos[1]] = ""

                                                        if a.Check(temp_board, (c if b.id == "K" else a.pos)):
                                                            can_move = True
                                                            break                                                
                                            
                                            if can_move == False:
                                                check_mate = True

                                            else:
                                                temp = (a.pos[1], a.pos[0])
                                                check = True   
                                                                                  
                                texto.mov_list.append(pieces.Position((target if reverse == False else (7-target[0], 7-target[1])), piezas.position[target[0]][target[1]], compr, (x.pos if reverse == False else (7-x.pos[0], 7-x.pos[1])), (texto.board_list[-1]), check, check_mate, ((7-temp[0], 7-temp[1]) if reverse == True else temp) if check == True else (), local_castling))
                                jugada += 1                          
                                
                                piezas.mp = []

                        piezas.mp = []
                        tablero.selected = ()
                        pressed = False
                        castling = ()
                    
                    for a in tablero.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 1 and jugada < len(texto.board_list)-1:
                                jugada += 1
                                white_t = False if white_t == True else True

                                a.Update()
                            
                            elif a.k == -1 and jugada > 0:
                                jugada -= 1
                                white_t = False if white_t == True else True

                                a.Update()
                            
                            elif a.k == 0 and jugada == len(texto.board_list)-1 and jugada != 0:
                                texto.board_list.remove(texto.board_list[-1])

                                if (texto.mov_list[-1]).castling[0] == True or (texto.mov_list[-1]).castling[1] == True:
                                    if (jugada+1)%2 == 0:
                                        wk_moved = False
                                    else:
                                        bk_moved = False
                                
                                if check_mate == True:
                                    check_mate = False

                                texto.mov_list.remove(texto.mov_list[-1])

                                jugada -= 1
                                white_t = False if white_t == True else True

                                a.Update()
                            
                            elif a.k == 3:
                                a.Update()
                    
                    for a in menu.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 2:
                                a.Update()

                
                elif event.type == pygame.MOUSEBUTTONUP:
                    for a in tablero.botones:
                        if a.rect.collidepoint(event.pos[0], event.pos[1]):
                            if a.k == 3:
                                reverse = (True if reverse == False else False)
                                texto.Reverse()

                                a.Update()

                            elif a.im == 1:
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
                #elif event.type == VIDEORESIZE:
                    #width, height = event.size
                    #if width < 700:     width = 700 #Límites mínimos de altura
                    #if height < 400:    height = 400 #Límites mínimos de anchura

                    #BoardDisplay = pygame.display.set_mode((width, height)) #Actualización de ventana con los parámetros ajustados.
                
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
        tablero.check_pos = () if jugada == 0 else (texto.mov_list[jugada-1]).check_pos

        tablero.draw(white_t, reverse) #Actualización del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        piezas.draw(reverse) #Actualización del contenido del tablero en pantalla por cada tick y en función de las longitudes de la ventana.
        texto.draw(jugada)
        menu.draw()
        pygame.display.update() #Refrescar la visualización en pantalla.

        #print(clock.get_fps())

if __name__ == '__main__': #Inicio de ejecución del programa
    Main() #Llamada a la función principal