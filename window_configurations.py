#Llibreries importades
import pygame
from pygame.locals import *
import sys

#Scripts importats
import window_behaviour
import scripts.ai.alpha_beta_pruning as ai

def Analysis_Environment(window, sideMenuDisplay, BoardDisplay, MenuDisplay, Data, text, peces, taulell, menu_lateral, menu, ai_text, Queue, size, clock):

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
                Data.catch_piece = window_behaviour.If_Board_Pressed(event, Data, peces, text, taulell, 1)

            elif Data.pressed == True: #S'executa en el cas de que prèviament s'hagi seleccionat una peça
                #Es revisa si l'usuari ha seleccionat alguna casella del taulell
                if (40.457*Data.proportion) <= event.pos[0]-Data.relative_center <= (471.99*Data.proportion) and (161.828*Data.proportion) <= event.pos[1]-Data.board_pos_y <= (593.371*Data.proportion): 
                    window_behaviour.Move(Data.catch_piece, event, Data, size, peces, text, taulell, menu_lateral, 1)

                peces.mp = []
                taulell.selected = ()
                Data.pressed = False
                Data.castling = ()
        
        window_behaviour.Buttons_Behaviour(event, Data, text, taulell, menu, peces, menu_lateral, ai_text)
        window_behaviour.Keys_Behaviour(event, Data, text, menu)
    
    if Data.module_on == True:
        window_behaviour.Analisis_Behaviour(text, ai, Queue, Data, text.board_list[Data.jugada])

    peces.position = text.board_list[Data.jugada+Data.page*26]
    taulell.check_pos = ([] if Data.jugada == 0 else (Data.text_data[Data.page][Data.jugada-1])[1])

    window.fill((243,239,239))
    sideMenuDisplay.fill((0,0,0,0))
    BoardDisplay.fill((243,239,239))
    MenuDisplay.fill((0,0,0,0))

    #Redibuixat del contingut de la finestra
    taulell.draw(Data.white_t, Data.reverse, Data.play_mode)
    peces.Update()
    text.draw(Data.jugada, Data.text_data, clock.get_fps(), (Data.text_relative_center[0] if Data.side_menu_on == False else Data.text_relative_center[1]), Data)
    ai_text.draw(Data.module_value, (Data.text_relative_center[0] if Data.side_menu_on == False else Data.text_relative_center[1]))
    menu.draw()
    window_behaviour.Animation(Data, menu)
    menu_lateral.Draw(Data.side_menu_on)

    window.blit(BoardDisplay, (Data.relative_center, Data.board_pos_y))
    window.blit(sideMenuDisplay, (0, Data.board_pos_y))
    window.blit(MenuDisplay, (0, Data.menu_pos_y))


def Play_Environment(window, sideMenuDisplay, BoardDisplay, MenuDisplay, Data, text, peces, taulell, menu_lateral, menu, ai_text, Queue, size, clock):

    for event in pygame.event.get():

        #Configuración de l'acció de tancar la finestra
        if event.type == pygame.QUIT:
            Data.end = True
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        
        #Event principal que captura quan l'usuari prem el mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Data.pressed == False and Data.check_mate == False and Data.freeze == False: #Se ejecuta si aún no se ha seleccionado ninguna pieza
                #Se revisa que la selección corresponda a una pieza y se muestra en pantalla las opciones de movimiento, actualizando las variables de control.
                Data.catch_piece = window_behaviour.If_Board_Pressed(event, Data, peces, text, taulell, 3.5)

            elif Data.pressed == True: #S'executa en el cas de que prèviament s'hagi seleccionat una peça
                #Es revisa si l'usuari ha seleccionat alguna casella del taulell
                if (40.457*Data.proportion) <= event.pos[0]-(Data.relative_center*3.5) <= (471.99*Data.proportion) and (161.828*Data.proportion) <= event.pos[1]-Data.board_pos_y <= (593.371*Data.proportion): 
                    window_behaviour.Move(Data.catch_piece, event, Data, size, peces, text, taulell, menu_lateral, 3.5)

                peces.mp = []
                taulell.selected = ()
                Data.pressed = False
                Data.castling = ()
        
        window_behaviour.Buttons_Behaviour(event, Data, text, taulell, menu, peces, menu_lateral, ai_text)
        window_behaviour.Keys_Behaviour(event, Data, text, menu)
    
    if Data.white_t != Data.module_turn:
        window_behaviour.Play_Behaviour(text, ai, Queue, Data, text.board_list[-1])

        if Data.module_value != None:
            text.board_list.append(Data.module_value)

            peces.position = text.board_list[-1]
            peces.draw(Data.reverse)

            Data.module_value = None
            Data.white_t = (True if Data.white_t == False else False)

    peces.position = text.board_list[-1]
    taulell.check_pos = ([] if Data.jugada == 0 else (Data.text_data[Data.page][Data.jugada-1])[1])

    window.fill((243,239,239))
    sideMenuDisplay.fill((0,0,0,0))
    BoardDisplay.fill((243,239,239))
    MenuDisplay.fill((0,0,0,0))

    #Redibuixat del contingut de la finestra
    taulell.draw(Data.white_t, Data.reverse, Data.play_mode)
    peces.Update()
    menu.draw()
    window_behaviour.Animation(Data, menu)
    menu_lateral.Draw(Data.side_menu_on)

    window.blit(BoardDisplay, (Data.relative_center*3.5, Data.board_pos_y))
    window.blit(sideMenuDisplay, (0, Data.board_pos_y))
    window.blit(MenuDisplay, (0, Data.menu_pos_y))