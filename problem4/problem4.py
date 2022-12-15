import os

def partTwo():
    try:
        file = open(os.getcwd() + "\problem4\sample.txt")
        lines = file.readlines()

        containedCounter = 0
        for line in lines:
            first, second = line.strip().split(",")
            firstStart, firstEnd = first.split("-")
            secondStart, secondEnd = second.split("-")

            if (int(firstStart) <= int(secondStart)):
                if (int(firstEnd) >= int(secondEnd) or int(firstEnd) <= int(secondStart)):
                    if (int(firstEnd) <= int(secondEnd) or int(secondEnd) <= int(firstEnd)):
                        containedCounter += 1

            elif (int(secondStart) <= int(firstStart)):
                if (int(secondEnd) >= int(firstEnd) or int(secondStart) <= int(firstEnd)):
                    if (int(secondEnd) <= int(firstEnd) or int(firstEnd) <= int(secondEnd)):
                        containedCounter += 1

        print("TOTAL: " + str(containedCounter))

    except Exception as e:
        print("Error: " +  str(e))


def partOne():
    try:
        file = open(os.getcwd() + "\problem4\problem4.txt")
        lines = file.readlines()

        containedCounter = 0
        for line in lines:
            first, second = line.strip().split(",")
            firstStart, firstEnd = first.split("-")
            secondStart, secondEnd = second.split("-")

            if (int(firstStart) <= int(secondStart) and int(firstEnd) >= int(secondEnd)):
                containedCounter += 1
            elif (int(secondStart) <= int(firstStart) and int(secondEnd) >= int(firstEnd)):
                containedCounter += 1

        print("TOTAL: " + str(containedCounter))

    except Exception as e:
        print("Error: " +  str(e))


def main():
    # partOne()
    partTwo()


main()