'''
Classe per a la implementació d'una estructura
de dades tipus arbre "maxmin".
'''
class Tree_Node():
    def __init__(self, data, position, pre_position):
        #Dades del Node
        self.data = data
        self.board = position
        self.pre_board = pre_position
        self.evaluation = 0

        self.childs = [] #Nodes inferiors annexos