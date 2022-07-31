# Assignment: Create a script which, starting from two input files, makes an output file with all the lines in common between the two files.
# In the output file, the lines have to be reversed compared to order they had in the first input file.

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


firstFile = readFile("./data/file_03_1.txt")
secondFile = readFile("./data/file_03_2.txt")

mergedFile = []

for line in firstFile:
    if line in secondFile:
        mergedFile.append(line)

writeFile("./data/file_03_3.txt", mergedFile[::-1])
