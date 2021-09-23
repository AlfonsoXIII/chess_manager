#Llibreries importades
import pygame
from pygame.locals import *
from PIL import Image
import sys
from copy import deepcopy

#Scripts importats
import chess_notations
import scripts.Objects as pieces
import scripts.variables as variables
import scripts.Text as Text
import scripts.Menu as Menu
import scripts.Board as Board
import scripts.Pieces as Pieces

def Animation(Data):

    def rot_center(image, rect, angle):

        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center = rect.center)
        return rot_image,rot_rect

    if Data.menu_open == True:
        if Data.menu_pos_y != 0: 
            Data.menu_pos_y += 2
            #rot_center([x for x in menu.buttons if x.id == 5], [x for x in menu.buttons if x.id == 5].get_rect(), Data.arrow_ang+2)

        if Data.board_pos_y != 0: Data.board_pos_y += 2

    else:
        if Data.menu_pos_y != -36: Data.menu_pos_y -= 2
        if Data.board_pos_y != -20: Data.board_pos_y -= 2

'''
Funció que gestiona les accions i els events del teclat quan la
finestra no perd el focus.
'''
def Keys_Behaviour(event, Data, text, menu):
    if event.type == KEYDOWN:
        if event.key == pygame.K_LEFT:
            if Data.jugada > 0: 
                Data.jugada -= 1
                Data.white_t = False if Data.white_t == True else True
        
        if event.key == pygame.K_RIGHT:
            if Data.jugada < len(text.board_list)-1: 
                Data.jugada += 1
                Data.white_t = False if Data.white_t == True else True
        
        if event.key == pygame.K_SPACE:
            #menu.Animation()
            Data.menu_open = (True if Data.menu_open == False else False)

'''
Funció que gestiona el comportament dels botons a pantalla.
'''
def Buttons_Behaviour(event, Data, text, taulell, menu):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for a in taulell.buttons:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                if a.id == 1 and Data.jugada < len(text.board_list)-1:
                    Data.jugada += 1
                    Data.white_t = False if Data.white_t == True else True

                    a.Update()
                
                elif a.id == -1 and Data.jugada > 0:
                    Data.jugada -= 1
                    Data.white_t = False if Data.white_t == True else True

                    a.Update()
                
                elif a.id == 0 and Data.jugada == len(text.board_list)-1 and Data.jugada != 0:
                    text.board_list.remove(text.board_list[-1])

                    if (text.mov_list[-1]).castling[0] == True or (text.mov_list[-1]).castling[1] == True:
                        if (Data.jugada+1)%2 == 0:
                            Data.wk_moved = False
                        else:
                            Data.bk_moved = False
                    
                    if Data.check_mate == True:
                        Data.check_mate = False

                    text.mov_list.remove(text.mov_list[-1])

                    Data.jugada -= 1
                    Data.white_t = False if Data.white_t == True else True

                    a.Update()
                
                elif a.id == 3:
                    a.Update()

        for a in menu.buttons:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                if a.id == 2:
                    a.Update()

    elif event.type == pygame.MOUSEBUTTONUP:
        for a in taulell.buttons:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                if a.id == 3:
                    Data.reverse = (True if Data.reverse == False else False)
                    text.Reverse()

                    a.Update()

                elif a.im == 1:
                    a.Update()
        
        for a in menu.buttons:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                if a.id == 2:
                    a.Update()

                    Data.end = True
                    pygame.display.quit()
                    pygame.quit()
                    Main()

