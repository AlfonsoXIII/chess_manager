import json

#Generació de un string amb la jugada en notació algebraica i caràcters unicode
def algebraic_de(piece, pos, capture, pos_or, number, check, check_mate, castling):  
    unicode = {"P": u'\u2659', "p": u'\u265F', "K": u'\u2654', "k": u'\u265A', "Q": u'\u2655', "q":u'\u265B', "N":u'\u2658', "n":u'\u265E', "B":u'\u2657', "b":u'\u265D', "R":u'\u2656', "r":u'\u265C'}
    ab = "abcdefgh"

    return str(number+"0-0" if castling[0] == True else number+"0-0-0" if castling[1] == True else number+(unicode[piece.upper()] if piece.upper() != "P" else ab[pos_or[1]] if capture == True else "")+("x" if capture == True else "")+ab[pos[1]]+str(8-pos[0])+("+" if check == True else "")+("#" if check_mate == True else ""))

#Transformació d'un string amb estructura FEN a un array 2d Python
def FEN_decode(FEN):
    FEN = FEN.split("/")

    array = [["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]]

    for x in range (0, 8):
        k = 0
        corrector = 0
        for y in range (0, len(str(FEN[x]))):
            
            if str(FEN[x])[y].isalpha() == True: 
                array[x][y+k-corrector] = str(FEN[x])[y]
            
            else:
                k += int(str(FEN[x])[y])
                corrector += 1

    return array

#Funció per a generar un arxiu JSON amb les dades d'una posició
def generate_file(Data, board_list, move_list, path):

    data = {}
    data["Data"] = [Data.white_t, Data.reverse, Data.jugada, Data.page, Data.check, Data.check_mate, Data.wk_moved, Data.bk_moved]
    data["board_list"] = board_list
    data["move_list"] = move_list

    with open(path+".json", 'w+') as file:
        json.dump(data, file)

#Funció per a carregar les dades d'un arxius JSON en un diccionari python
def charge_file(file_path):

    with open(file_path, "r") as file:
        data = json.load(file)

    return data