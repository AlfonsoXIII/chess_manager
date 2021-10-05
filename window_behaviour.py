#Llibreries importades
import pygame
from copy import deepcopy
import webbrowser
import os
import easygui

#Scripts importats
import scripts.side_Menu
import chess_notations

def side_MenuWindow(Data, enabled):
    if enabled == True:
        Data.relative_center = Data.static_relative_center[1]

    else:
        Data.relative_center = Data.static_relative_center[0]
'''
Funció encarregada de calcular la proporció a la que tots
els elements de la finestra s'hauran d'escalar mantenint 
l'aspect ratio original i en funció de la resolució del monitor
de l'usuari.
'''
def Proportion(display_dimensions, original_dimensions):
    if (display_dimensions[0]-original_dimensions[0]) <= (display_dimensions[1]-original_dimensions[1]):
        return display_dimensions[0]/original_dimensions[0]
    
    else:
        return display_dimensions[1]/original_dimensions[1]

'''
Funció encarregada d'animar les transicions en finestra en
activar el menú o desactivar-lo.
'''
def Animation(Data, menu):
    if Data.menu_open == True:
        if Data.menu_counter[0] != 20: 
            Data.menu_pos_y += int(5.057*Data.proportion)
            Data.menu_counter[0] += 1

            for a in menu.buttons:
                if a.id == 5:
                    a.Update(1)

        if Data.menu_counter[1] != 18: 
            Data.board_pos_y += int(5.057*Data.proportion)
            Data.menu_counter[1] += 1

    else:
        if Data.menu_counter[0] != 0:
            Data.menu_pos_y -= int(5.057*Data.proportion)
            Data.menu_counter[0] -= 1

            for a in menu.buttons:
                if a.id == 5:
                    a.Update(-1)

        if Data.menu_counter[1] != 4: 
            Data.board_pos_y -= int(5.057*Data.proportion)
            Data.menu_counter[1] -= 1

'''
Funció que gestiona les accions i els events del teclat quan la
finestra no perd el focus.
'''
def Keys_Behaviour(event, Data, text, menu):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if Data.jugada > 0: 
                Data.jugada -= 1
                Data.white_t = False if Data.white_t == True else True
        
        if event.key == pygame.K_RIGHT:
            if Data.jugada < len(text.board_list)-1: 
                Data.jugada += 1
                Data.white_t = False if Data.white_t == True else True

def promotion_Move(Data, peces, text, taulell, sideMenu, piece, pos, pos_or):
    Data.white_t = (True if Data.white_t == False else False)
    taulell.selected = ()
    Data.pressed = False
    text.board_list.append(deepcopy(text.board_list[-1]))
    
    (text.board_list[-1])[pos[0]][pos[1]] = (piece if (text.board_list[-1])[pos_or[0]][pos_or[1]].isupper() else piece.lower())
    (text.board_list[-1])[pos_or[0]][pos_or[1]] = ""

    peces.position = text.board_list[-1]
    peces.draw(Data.reverse)

    check = False
    temp = []

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
                                                        
    Data.text_data.append((chess_notations.algebraic_de(peces.position[pos[0]][pos[1]], 
                                                        (pos if Data.reverse == False else (7-pos[0], 7-pos[1])),
                                                        False,
                                                        (pos_or if Data.reverse == False else (7-pos_or[0], 7-pos_or[1])),
                                                        (str("{} ").format((str(int(Data.jugada/2)+1)+".") if Data.jugada%2 == 0 else "")),
                                                        check,
                                                        Data.check_mate,
                                                        (False, False)), temp))

    Data.jugada += 1                          
    peces.mp = []

