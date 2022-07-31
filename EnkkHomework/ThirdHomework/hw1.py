# Assignment: Create a script which takes a series of words or punctuation symbols (only . , ! ?) from the user.
# The input has to stop when the user writes the word 'stop'.
# At the end of the insertion, the script has to print the sentence/sentences written by the user, making sure that all the punctuation is correct.
# After this, the script has to make some statistics about the text:
#     - number of words (without punctuation)
#     - number of punctuation symbols
#     - number of sentences
#     - most frequent character
#     - less frequent character

def getChar(text):
    chars = []

    for sentence in text:
        for char in sentence:
            if char != ' ':
                chars.append(char.lower())

    return chars


def getMostFrequentElement(list):
    mostFrequentElementCount = list.count(list[0])
    mostFrequentElementIndex = 0

    for i in range(1, len(list)):
        if list.count(list[i]) > mostFrequentElementCount:
            mostFrequentElementCount = list.count(list[i])
            mostFrequentElementIndex = i

    return list[mostFrequentElementIndex]


def getLeastFrequentElement(list):
    leastFrequentElementCount = list.count(list[0])
    leastFrequentElementIndex = 0

    for i in range(1, len(list)):
        if list.count(list[i]) < leastFrequentElementCount:
            leastFrequentElementCount = list.count(list[i])
            leastFrequentElementIndex = i

    return list[leastFrequentElementIndex]


print("Let's begin with the input \n\n\n")

word = input('Digit the word: ')

sentence = ''

text = []
words = []
punctuation = []

while(word != 'stop'):
    if word in ('.', '!', '?'):
        sentence = sentence + word
        text.append(sentence)
        sentence = ''
        punctuation.append(word)
    elif word == ',':
        sentence = sentence + word
    else:
        if sentence == '':
            sentence = word.capitalize()
        else:
            sentence = sentence + " " + word
        words.append(word)

    word = input('Digit the word: ')

for sentence in text:
    print("\n\n\n{}".format(sentence))

print("\n\n\nLet's make some statistics \n\n")
print("Number of words: ", len(words))
print("Number of punctuation: ", len(punctuation))
print("Number of sentences: ", len(text))
print("Most frequent character: ", getMostFrequentElement(getChar(text)))
print("Least frequent character: ", getLeastFrequentElement(getChar(text)))
