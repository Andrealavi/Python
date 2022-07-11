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
    if int(numbers[i]) > 5 and int(numbers[i]) < 10:
        fixedNumbers.append(int(numbers[i]))

writeFile("output.txt", fixedNumbers)
