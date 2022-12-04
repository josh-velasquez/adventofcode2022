import os

LOWERCASE_OFFSET = 96
UPPERCASE_OFFSET = 38

def getLetterValue(letter):
    if (letter.isupper()):
        return int(ord(letter)) - UPPERCASE_OFFSET
    elif (letter.islower()):
        return int(ord(letter)) - LOWERCASE_OFFSET

def getSharedLetter(first, second):
    for letter in first:
        if (letter in second):
            return letter

def getSharedLetters(words):
    if (words == ""):
        return
    first, second, third = words.strip().split(" ")
    for letter in first:
        if (letter in second and letter in third):
            return letter

def partTwo():
    try:
        file = open(os.getcwd() + "\problem3\problem3.txt")
        lines = file.readlines()

        totalSum = 0
        counter = 1
        grouping = ""
        for line in lines:
            grouping = line.strip() + " " + grouping
            if (counter % 3 == 0):
                sharedLetter = getSharedLetters(grouping)
                totalSum += getLetterValue(sharedLetter)
                grouping = ""
            counter += 1
        print("Total Sum: " + str(totalSum))

    except Exception as e:
        print("Error: " +  str(e))

def partOne():
    try:
        file = open(os.getcwd() + "\problem3\sample.txt")
        lines = file.readlines()

        totalSum = 0
        for line in lines:
            first = line[:len(line)//2]
            second = line[len(line)//2:len(line)]
            sharedLetter = getSharedLetter(first, second)
            letterValue = getLetterValue(sharedLetter)
            print("SHARED: " + str(sharedLetter) + " VAL: " + str(letterValue))
            totalSum += letterValue

        print("Total Sum: " + str(totalSum))


    except Exception as e:
        print("Error: " +  str(e))


def main():
    # partOne()
    partTwo()


main()