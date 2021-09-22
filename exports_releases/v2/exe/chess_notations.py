def algebraic_de(piece, pos, capture, pos_or, number):  
    #unicode = {"P": u'\u2659', "p": u'\u265F', "K": u'\u2654', "k": u'\u265A', "Q": u'\u2655', "q":u'\u265B', "N":u'\u2658', "n":u'\u265E', "B":u'\u2657', "b":u'\u265D', "R":u'\u2656', "r":u'\u265C'}
    ab = "abcdefgh"

    #return unicode[piece]+"e4" if piece.upper() != "P" else "e4"
    return str(number+(piece.upper() if piece.upper() != "P" else ab[pos_or[1]] if capture == True else "")+("x" if capture == True else "")+ab[pos[1]]+str(8-pos[0]))

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
            
            #print(k, " ", str(FEN[x])[y])

    return array


