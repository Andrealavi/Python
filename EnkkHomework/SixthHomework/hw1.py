# Assignment: Create a quiz game in which the user have to choose from two artist the one who published more albums.
# The data will be obtained from the deezer api (https://api.deezer.com/artist/:id) and the id of the artists will be got from ./data/authors.json file.
# After the game, the user can choose whether to play another game or not, by clicking letter Y.

import json
import random
import requests

with open('./data/authors.json', 'r') as f:
    authors = json.load(f)
    authorsName = [author for author in authors]


def answerChecker(firstAnswer, secondAnswer, userAnswer):
    firstAnswerAlbums = requests.get(
        "https://api.deezer.com/artist/{}".format(authors[firstAnswer])).json()['nb_album']
    secondAnswerAlbums = requests.get(
        "https://api.deezer.com/artist/{}".format(authors[firstAnswer])).json()['nb_album']

    if (userAnswer == 1 and firstAnswerAlbums > secondAnswerAlbums) or (userAnswer == 2 and firstAnswerAlbums < secondAnswerAlbums):
        print("You have won =)\n\n")
    else:
        print("I'm sorry but you have lost :-( \n\n")


def quiz():
    try:

        firstAnswer = authorsName[random.randint(0, len(authorsName) - 1)]
        secondAnswer = authorsName[random.randint(0, len(authorsName) - 1)]

        while (firstAnswer == secondAnswer):
            firstAnswer = authorsName[random.randint(0, len(authorsName) - 1)]
            secondAnswer = authorsName[random.randint(0, len(authorsName) - 1)]

        userAnswer = int(input('Which is the artist who has published more albums {} (1) or {} (2)? \n'.format(
            firstAnswer, secondAnswer)))

        if userAnswer not in (1, 2):
            raise Exception(
                "You have inserted neither 1 nor 2. Please try again (you'll lose your actual quiz)")

        answerChecker(firstAnswer, secondAnswer, userAnswer)

        anotherGame = input(
            "You can play another time if you want. Just press Y: ").upper()

        if anotherGame == "Y":
            quiz()

    except ValueError as error:
        print("You haven't inserted a number, please try again\n")
        quiz()
    except Exception as error:
        print(error, "\n")
        quiz()


quiz()
