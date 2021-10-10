#Scripts importats
import movements as mvs
import tree_dataStructure as tree

#Mòduls importats
from copy import deepcopy
import time

'''
Funció encarregada de evaluar una posició en concret
tot retornant un valor numèric el qual pot ser:
    
    Dom f: R
'''
def Evaluate_Position(node):
    board_value = 0

    chess_value = {"P":1, "N":2, "B":3, "R":5, "Q":9, "K":900, "p":-1, "n":-2, "b":-3, "r":-5, "q":-9, "k":-900}

    for row in node.board:
        for square in row:
            if square != "":
                board_value += chess_value[square]
    
    return board_value

'''
Funció encarregada de processar l'arbre de jugades i ordenar-les
en un diccionari de millors a pitjors amb el resultat de la seva 
evaluació adjunt i la millor linia possible.
'''
def Process_Tree(tree, colour):
    moves = {}
    
    #Funció privada per a analitzar l'arbre al complet utilitzant recursivitat
    def Tree_Childs(node):
        ##### NODE AMB CONTINUACIÓ ######
        if len(node.childs) != 0:
            catch_val = 1000
            for child in node.childs:
                value = Tree_Childs(child)

                if value < catch_val:
                    catch_val = value
            
            return catch_val

        ##### NODE FINAL #####
        else:
            return Evaluate_Position(node)

    for root_node in tree:
        absTime = time.time()
        value = Tree_Childs(root_node)

        moves[str(str(root_node.data[0])+"-"+str(root_node.data[1]))] = value

        print(time.time()-absTime)
    
    ##### ORDRE DEL DICCIONARI DE MANERA CREIXENT #####    
    sorted_moves = sorted(moves.items(), key=lambda x: x[1], reverse=colour)

    moves = {}
    for x in sorted_moves:
        moves[x[0]] = x[1]
    
    return moves

'''
Funció encarregada de calcular les jugades possibles per a
una posició i afegir-les a l'arbre de jugades.
'''
def Add_Depth(node, colour):
    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if node.board[b][a].upper() == "P" and node.board[b][a].isupper() == colour:
                temp = mvs.Pawn(node.board, (0 if node.board[b][a].isupper() else 1), (b, a))
            
            elif node.board[b][a].upper() == "N" and node.board[b][a].isupper() == colour:
                temp = mvs.Knight(node.board, (b, a))

            elif node.board[b][a].upper() == "R" and node.board[b][a].isupper() == colour:
                temp = mvs.Rock(node.board, (b, a))
            
            elif node.board[b][a].upper() == "B" and node.board[b][a].isupper() == colour:
                temp = mvs.Bishop(node.board, (b, a))
            
            elif node.board[b][a].upper() == "Q" and node.board[b][a].isupper() == colour:
                temp = mvs.Queen(node.board, (b, a))
            
            elif node.board[b][a].upper() == "K" and node.board[b][a].isupper() == colour:
                temp = mvs.King(node.board, (0 if node.board[b][a].isupper() else 1), (b, a))

            for x in temp:
                temp_board = deepcopy(node.board)
                temp_board[x[0]][x[1]] = deepcopy(node.board[b][a])
                temp_board[b][a] = ""

                same_king = ()
                other_king = ()

                for c in range(0, 8):
                    for d in range(0, 8):
                        if temp_board[x[0]][x[1]].upper() != "K":
                            if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() == colour:
                                same_king = (d, c)
                        
                        else:
                            same_king = x
                        
                        if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() != colour:
                            other_king = (d, c)


                if mvs.King_Check(temp_board, same_king) and (mvs.King_Check(node.board, other_king) or (mvs.King_Check(node.board, other_king) == False and mvs.King_Check(temp_board, other_king))):
                    node.childs.append(tree.Tree_Node([(b, a), x], temp_board, node.board))
                
                    if mvs.King_Check(temp_board, other_king) == False:



'''
Funció principal encarregada d'implementar i coordinar tot
el sistema d'anàlisis i retornar una llista ordenada amb
les principales jugades, i les seves linies concretes.
'''
def Main(board, depth, colour):
    absTime = time.time()
    print("Depth: ", str(depth))
    tree_root = []

    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if board[b][a].upper() == "P" and board[b][a].isupper() == colour:
                temp = mvs.Pawn(board, (0 if board[b][a].isupper() else 1), (b, a))
            
            elif board[b][a].upper() == "N" and board[b][a].isupper() == colour:
                temp = mvs.Knight(board, (b, a))

            elif board[b][a].upper() == "R" and board[b][a].isupper() == colour:
                temp = mvs.Rock(board, (b, a))
            
            elif board[b][a].upper() == "B" and board[b][a].isupper() == colour:
                temp = mvs.Bishop(board, (b, a))
            
            elif board[b][a].upper() == "Q" and board[b][a].isupper() == colour:
                temp = mvs.Queen(board, (b, a))
            
            elif board[b][a].upper() == "K" and board[b][a].isupper() == colour:
                temp = mvs.King(board, (0 if board[b][a].isupper() else 1), (b, a))
            
            #print(temp)

            for x in temp:
                temp_board = deepcopy(board)
                temp_board[x[0]][x[1]] = deepcopy(board[b][a])
                temp_board[b][a] = ""

                #if temp_board[x[0]][x[1]].upper() == "K":
                    #castling = [] 
                    #movimientos = x.Movement(peces.position)
                    #if_castling = x.Castling(text.board_list[-1], (Data.wk_moved if x.colour == 0 else Data.bk_moved))
                    #if if_castling[0]: 
                    #    Data.castling.append((x.pos[0], x.pos[1]+(2*(1 if Data.reverse == False else -1))))
                    #    movimientos.append((x.pos[0], x.pos[1]+(2*(1 if Data.reverse == False else -1))))
                    #else: Data.castling.append((0, 0))
                    #if if_castling[1]: 
                    #    Data.castling.append((x.pos[0], x.pos[1]+(-2*(1 if Data.reverse == False else -1))))
                    #    movimientos.append((x.pos[0], x.pos[1]+(-2*(1 if Data.reverse == False else -1))))
                    #else: Data.castling.append((0, 0))
                    
                #else:   movimientos = x.Movement(peces.position)

                same_king = ()
                other_king = ()

                for c in range(0, 8):
                    for d in range(0, 8):
                        if temp_board[x[0]][x[1]].upper() != "K":
                            if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() == colour:
                                same_king = (d, c)
                        
                        else:
                            same_king = x
                        
                        if temp_board[d][c].upper() == "K" and temp_board[d][c].isupper() != colour:
                            other_king = (d, c)

                if mvs.King_Check(temp_board, same_king) and (mvs.King_Check(temp_board, other_king) or (mvs.King_Check(temp_board, other_king) == False and mvs.King_Check(board, other_king))):
                    tree_root.append(tree.Tree_Node([(b, a), x], temp_board, board))                    


    for node in tree_root:
        absTime = time.time()
        #print(node.data)
        Add_Depth(node, False)

        #for nodex in node.childs:
            #Add_Depth(nodex, True)

            #for nodexx in nodex.childs:
                #Add_Depth(nodexx, False)
        
        print(time.time()-absTime)
    print("######################################################")
    
    return Process_Tree(tree_root, colour)

'''
print(Main([["", "k", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "P", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "P", ""],
            ["", "", "", "", "", "", "K", ""]]))
'''

print(Main([["", "k", "", "", "", "", "", ""],
            ["", "p", "", "", "n", "", "p", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "Q", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "R", "", "", "", "", "P"],
            ["", "", "", "", "", "P", "", "K"],
            ["", "", "", "", "", "", "", ""]], 
            4, 
            True))