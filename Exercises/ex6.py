def readFile(filename):
    file = open(filename)
    fileContent = file.readlines()

    for i in range(0, len(fileContent)):
        fileContent[i] = fileContent[i].replace("\n", "")

    file.close()

    return fileContent


def writeFile(filename, fileContent):
    file = open(filename, "w")

    for line in fileContent:
        file.write(str(line) + "\n")

    file.close()


words = readFile("input.txt")
fixedWords = []

for i in range(len(words)):
    if len(words[i]) > 5:
        fixedWords.append(words[i])

writeFile("output.txt", fixedWords)
