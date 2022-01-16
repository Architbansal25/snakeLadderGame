import Util


class Snake:
    def __init__(self):
        pass

    def defaultPostionSnake(self):
        snakes = {25: 5, 49: 14}
        return snakes


class Board:
    def __init__(self):
        pass

    def defaultBoardSize(self):
        boardSize = 7
        return boardSize


class Ladder:
    def __init__(self):
        pass

    def defaultPostionLadder(self):
        ladders = {3: 22, 8: 30}
        return ladders


class CustomSnake(Snake):
    def __init__(self):
        pass

    def customSnakePostion(self, totalSnakes, boardSize):
        snakes = {}
        totalboardSize = boardSize * boardSize
        for i in range(totalSnakes):
            print('enter snake head')
            snake_head = Util.integerInput()
            print('enter snake tail')
            snake_tail = Util.integerInput()
            if (snake_head > totalboardSize - 1 or snake_tail > totalboardSize - 1):
                print('you have entered max size snake head and tail than board -----Please enter again')
                print('enter snake head')
                snake_head = Util.integerInput()
                print('enter snake tail')
                snake_tail = Util.integerInput()
            elif (snake_head < boardSize):
                print('you have entered snake head and tail at first place on board -----Please enter again')
                print('enter snake head')
                snake_head = Util.integerInput()
                print('enter snake tail')
                snake_tail = Util.integerInput()
            elif (snake_head < snake_tail or snake_head == snake_tail):
                print('you have entered wrong snake head and tail -----Please enter again')
                print('enter snake head')
                snake_head = Util.integerInput()
                print('enter snake tail')
                snake_tail = Util.integerInput()

            snakes[snake_head] = snake_tail
        return snakes


class CustomLadder(Ladder):

    def __init__(self):
        pass

    def customLadderPostion(self, totalLadders, boardSize):
        ladders = {}
        totalboardSize = boardSize * boardSize
        for i in range(totalLadders):
            print('enter ladder bottom')
            ladder_tail = Util.integerInput()
            print('enter ladder top')
            ladder_head = Util.integerInput()
            if (ladder_head > totalboardSize - 1 or ladder_tail > totalboardSize - 1):
                print('you have entered max size of ladder head and tail than board -----Please enter again')
                print('enter ladder bottom')
                ladder_tail = Util.integerInput()
                print('enter ladder top')
                ladder_head = Util.integerInput()
            elif (ladder_head < ladder_tail or ladder_head == ladder_tail):
                print('you have entered wrong ladder head and tail -----Please enter again')
                print('enter ladder bottom')
                ladder_tail = Util.integerInput()
                print('enter ladder top')
                ladder_head = Util.integerInput()

            ladders[ladder_tail] = ladder_head
        return ladders


class CustomBoard(Board):
    def __init__(self):
        pass

    def customBoardSize(self):
        boardSize = Util.integerInput()
        return boardSize
