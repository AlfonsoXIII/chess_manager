import movements as mvs

def Evaluate_Position(board, piece_pos, move):
    pass

def Main(board):
    movements = {}

    for a in range(0, 8):
        for b in range(0, 8):
            if board[b][a].upper() == "P":
                movements[(b, a)] = mvs.Pawn(board, (0 if board[b][a].isupper() else 1), (b, a))
    
    return movements


print(Main([["", "k", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["p", "", "", "", "", "", "", ""],
            ["", "p", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "P"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "P", ""],
            ["", "", "", "", "", "", "K", ""]]))