import multiprocessing

def main(board):
    apa = ai.max_value

    p1 = multiprocessing.Process(target=apa, args=[board, -inf, +inf, False, 1])
    p1.start()
    value = p1.get()
    p1.join()

    return value

if __name__ == "__main__":
    print("uwu")
    value = main(board)