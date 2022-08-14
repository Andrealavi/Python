# Assignment: Create a quiz game in which the user have to choose from two artist the one who has more fans.
# The data will be obtained from the deezer api (https://api.deezer.com/artist/:id) and the id of the artists will be got from ./data/authors.json file.
# The user has to be able to add other artist to ./data/authors.json file. In order to do this, deezer api (https://api.deezer.com/search/artist?q=:ArtistName) will be used to search for the artist using his name.
# After the game, the user can choose whether to play another game or not, by clicking letter Y.

import json
import random
import requests


def answerChecker(authors, firstAnswer, secondAnswer, userAnswer):
    firstAnswerFans = requests.get(
        "https://api.deezer.com/artist/{}".format(authors[firstAnswer])).json()['nb_fan']
    secondAnswerFans = requests.get(
        "https://api.deezer.com/artist/{}".format(authors[secondAnswer])).json()['nb_fan']

    if (userAnswer == 1 and firstAnswerFans > secondAnswerFans) or (userAnswer == 2 and firstAnswerFans < secondAnswerFans):
        print("You have won =)\n\n")
    else:
        print("I'm sorry but you have lost :-( \n\n")


def addArtists():

    try:
        artistName = input('Insert the name of the artist you want to add: ')

        url = "https://api.deezer.com/search/artist?q={}".format(artistName)

        artist = requests.get(url).json()['data'][0]

        with open('./data/authors.json', 'r') as f:
            authors = json.load(f)

            if artist['name'] in [author for author in authors]:
                raise Exception(
                    "The Artist you're trying to add is already present in our quiz. Try again with another artist.\n\n")

        with open('./data/authors.json', 'w') as f:
            authors[artist['name']] = artist['id']
            json.dump(authors, f, indent=4)

    except Exception as error:
        print(error)
        choice = input(
            'If you want to add another artist, press Y otherwise any other key on the keyboard: ').upper()
        if choice == 'Y':
            addArtists()


def quiz():
    try:

        with open('./data/authors.json', 'r') as f:
            authors = json.load(f)
            authorsName = [author for author in authors]

        firstAnswer = authorsName[random.randint(0, len(authorsName) - 1)]
        secondAnswer = authorsName[random.randint(0, len(authorsName) - 1)]

        while (firstAnswer == secondAnswer):
            firstAnswer = authorsName[random.randint(0, len(authorsName) - 1)]
            secondAnswer = authorsName[random.randint(0, len(authorsName) - 1)]

        userAnswer = int(input('Which is the artist who has more fans {} (1) or {} (2)? \n'.format(
            firstAnswer, secondAnswer)))

        if userAnswer not in (1, 2):
            raise Exception(
                "You have inserted neither 1 nor 2. Please try again (you'll lose your actual quiz)")

        answerChecker(authors, firstAnswer, secondAnswer, userAnswer)

        anotherGame = input(
            "You can play another time if you want. Just press Y otherwise any other key on your keyboard: ").upper()

        if anotherGame == "Y":
            quiz()

    except ValueError as error:
        print("You haven't inserted a number, please try again\n")
        quiz()
    except Exception as error:
        print(error, "\n")
        quiz()


try:
    print('If you want, you can add other artists to the quiz')
    choice = input(
        'Write Y to add another artist, N to start the game without other artists: ').upper()

    if choice == 'Y':
        addArtists()
    elif choice == 'N':
        print("Allright let's start the quiz")
    else:
        raise Exception(
            "You haven't inserted a valid answer. You won't be able to add other artists to the quiz.")
except Exception as error:
    print(error)

quiz()
