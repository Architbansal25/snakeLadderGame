import Util

class Move:
    def __init__(self):
        pass

    def move(self, pos, ladder, snake):
        dice = Util.getDice()
        print(f"Dice:{dice}")
        pos = pos + dice

        if pos in ladder:
            print("player took the ladder")
            pos = ladder[pos]
            print(f"postion:{pos}")
        elif pos in snake:
            print("player bite by snake")
            pos = snake[pos]
            print(f"postion:{pos}")

        else:
            print(f"postion:{pos}")
        print("\n")
        return pos
