import os

def getLettersFromRow(line):
    newLetters = []
    for i in range(len(line)):
        if (line[i] == '' or line[i] == ' '):
            newLetters.append(None)
        else:
            # can have multiple letters
            letters = line[i].strip().split()
            for char in letters:
                newLetters.append(char[1])
    return newLetters


def processMoves(crates, move):
    splitMoves = move.split(" ")
    numBox = int(splitMoves[1])
    start = int(splitMoves[3]) - 1
    end = int(splitMoves[5]) - 1

    movedLetters = []
    letterCounter = 0
    for i in range(len(crates)):
        if (numBox != letterCounter and crates[i][start] != None):
            letterToAppend = crates[i][start]
            movedLetters.append(letterToAppend)
            crates[i][start] = None
            letterCounter += 1

    # put the letters that is moved
    for j in range((len(crates) - 1), -1, -1):
        if ((crates[j][end] == None) and (len(movedLetters) != 0)):
            crates[j][end] = movedLetters.pop(0)
    return crates

def partOne():
    try:
        file = open(os.getcwd() + "/problem5/problem5.txt")
        lines = file.readlines()
        crates = []
        movesList = []
        doneReadingCrates = False
        maxCrateHeight = 0
        for line in lines:
            if (line != "\n" and (not doneReadingCrates)):
                if (not line.strip().replace(" ", "").isnumeric()):
                    lettersList = getLettersFromRow(line.strip("\n").split("   "))
                    letterRow = []
                    
                    for i in range(len(lettersList)):
                        if (lettersList[i] != None):
                            letterRow.append(lettersList[i])
                            maxCrateHeight += 1
                        else:
                            letterRow.append(None)
                    crates.append(letterRow)
                else:
                    doneReadingCrates = True
            else:
                movesList.append(line.strip())
        
        # crates = [
        #     [None, 'D', None],
        #     ['N', 'C', None],
        #     ['Z', 'M', 'P']
        # ]

        crates = [
            ['V', None, None, 'T', None, None, 'J', None, None],
            ['Q', None, None, 'M', 'P', None, 'Q', None, 'J'],
            ['W', 'B', None, 'N', 'Q', None, 'C', None, 'T'],
            ['M', 'C', None, 'F', 'N', None, 'G', 'W', 'G'],
            ['B', 'W', 'J', 'H', 'L', None, 'R', 'B', 'C'],
            ['N', 'R', 'R', 'W', 'W', 'W', 'D', 'N', 'F'],
            ['Z', 'Z', 'Q', 'S', 'F', 'P', 'B', 'Q', 'L'],
            ['C', 'H', 'F', 'Z', 'G', 'L', 'V', 'Z', 'H']]

        # add extra rows (if all crates are stacked together)
        originalCratesHeight = len(crates)
        rowCount = len(crates[0])
        if (len(crates) != maxCrateHeight):
            for i in range(maxCrateHeight - originalCratesHeight):
                crates.insert(i, [None]*(rowCount))
        
        # process moves list
        for move in movesList:
            if (move != ""):
                crates = processMoves(crates, move)


        # clean up crates (shave off none rows)
        rowsToRemove = 0
        for letterRow in crates:
            if letterRow.count(None) == len(letterRow):
                rowsToRemove += 1
                
        # remove excess rows
        del crates[:rowsToRemove]
        
        
        print(crates[len(crates) - 1])


        # ['M', 'N', 'Z', 'T', 'B', 'B', 'V', 'H', 'P']
        # ['C', 'H', 'F', 'Z', 'G', 'L', 'V', 'Z', 'H']

    except Exception as e:
        print("Error: " +  str(e))



def main():
    partOne()


main()