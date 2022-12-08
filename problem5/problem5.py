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
    # print("BEFORE")
    # print(crates)
    movedLetters = []
    # grab the letters to move
    letterCounter = 0
    for i in range(len(crates)):
        if (numBox != letterCounter and crates[i][start] != None):
            letterToAppend = crates[i][start]
            movedLetters.append(letterToAppend)
            crates[i][start] = None
            letterCounter += 1
    # print(movedLetters)

    # put the letters that is moved
    # movedLetters = ['D', 'N', 'Z']
    # crates =
    # [[None, None, None], 
    #  [None, None, None], 
    #  [None, None, None], 
    #  [None, None, None], 
    #  [None, 'C', None], 
    #  [None, 'M', 'P']]
    print("BEFORE")
    print(crates)
    for j in range((len(crates) - 1), -1, -1):
        # print("J: " + str(j) + " LEN: " + str(len(movedLetters)))
        if ((crates[j][end] == None) and (len(movedLetters) != 0)):
            crates[j][end] = movedLetters.pop(0)
    print("AFTER")
    print(crates)
    # crates =
    # [[None, None, 'Z'], 
    #  [None, None, 'Z'], 
    #  [None, None, 'Z'], 
    #  [None, None, 'N'], 
    #  [None, 'C', 'D'], 
    #  [None, 'M', 'P']]

    # print("AFTER")
    # print(crates)

    return crates

def partOne():
    try:
        file = open(os.getcwd() + "/problem5/sample.txt")
        lines = file.readlines()
        crates = [] # sample dimension
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
        
        # add extra rows (if all crates are stacked together)
        if (len(crates) != maxCrateHeight):
            noneList = [None]*(len(crates[0]))
            originalCratesHeight = len(crates)
            for i in range(maxCrateHeight - originalCratesHeight):
                crates.insert(i, noneList)
        
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
        # print(crates)
    except Exception as e:
        print("Error: " +  str(e))



def main():
    partOne()


main()