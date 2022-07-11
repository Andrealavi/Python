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

fixedNumbers.append(int(numbers[0]))

for i in range(1, len(numbers)):
    fixedNumbers.append(int(numbers[i])*int(numbers[i-1]))

writeFile("output.txt", fixedNumbers)
