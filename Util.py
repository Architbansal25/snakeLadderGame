import random
import numpy as np
import matplotlib.pyplot as plt


def getDice():
    dice = random.randint(1, 6)
    return dice


def convertIntoNumpyArray(moveList):
    array = np.array(moveList)
    return array


def integerInput():
    try:
        n = int(input())
        return n
    except:
        print('type an integer')
        return integerInput()

def plotGraph(player1, player2):
    # print(player1,player2,sep='\n')
    font = {'family': 'serif', 'color': 'darkred', 'size': 13}
    plt.plot(player1, player2, color="blue")
    plt.xlabel("moves of player 1", fontdict=font)
    plt.ylabel("moves of player 2", fontdict=font)
    plt.show()
# plotGraph()
