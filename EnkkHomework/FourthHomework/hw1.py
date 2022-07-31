# Assignment: Create a script which prints out the fourth row of a file.

def readFile(filename):
    file = open(filename)
    fileContent = file.readlines()

    for i in range(0, len(fileContent)):
        fileContent[i] = fileContent[i].replace("\n", "")

    file.close()

    return fileContent


print(readFile('./data/file_01.txt')[3])
