import random
import os

moves = [["r", "p", "s"], ["p", "s", "r"], ["s", "r", "p"]]


def game(playerMove):
    cpuMove = random.choice(moves)

    print("... \n")
    print("... \n")
    print("... \n")

    print(playerMove, " against ", cpuMove[0], "\n")

    if playerMove == cpuMove[1]:
        print("You have won!!!")
    elif playerMove == cpuMove[2]:
        print("You have lose :-(")
    else:
        print("You have draw, let's try again")
        return False

    return True


while True:

    playerMove = input("Chose your move (Write r, p or s): ").lower()
    Game = game(playerMove)

    if playerMove in moves[0] and Game:
        anotherGame = input(
            "\n Do you want to play another game? (y or n) ").lower()

        if anotherGame == "y":
            os.system("clear")
            pass
        else:
            break
    elif playerMove in moves[0] and not Game:
        pass
    else:
        print("Please enter an acceptable value \n")
