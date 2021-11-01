import multiprocessing
from math import inf
import time


def test1(a, b):
    time.sleep(a)
    print(a, b)

def test2(a, b):
    time.sleep(100)
    print("uwu")

def test3(a, b):
    time.sleep(3)
    b.put(str(a))

    return a

def main():

    p1 = multiprocessing.Process(target=test2, args=[1, 2])
    p2 = multiprocessing.Process(target=test3, args=[1])
    
    p2.start()

    print("5")