'''
Funció que implementa els canvis en pantalla per a les peces en accionar 
una d'elles.
'''
def Move(x, event, Data, size, peces, text, taulell):
    target = ([a for a in range(1, 9) if size*a+120+Data.board_pos_y > event.pos[1]][0]-1, [a for a in range(1, 9) if size*a+(30) > event.pos[0]][0]-1)
    if x.rect.collidepoint(event.pos[0], event.pos[1]):
        peces.mp = []
        taulell.selected = ()
        Data.pressed = False

    elif target in peces.mp:
        compr = True if peces.position[target[0]][target[1]] != "" else False
        Data.white_t = (True if Data.white_t == False else False)
        taulell.selected = ()
        Data.pressed = False
        text.board_list.append(deepcopy(text.board_list[-1]))

        local_castling = (False, False)
        
        if x.id == "K" and Data.castling[0] != (0, 0) and Data.castling[0] == target:
            k = (1 if Data.reverse == False else -1)
            (text.board_list[-1])[target[0]][target[1]+(-1*k)] = "R" if (text.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else "r"
            (text.board_list[-1])[x.pos[0]][x.pos[1]+(3*k)] = ""

            (text.board_list[-1])[target[0]][target[1]] = x.id if (text.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
            (text.board_list[-1])[x.pos[0]][x.pos[1]] = ""

            local_castling = (True, False)
        
        elif x.id == "K" and Data.castling[1] != (0, 0) and Data.castling[1] == target:
            k = (1 if Data.reverse == False else -1)
            (text.board_list[-1])[target[0]][target[1]+(1*k)] = "R" if (text.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else "r"
            (text.board_list[-1])[x.pos[0]][x.pos[1]+(-4*k)] = ""

            (text.board_list[-1])[target[0]][target[1]] = x.id if (text.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
            (text.board_list[-1])[x.pos[0]][x.pos[1]] = ""

            local_castling = (False, True)
        
        else:
            (text.board_list[-1])[target[0]][target[1]] = x.id if (text.board_list[-1])[x.pos[0]][x.pos[1]].isupper() else x.id.lower()
            (text.board_list[-1])[x.pos[0]][x.pos[1]] = ""

        if x.id == "K":
            if x.colour == 0: Data.wk_moved = True
            else: Data.bk_moved = True
        
        peces.position = text.board_list[-1]
        peces.draw(Data.reverse)

        check = False

        for a in peces.c_g:
            if a.id == "K" and a.colour == (0 if Data.white_t == True else 1):
                if a.Check(text.board_list[-1], a.pos) == False:
                    can_move = False
                    for b in peces.c_g:
                        if b.colour == (0 if Data.white_t == True else 1):
                            if b.id == "K": movimientos = b.Movement(peces.position)
                            else:   movimientos = b.Movement(peces.position)
                            
                            for c in movimientos:
                                temp_board = deepcopy(text.board_list[-1])
                                temp_board[c[0]][c[1]] = temp_board[b.pos[0]][b.pos[1]]
                                temp_board[b.pos[0]][b.pos[1]] = ""

                                if a.Check(temp_board, (c if b.id == "K" else a.pos)):
                                    can_move = True
                                    break                                                
                    
                    if can_move == False:
                        Data.check_mate = True

                    else:
                        temp = (a.pos[1], a.pos[0])
                        check = True   
                                                            
        text.mov_list.append(pieces.Position((target if Data.reverse == False else (7-target[0], 7-target[1])), peces.position[target[0]][target[1]], compr, (x.pos if Data.reverse == False else (7-x.pos[0], 7-x.pos[1])), (text.board_list[-1]), check, Data.check_mate, ((7-temp[0], 7-temp[1]) if Data.reverse == True else temp) if check == True else (), local_castling))
        Data.jugada += 1                          
        
        peces.mp = []

'''
Funció que corrobora si l'usuari ha fet click a una casella del taulell, i posteriorment
assigna els valors que corresponen a les variables de "Moviments Possibles" per a mostrar-los
en pantalla i s'encarrega de les comprovacions necessaries en cas de que la posició estigui
en escacs o semblant.
'''
def If_Board_Pressed(event, Data, peces, text, taulell):
    for x in peces.c_g:                               
        if x.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y) and peces.position[x.pos[0]][x.pos[1]].isupper() == Data.white_t:
            if x.id == "K":
                Data.castling = [] 
                movimientos = x.Movement(peces.position)
                if_castling = x.Castling(text.board_list[-1], (Data.wk_moved if x.colour == 0 else Data.bk_moved))
                if if_castling[0]: 
                    Data.castling.append((x.pos[0], x.pos[1]+(2*(1 if Data.reverse == False else -1))))
                    movimientos.append((x.pos[0], x.pos[1]+(2*(1 if Data.reverse == False else -1))))
                else: Data.castling.append((0, 0))
                if if_castling[1]: 
                    Data.castling.append((x.pos[0], x.pos[1]+(-2*(1 if Data.reverse == False else -1))))
                    movimientos.append((x.pos[0], x.pos[1]+(-2*(1 if Data.reverse == False else -1))))
                else: Data.castling.append((0, 0))
                
            else:   movimientos = x.Movement(peces.position)

            other_king = [b for b in peces.c_g if b.id == "K" and b.colour == (0 if Data.white_t == True else 1)]

            for a in peces.c_g:
                if a.id == "K" and a.colour == (1 if Data.white_t == True else 0):
                    for b in movimientos:
                        temp_board = deepcopy(text.board_list[-1])
                        
                        temp_board[b[0]][b[1]] = x.id if temp_board[x.pos[0]][x.pos[1]].isupper() == True else x.id.lower()
                        temp_board[x.pos[0]][x.pos[1]] = ""
                                                    
                        if (other_king[0]).Check(temp_board, (b if x.id == "K" else (other_king[0]).pos)) and (a.Check(text.board_list[-1], a.pos) or (a.Check(text.board_list[-1], a.pos) == False and a.Check(temp_board, b))):
                            taulell.selected = (x.pos[1], x.pos[0])
                            peces.mp.append(b)
                            Data.pressed = True
                            
                    break            
            return x

def Main(): #Funció principal del programa
    pygame.init()

    #Declaración de la paleta de colors per a la interfície
    yellow, green, white, charcoal = (231,231,216),(131, 175, 155),(255,255,255), (54,69,79)

    image = Image.open("images/chess_pieces.png") #Obertura del spritemap amb la llibreria PIL
    images = image.crop((120, 0, 160, 40)) #Selecció de l'icona per a la finestra
    icon = pygame.image.fromstring(images.tobytes(), images.size, images.mode) #Creació de la variable icona

    #Inicialització de la finestra
    window = pygame.display.set_mode((700, 525))
    pygame.display.set_caption("Chess Manager")
    pygame.display.set_icon(icon)
    window.fill((243,239,239))

    BoardDisplay = pygame.Surface((700, 525))
    BoardDisplay.fill(((243,239,239)))

    MenuDisplay = pygame.Surface((700, 110)).convert_alpha()
    MenuDisplay.fill((0,0,0,0))

    #Informació per a la construcció del taulell & finestra
    size = 40
    boardLength = 8
    Data = variables.Data() #Classe externa amb totes les variables principals

    #Creació de l'objecte Taulell per a la finestra i primer dibuixat
    text = Text.Text(BoardDisplay)
    text.board_list.append(chess_notations.FEN_decode("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))
    text.draw(Data.jugada)

    #Creació de l'objecte Menu per a la finestra i primer dibuixat
    menu = Menu.Menu(MenuDisplay)
    menu.Generate_Buttons()
    menu.draw()

    #Creació de l'objecte Taulell per a la finestra i primer dibuixat
    taulell = Board.Board(green, yellow, charcoal, white, BoardDisplay, pygame.display.get_surface().get_size(), size, boardLength)
    taulell.Generate_Buttons()
    taulell.draw(Data.white_t, Data.reverse)

    #Creació de l'objecte Peces per a la finestra i primer dibuixat
    peces = Pieces.Pieces(BoardDisplay, size, boardLength, text.board_list)
    peces.draw(pygame.display.get_surface().get_size())

    clock = pygame.time.Clock()
    
    while Data.end != True: #Bucle principal de la finestra
        clock.tick(60) #Limitació dels FPS a 60

        for event in pygame.event.get():

                #Configuración de l'acció de tancar la finestra
                if event.type == pygame.QUIT:
                    Data.end = True
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                
                #Event principal que captura quan l'usuari prem el mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if Data.pressed == False and Data.jugada == len(text.board_list)-1 and Data.check_mate == False: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                        #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                        x = If_Board_Pressed(event, Data, peces, text, taulell)

                    elif Data.pressed == True: #S'executa en el cas de que prèviament s'hagi seleccionat una peça
                        #Es revisa si l'usuari ha seleccionat alguna casella del taulell
                        if 30 <= event.pos[0] <= 350 and 30 <= event.pos[1] <=440: 
                            Move(x, event, Data, size, peces, text, taulell)

                        peces.mp = []
                        taulell.selected = ()
                        Data.pressed = False
                        Data.castling = ()
                    
                Buttons_Behaviour(event, Data, text, taulell, menu)
                Keys_Behaviour(event, Data, text, menu)

                #elif event.type == VIDEORESIZE:
                    #width, height = event.size
                    #if width < 700:     width = 700 #Límites mínimos de altura
                    #if height < 400:    height = 400 #Límites mínimos de anchura

                    #BoardDisplay = pygame.display.set_mode((width, height)) #Actualización de ventana con los parámetros ajustados.

        peces.position = text.board_list[Data.jugada]
        taulell.check_pos = () if Data.jugada == 0 else (text.mov_list[Data.jugada-1]).check_pos
        
        window.fill((243,239,239))
        BoardDisplay.fill((243,239,239))
        MenuDisplay.fill((0,0,0,0))

        #Redibuixat del contingut de la finestra
        taulell.draw(Data.white_t, Data.reverse)
        peces.draw(Data.reverse)
        text.draw(Data.jugada)
        menu.draw()
        Animation(Data)

        window.blit(BoardDisplay, (0, Data.board_pos_y))
        window.blit(MenuDisplay, (0, Data.menu_pos_y))
        pygame.display.update() #Actualització de la finestra

        #print(clock.get_fps())

if __name__ == '__main__': #Inici d'execució del programa
    Main() #Trucada a la funció principal