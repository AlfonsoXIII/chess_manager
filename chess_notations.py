def algebraic_de(piece, pos, capture, pos_or, number, check, check_mate, castling):  
    unicode = {"P": u'\u2659', "p": u'\u265F', "K": u'\u2654', "k": u'\u265A', "Q": u'\u2655', "q":u'\u265B', "N":u'\u2658', "n":u'\u265E', "B":u'\u2657', "b":u'\u265D', "R":u'\u2656', "r":u'\u265C'}
    ab = "abcdefgh"

    #return unicode[piece]+"e4" if piece.upper() != "P" else "e4"
    return str(number+"0-0" if castling[0] == True else number+"0-0-0" if castling[1] == True else number+(unicode[piece.upper()] if piece.upper() != "P" else ab[pos_or[1]] if capture == True else "")+("x" if capture == True else "")+ab[pos[1]]+str(8-pos[0])+("+" if check == True else "")+("#" if check_mate == True else ""))
    #return str(number+"0-0" if castling[0] == True else number+"0-0-0" if castling[1] == True else number+(piece.upper() if piece.upper() != "P" else ab[pos_or[1]] if capture == True else "")+("x" if capture == True else "")+ab[pos[1]]+str(8-pos[0])+("+" if check == True else "")+("#" if check_mate == True else ""))

def FEN_encode(board):
    data = ""
    counter = 0
    
    for x in board:
        for y in x:
            if y != "":
                if counter != 0:
                    data += str(counter)
                    counter = 0
                data += str(y)
            else:
                counter += 1

        if counter != 0:
            data += str(counter)
        
        counter = 0
        if board.index(x) != 7:
            data += "/"
    
    return data

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

def generate_file(Data, board_list, move_list, path):
    file = open(path+".ccmm", "w", encoding="utf-8-sig")
    boards = ""
    moves = ""

    for x in board_list:
        if board_list.index(x) != len(board_list)-1:
            boards += FEN_encode(x)+","
        
        else:
            boards += FEN_encode(x)
    
    if len(move_list) != 0:
        for x in move_list:
            if move_list.index(x) != len(move_list)-1:
                moves += str(str(x[0])+","+(" , " if x[1] == [] else str(str(x[1][0])+","+str(x[1][1])))+";")
            
            else:
                moves += str(str(x[0])+","+(" , " if x[1] == [] else str(str(x[1][0])+","+str(x[1][1]))))
    
    else:
        moves = None

    file.write(str(moves)+"\n")
    file.write(str(boards)+"\n")
    file.write(str(Data.white_t)+","+str(Data.reverse)+","+str(Data.jugada)+","+str(Data.check)+","+str(Data.check_mate)+","+str(Data.wk_moved)+","+str(Data.bk_moved))

def charge_file(file_path):
    file = open(file_path, "r", encoding="utf-8-sig")
    lines = file.readlines()

    m1 = []
    m2 = []

    if lines[0] != "None\n":
        for x in lines[0].split(";"):
            temp = x.split(",")
            m1.append([str(temp[0]), ([] if temp[1] == " " else (int(temp[1]), int(temp[2])))])
    
    for x in lines[1].split(","):
        m2.append(FEN_decode(str(x).replace("\n", "")))

    return [m1, m2, lines[2].split(",")]