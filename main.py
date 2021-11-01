#Llibreries importades
import multiprocessing
import pygame
from pygame.locals import *
from PIL import Image
import sys

#Scripts importats
import chess_notations
import window_configurations as configs
import scripts.variables as variables
import scripts.Text as Text
import scripts.ai_text as AI_Text
import scripts.Menu as Menu
import scripts.Board as Board
import scripts.Pieces as Pieces
import scripts.side_Menu as side_Menu
import window_behaviour

def Main(precharged_data): #Funció principal del programa
    pygame.init()

    #Declaració de la paleta de colors per a la interfície
    yellow, green, white, charcoal = (231,231,216), (131, 175, 155), (255,255,255), (54,69,79)

    icon = pygame.image.load("images/ico.png")

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
    Data.precharged_data = precharged_data
    Data.proportion = window_behaviour.Proportion((window_width,window_height), (1360, 708))
    Data.text_relative_center = [((window_width)-(943.99*Data.proportion))/2, (((window_width)-(943.99*Data.proportion))/2)/2]
    Data.menu_pos_y = int(-101.14*Data.proportion)
    Data.board_pos_y = int(-66.08*Data.proportion)
    Data.static_relative_center = [Data.text_relative_center[0]/2, Data.text_relative_center[0]]
    Data.relative_center = Data.text_relative_center[0]/2

    size = int(53.94*Data.proportion)
    boardLength = 8

    #Creació de l'objecte Taulell per a la finestra i primer dibuixat
    text = Text.Text(BoardDisplay, 
                    Data.proportion,
                    Data.text_relative_center)
    text.board_list.append(chess_notations.FEN_decode("8/1k2r3/8/8/8/8/8/2K5")) #("5k2/7P/8/8/8/8/8/1K6")
    text.build(Data.precharged_data, Data.text_relative_center[0])
    text.draw(Data.jugada, Data.text_data, 1, Data.text_relative_center[0], Data)

    ai_text = AI_Text.Text(BoardDisplay,
                        Data.proportion,
                        Data.text_relative_center)
    ai_text.build(Data.precharged_data, Data.text_relative_center[0])
    ai_text.draw("off", Data.text_relative_center[0])

    #Creació de l'objecte Menu per a la finestra i primer dibuixat
    menu = Menu.Menu(MenuDisplay, 
                    Data.proportion)
    menu.Generate_Buttons(Data.precharged_data)
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
    taulell.Generate_Buttons(Data.precharged_data)
    taulell.draw(Data.white_t, 
                Data.reverse,
                Data.play_mode)

    #Creació de l'objecte Peces per a la finestra i primer dibuixat
    peces = Pieces.Pieces(BoardDisplay, 
                        size, 
                        boardLength, 
                        text.board_list, 
                        Data.proportion,
                        Data.precharged_data)
    peces.draw(Data.reverse)

    menu_lateral= side_Menu.side_Menu(sideMenuDisplay, Data.proportion)
    menu_lateral.Build(Data.precharged_data)
    menu_lateral.Draw(Data.side_menu_on)

    clock = pygame.time.Clock()

    Queue = multiprocessing.Queue()

    while Data.end != True: #Bucle principal de la finestra
        clock.tick(60) #Limitació dels FPS a 60

        if Data.play_mode == True:
            configs.Analysis_Environment(window,
                                        sideMenuDisplay,
                                        BoardDisplay,
                                        MenuDisplay,
                                        Data,
                                        text,
                                        peces,
                                        taulell,
                                        menu_lateral,
                                        menu,
                                        ai_text,
                                        Queue,
                                        size,
                                        clock)
        
        else:
            configs.Play_Environment(window,
                                    sideMenuDisplay,
                                    BoardDisplay,
                                    MenuDisplay,
                                    Data,
                                    text,
                                    peces,
                                    taulell,
                                    menu_lateral,
                                    menu,
                                    ai_text,
                                    Queue,
                                    size,
                                    clock)

        pygame.display.update() #Actualització de la finestra