'''
Funció que gestiona el comportament dels botons a pantalla.
'''
def Buttons_Behaviour(event, Data, text, taulell, menu, peces, sideMenu):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for a in taulell.buttons:
            if a.rect.collidepoint(event.pos[0]-Data.relative_center, event.pos[1]-Data.board_pos_y):
                if a.id == 1 and Data.jugada < len(text.board_list)-1:
                    Data.jugada += 1
                    Data.white_t = False if Data.white_t == True else True

                    a.Update()

                    peces.position = text.board_list[Data.jugada]
                    peces.draw(Data.reverse)
                    
                    Data.catch_button = a
                
                elif a.id == -1 and Data.jugada > 0:
                    Data.jugada -= 1
                    Data.white_t = False if Data.white_t == True else True

                    a.Update()

                    peces.position = text.board_list[Data.jugada]
                    peces.draw(Data.reverse)

                    Data.catch_button = a
                
                elif a.id == 0 and Data.jugada == len(text.board_list)-1 and Data.jugada != 0:
                    text.board_list.remove(text.board_list[-1])

                    if "0-0" in (Data.text_data[-1][0]) or "0-0-0" in (Data.text_data[-1][0]):
                        if (Data.jugada+1)%2 == 0:
                            Data.wk_moved = False
                        else:
                            Data.bk_moved = False
                    
                    if Data.check_mate == True:
                        Data.check_mate = False

                    Data.text_data.remove(Data.text_data[-1])

                    Data.jugada -= 1
                    Data.white_t = (False if Data.white_t == True else True)

                    a.Update()
                    Data.catch_button = a

                    peces.position = text.board_list[Data.jugada]
                    peces.draw(Data.reverse)
                
                elif a.id == 3:
                    a.Update()
                    Data.catch_button = a

        for a in menu.buttons:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.menu_pos_y):
                if a.id == 4:
                    Data.menu_open = (True if Data.menu_open == False else False)
                
                elif a.id == 6:
                    a.Update()
                    Data.catch_button = a

                    if sideMenu.menus_active["Config"] == False:
                        sideMenu.content.append(scripts.side_Menu.config_menu(sideMenu.screen, Data.proportion))
                        sideMenu.content[-1].Build()
                        sideMenu.menus_active["Config"] = True
                    
                    if Data.side_menu_on == False:
                        Data.side_menu_on = True
                        side_MenuWindow(Data, Data.side_menu_on)

                elif a.id == 9 or a.id == 10 or a.id == 11 or a.id == 12 or a.id == 13 or a.id == 14:
                    a.Update()
                    Data.catch_button = a
        
        for a in sideMenu.buttons:
            if a.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                sideMenu.Switch(sideMenu.buttons.index(a))

        for a in sideMenu.buttons_1:
            if a.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                a.Update()
                Data.catch_button = a

        ############################## EVENTS BOTONS EXTERNS del MENÚ LATERAL ##############################
        for a in sideMenu.content:
            for b in a.buttons:
                if b.rect.collidepoint(event.pos[0], event.pos[1]-Data.board_pos_y):
                    ########## EVENTS MENÚ PROMOCIÓ ##########
                    if a.id == "Promotion":
                        a.catch_piece = b
                        a.selected = [b.rect.x, b.rect.y, 60, 60]
                    
                    ########## EVENTS MENÚ CONFIGURACIÓ ##########
                    if a.id == "Config":
                        b.Update()

    elif event.type == pygame.MOUSEBUTTONUP:
        if Data.catch_button != None:
            Data.catch_button.Update()

            if Data.catch_button.id == 3:
                Data.reverse = (True if Data.reverse == False else False)
                text.Reverse()
                peces.draw(Data.reverse)

            elif Data.catch_button.id == 7:
                    if (sideMenu.content[sideMenu.content_shown]).id == "Promotion" and (sideMenu.content[sideMenu.content_shown]).catch_piece != None:
                        promotion_Move(Data, 
                                        peces, 
                                        text, 
                                        taulell, 
                                        sideMenu, 
                                        ((sideMenu.content[sideMenu.content_shown]).catch_piece).id, 
                                        (sideMenu.content[sideMenu.content_shown]).pos, 
                                        (sideMenu.content[sideMenu.content_shown]).pos_or)
                    
                    sideMenu.menus_active[sideMenu.content[sideMenu.content_shown].id] = False
                    sideMenu.content.remove(sideMenu.content[sideMenu.content_shown])

                    Data.freeze = False

                    if len(sideMenu.content) == 0:
                        Data.side_menu_on = False
                        side_MenuWindow(Data, Data.side_menu_on)
                    
                    else:
                        sideMenu.content_shown -= 1
            
            elif Data.catch_button.id == 8:
                Data.freeze = False
                sideMenu.menus_active[sideMenu.content[sideMenu.content_shown].id] = False
                sideMenu.content.remove(sideMenu.content[sideMenu.content_shown])

                if len(sideMenu.content) == 0:
                    Data.side_menu_on = False
                    side_MenuWindow(Data, Data.side_menu_on)
                
                else:
                    sideMenu.content_shown -= 1
            
            elif Data.catch_button.id == 9:
                path = easygui.filesavebox(msg = "EMMAGATZEMAR POSICIÓ",
                                            title = "Cercador",
                                            default= "*.ccmm")
                
                if path != None:
                    chess_notations.generate_file(Data, text.board_list, Data.text_data, path)
            
            elif Data.catch_button.id == 10:
                path = easygui.fileopenbox(msg = "OBRIR POSICIÓ",
                                            title = "Cercador",
                                            default= "*.ccmm",
                                            filetypes = ["*.ccmm"],
                                            multiple = False)

                if path != None:
                    data = chess_notations.charge_file(path)

                    text.board_list = data[1]
                    Data.jugada = int(data[2][2])
                    Data.pressed = False
                    Data.white_t = (True if data[2][0] == "True" else False)
                    Data.reverse = (True if data[2][1] == "True" else False)
                    Data.check = (True if data[2][3] == "True" else False)
                    Data.check_mate = (True if data[2][4] == "True" else False)
                    Data.wk_moved = (True if data[2][5] == "True" else False)
                    Data.bk_moved = (True if data[2][6] == "True" else False)
                    Data.castling = []
                    Data.text_data = data[0]
                    
                    peces.position = text.board_list[Data.jugada]
                    peces.draw(Data.reverse)

            elif Data.catch_button.id == 11:
                text.board_list = []
                text.board_list.append(chess_notations.FEN_decode("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))
                Data.jugada = 0
                Data.pressed = False
                Data.white_t = True
                Data.reverse = False
                Data.check = False
                Data.check_mate = False
                Data.wk_moved = False
                Data.bk_moved = False
                Data.castling = []
                Data.text_data = []
                
                peces.position = text.board_list[Data.jugada]
                peces.draw(Data.reverse)
            
            elif Data.catch_button.id == 13:
                path = os.path.abspath(os.path.dirname(__file__))
                os.system(f'start {os.path.realpath(path)}')

            elif Data.catch_button.id == 14:
                webbrowser.open('https://github.com/AlfonsoXIII/chess_manager')

            Data.catch_button = None

'''
Funció que implementa els canvis en pantalla per a les peces en accionar 
una d'elles.
'''
def Move(x, event, Data, size, peces, text, taulell, sideMenu):
    target = ([a for a in range(1, 9) if (size*a)+int(161.828*Data.proportion)+Data.board_pos_y > event.pos[1]][0]-1, 
            [a for a in range(1, 9) if (size*a)+int(40.457*Data.proportion)+Data.relative_center > event.pos[0]][0]-1)

    if x.rect.collidepoint(event.pos[0]-Data.relative_center, event.pos[1]-Data.board_pos_y):
        peces.mp = []
        taulell.selected = ()
        Data.pressed = False
    
    elif x.id == "P" and (target[0] == 7 or target[0] == 0):
        sideMenu.Add(scripts.side_Menu.promotion_menu(sideMenu.screen, Data.proportion))
        sideMenu.content[-1].Build()
        sideMenu.content[-1].pos = target
        sideMenu.content[-1].pos_or = x.pos
        sideMenu.menus_active["Promotion"] = True
        sideMenu.Switch(len(sideMenu.content)-1)
        Data.freeze = True
        
        if Data.side_menu_on == False:
            Data.side_menu_on = True
            side_MenuWindow(Data, Data.side_menu_on)


    elif target in peces.mp:
        compr = (True if peces.position[target[0]][target[1]] != "" else False)
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
        temp = []

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
                                                            
        Data.text_data.append((chess_notations.algebraic_de(peces.position[target[0]][target[1]], 
                                                            (target if Data.reverse == False else (7-target[0], 7-target[1])),
                                                            compr,
                                                            (x.pos if Data.reverse == False else (7-x.pos[0], 7-x.pos[1])),
                                                            (str("{} ").format((str(int(Data.jugada/2)+1)+".") if Data.jugada%2 == 0 else "")),
                                                            check,
                                                            Data.check_mate,
                                                            local_castling), (temp if Data.reverse == False or temp == [] else (7-temp[0], 7-temp[1]))))

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
        if x.rect.collidepoint(event.pos[0]-Data.relative_center, event.pos[1]-Data.board_pos_y) and peces.position[x.pos[0]][x.pos[1]].isupper() == Data.white_t:
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
                    return x