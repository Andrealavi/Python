# Assignment: Create a script which, starting from an input file with two lines of number (e.g 1,2,3).
# The two lines have to become two list of three values. At the end, the script has to realize an output file
# in which there'll be a matrix. The matrix will have as diagonal the sum of lists' values and in all the other position a '0'.

# e.g

# Input File:

# 1,2,3
# 4,5,6

# Output File:

# 5 0 0
# 0 7 0
# 0 0 9
#
#

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


def stringToNumberParser(fileContent):
    numbersList = []
    parsedList = []

    for line in fileContent:
        for char in line:
            if char != ',':
                numbersList.append(int(char))
        parsedList.append(numbersList)
        numbersList = []
    return parsedList


def createMatrix(list):
    matrix = []

    firstRow = "{} 0 0".format((list[0][0] + list[1][0]))
    secondRow = "0 {} 0".format((list[0][1] + list[1][1]))
    thirdRow = "0 0 {}".format((list[0][2] + list[1][2]))

    matrix.append(firstRow)
    matrix.append(secondRow)
    matrix.append(thirdRow)

    return matrix


fileContent = readFile('./data/file_04_1.txt')

matrixContent = stringToNumberParser(fileContent)

matrix = createMatrix(matrixContent)

writeFile("./data/file_04_2.txt", matrix)
