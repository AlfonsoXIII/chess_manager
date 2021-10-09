#Scripts importats
import movements as mvs
import tree_dataStructure as tree

#Mòduls importats
from copy import deepcopy

'''
Funció encarregada de evaluar una posició en concret
tot retornant un valor numèric el qual pot ser:
    
    Dom f: R
'''
def Evaluate_Position(node):
    board_value = 0
    pre_board_value = 0

    chess_value = {"P":1, "N":2, "B":3, "R":5, "Q":9, "K":900, "p":-1, "n":-2, "b":-3, "r":-5, "q":-9, "k":-900}

    for row in node.board:
        for square in row:
            if square != "":
                board_value += chess_value[square]
    
    for row in node.pre_board:
        for square in row:
            if square != "":
                pre_board_value += chess_value[square]
    
    return board_value

'''
Funció encarregada de calcular les jugades possibles per a
una posició i afegir-les a l'arbre de jugades.
'''
def Add_Depth(node):
    #temp_board = deepcopy(node.board)
    #temp_board[node.data[0][0]][node.data[0][1]] = ""

    for a in range(0, 8):
        for b in range(0, 8):
            if node.board[b][a].upper() == "P":
                temp = mvs.Pawn(node.board, (0 if node.board[b][a].isupper() else 1), (b, a))

                for x in temp:
                    temp_board = deepcopy(node.board)
                    temp_board[x[0]][x[1]] = node.board[b][a]
                    temp_board[b][a] = ""

                    node.childs.append(tree.Tree_Node([(b, a), x], temp_board, node.board))
                    #print("tinker patroll")

'''
Funció principal encarregada d'implementar i coordinar tot
el sistema d'anàlisis i retornar una llista ordenada amb
les principales jugades, i les seves linies concretes.
'''
def Main(board):
    tree_root = []

    for a in range(0, 8):
        for b in range(0, 8):
            temp = []

            if board[b][a].upper() == "P":
                temp = mvs.Pawn(board, (0 if board[b][a].isupper() else 1), (b, a))
            
            elif board[b][a].upper() == "N":
                temp = mvs.Knight(board, (b, a))

            for x in temp:
                temp_board = deepcopy(board)
                temp_board[x[0]][x[1]] = board[b][a]
                temp_board[b][a] = ""

                tree_root.append(tree.Tree_Node([(b, a), x], temp_board, board))
            
            #if board[b][a].upper() == "K":
                #movements[(b, a)] = mvs.King(board, (0 if board[b][a].isupper() else 1), (b, a))


    for node in tree_root:
        Add_Depth(node)
        #print(node.childs)
        #if Evaluate_Position(node) != 0:
                #print(Evaluate_Position(node))
    
        for nodex in node.childs:
            Add_Depth(nodex)
            #if Evaluate_Position(nodex) != 0:
                    #print(Evaluate_Position(nodex))
            #print(nodex.childs)

            for nodexx in nodex.childs:
                if Evaluate_Position(nodexx) != 0:
                    print(Evaluate_Position(nodexx))
                    #print(nodexx.board)
    
    return tree_root

'''
print(Main([["", "k", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["p", "", "", "", "", "", "", ""],
            ["", "p", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "P"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "P", ""],
            ["", "", "", "", "", "", "K", ""]]))
'''

print(Main([["", "k", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "p", "", "n", "", "", "", ""],
            ["", "", "", "", "", "N", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "P", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "K", ""]]))