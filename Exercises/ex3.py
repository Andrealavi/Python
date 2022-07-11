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


numbers = readFile("input.txt")
fixedNumbers = []

for i in range(len(numbers)):
    fixedNumbers.append(numbers[i]*2)

writeFile("output.txt", fixedNumbers)
