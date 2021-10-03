#Llibreries importades
import pygame
from pygame.locals import *
from PIL import Image
import sys

#Scripts importats
import chess_notations
import scripts.variables as variables
import scripts.Text as Text
import scripts.Menu as Menu
import scripts.Board as Board
import scripts.Pieces as Pieces
import scripts.side_Menu as side_Menu
import window_behaviour

def Main(): #Funció principal del programa
    pygame.init()

    #Declaración de la paleta de colors per a la interfície
    yellow, green, white, charcoal = (231,231,216), (131, 175, 155), (255,255,255), (54,69,79)

    image = Image.open("images/chess_pieces.png") #Obertura del spritemap amb la llibreria PIL
    images = image.crop((120, 0, 160, 40)) #Selecció de l'icona per a la finestra
    icon = pygame.image.fromstring(images.tobytes(), images.size, images.mode) #Creació de la variable icona

    #Càlcul de les dimensions de la finestra en relació al monitor
    info = pygame.display.Info()
    screen_width,screen_height = info.current_w,info.current_h
    window_width,window_height = screen_width,screen_height-60

    #Inicialització de la finestra
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Chess Manager")
    pygame.display.set_icon(icon)
    window.fill((243,239,239))
    
    #Creació de les diverses superfícies de treball
    BoardDisplay = pygame.Surface((window_width, window_height)).convert_alpha()
    BoardDisplay.fill((0,0,0,0))

    sideMenuDisplay = pygame.Surface((window_width, window_height+100)).convert_alpha()
    sideMenuDisplay.fill((0,0,0,0))

    MenuDisplay = pygame.Surface((window_width, window_height)).convert_alpha()
    MenuDisplay.fill((0,0,0,0))

    #Informació per a la construcció del taulell & finestra
    Data = variables.Data() #Classe externa amb totes les variables principals
    Data.proportion = window_behaviour.Proportion((window_width,window_height), (700, 525))
    Data.text_relative_center = [((window_width)-(700*Data.proportion))/2, (((window_width)-(700*Data.proportion))/2)/2]
    Data.menu_pos_y = int(-75*Data.proportion)
    Data.board_pos_y = int(-49*Data.proportion)
    Data.static_relative_center = [Data.text_relative_center[0]/2, Data.text_relative_center[0]]
    Data.relative_center = Data.text_relative_center[0]/2

    size = int(40*Data.proportion)
    boardLength = 8

    #Creació de l'objecte Taulell per a la finestra i primer dibuixat
    text = Text.Text(BoardDisplay, 
                    Data.proportion,
                    Data.text_relative_center)
    text.board_list.append(chess_notations.FEN_decode("8/1k2r3/8/8/8/8/8/2K5")) #("5k2/7P/8/8/8/8/8/1K6")
    text.draw(Data.jugada, Data.text_data, 1, Data.text_relative_center[0])

    #Creació de l'objecte Menu per a la finestra i primer dibuixat
    menu = Menu.Menu(MenuDisplay, 
                    Data.proportion)
    menu.Generate_Buttons()
    menu.draw()

    #Creació de l'objecte Taulell per a la finestra i primer dibuixat
    taulell = Board.Board(green, 
                        yellow, 
                        charcoal, 
                        white, 
                        BoardDisplay, 
                        pygame.display.get_surface().get_size(), 
                        size, 
                        boardLength, 
                        Data.proportion)
    taulell.Generate_Buttons()
    taulell.draw(Data.white_t, 
                Data.reverse)

    #Creació de l'objecte Peces per a la finestra i primer dibuixat
    peces = Pieces.Pieces(BoardDisplay, 
                        size, 
                        boardLength, 
                        text.board_list, 
                        Data.proportion)
    peces.draw(Data.reverse)

    menu_lateral= side_Menu.side_Menu(sideMenuDisplay)
    menu_lateral.Build()
    menu_lateral.Draw(Data.side_menu_on)

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
                    if Data.pressed == False and Data.jugada == len(text.board_list)-1 and Data.check_mate == False and Data.freeze == False: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                        #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                        x = window_behaviour.If_Board_Pressed(event, Data, peces, text, taulell)

                    elif Data.pressed == True: #S'executa en el cas de que prèviament s'hagi seleccionat una peça
                        #Es revisa si l'usuari ha seleccionat alguna casella del taulell
                        if (30*Data.proportion) <= event.pos[0]-Data.relative_center <= (350*Data.proportion) and (120*Data.proportion) <= event.pos[1]-Data.board_pos_y <= (440*Data.proportion): 
                            window_behaviour.Move(x, event, Data, size, peces, text, taulell, menu_lateral)

                        peces.mp = []
                        taulell.selected = ()
                        Data.pressed = False
                        Data.castling = ()
                
                window_behaviour.Buttons_Behaviour(event, Data, text, taulell, menu, peces, menu_lateral)
                window_behaviour.Keys_Behaviour(event, Data, text, menu)

        peces.position = text.board_list[Data.jugada]
        taulell.check_pos = ([] if Data.jugada == 0 else (Data.text_data[Data.jugada-1])[1])
        
        window.fill((243,239,239))
        sideMenuDisplay.fill((0,0,0,0))
        BoardDisplay.fill((243,239,239)) #(243,239,239)
        MenuDisplay.fill((0,0,0,0))

        #Redibuixat del contingut de la finestra
        taulell.draw(Data.white_t, Data.reverse)
        peces.Update()
        text.draw(Data.jugada, Data.text_data, clock.get_fps(), (Data.text_relative_center[0] if Data.side_menu_on == False else Data.text_relative_center[1]))
        menu.draw()
        window_behaviour.Animation(Data, menu)
        menu_lateral.Draw(Data.side_menu_on)

        window.blit(BoardDisplay, (Data.relative_center, Data.board_pos_y))
        window.blit(sideMenuDisplay, (0, Data.board_pos_y))
        window.blit(MenuDisplay, (0, Data.menu_pos_y))
        pygame.display.update() #Actualització de la finestra

if __name__ == '__main__': #Inici d'execució del programa
    Main() #Trucada a la funció principal