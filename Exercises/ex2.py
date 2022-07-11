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


items = readFile("input.txt")
fixedItems = []

for i in range(len(items)):
    if items[i] != "cioccolata":
        fixedItems.append(items[i])

writeFile("output.txt", fixedItems)
