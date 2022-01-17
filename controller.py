import Configuration, gameMove, Util

pos1 = 0
pos2 = 0
player1 = []
player2 = []
ladders = {}
snakes = {}
boardSize = 0
totalBoardSize = 0
print('Do you want customize the settings then press Y and for default settings type N')
gameSetting = input()
if (gameSetting == 'Y' or gameSetting == 'y'):
    print('Do you want customize the board then press Y and for default board type N')
    boardSetting = input()
    if (boardSetting == 'Y' or boardSetting == 'y'):
        config = Configuration.CustomBoard()
        print('Enter your board Size')
        boardSize = config.customBoardSize()
        totalBoardSize = boardSize * boardSize
    else:
        print('you have choosed default settings for board')
        config = Configuration.CustomBoard()
        boardSize = config.defaultBoardSize()
        totalBoardSize = boardSize * boardSize
    print('Do you want customize the ladders then press Y and for default board type N')
    laddersSetting = input()
    if (laddersSetting == 'Y' or boardSetting == 'y'):
        print('Enter count of ladders')
        totalLadders = Util.integerInput()
        config = Configuration.CustomLadder()
        ladders = config.customLadderPostion(totalLadders, boardSize)
    else:
        print('you have choosed default settings for ladders')
        config = Configuration.CustomLadder()
        ladders = config.defaultPostionLadder()
    print('Do you want customize the snakes then press Y and for default board type N')
    snakesSetting = input()
    if (snakesSetting == 'Y' or snakesSetting == 'y'):
        print('Enter count of snakes')
        totalsnakes = Util.integerInput()
        config = Configuration.CustomSnake()
        snakes = config.customSnakePostion(totalsnakes, boardSize)
    else:
        print('you have choosed default settings for snake')
        config = Configuration.CustomSnake
        snakes = config.defaultPostionSnake()
else:
    print('you have choosed default settings for game')
    boardConfig = Configuration.Board()
    boardSize = boardConfig.defaultBoardSize()
    snakeConfig = Configuration.Snake()
    snakes = snakeConfig.defaultPostionSnake()
    ladderConfig = Configuration.Ladder()
    ladders = ladderConfig.defaultPostionLadder()
    totalBoardSize = boardSize * boardSize
print('now game starts')
moves = gameMove.Move()
while True:
    A = input("Press enter to throw dice for player 1:")
    pos1 = moves.move(pos1, ladders, snakes)
    player1.append(pos1)
    if (pos1 >= totalBoardSize):
        print("player 1 wins")
        break
    B = input("Press enter to throw dice for player 2:")
    pos2 = moves.move(pos2, ladders, snakes)
    player2.append(pos2)
    if (pos2 >= totalBoardSize):
        print("player 2 wins")
        break

if (len(player1) > len(player2)):
    player2.append(0)
elif (len(player1) < len(player2)):
    player1.append(0)
movesPlayer1 = Util.convertIntoNumpyArray(player1)
movesPlayer2 = Util.convertIntoNumpyArray(player2)
print(f"player1 all movements:{movesPlayer1}")
print(f"player2 all movements:{movesPlayer2}")
print('Do you want to plot the graph b/w player1 and player2 movements on board then press Y for yes and N for no')
graphPlot = input()
if (graphPlot == 'Y' or graphPlot == 'y'):
    Util.plotGraph(movesPlayer1, movesPlayer2)
else:
    print('Game Over !!!!!!!!!!!!!!!')
