import os

def partOne():
    try:
        file = open(os.getcwd() + "\problem1\problem1.txt", "r")
        lines = file.readlines()

        highestTotalCalories = 0
        currentTotalCalories = 0
        for line in lines:
            val = line.strip()
            if (val.isdigit()):
                currentTotalCalories += int(val)
            else:
                if (currentTotalCalories > highestTotalCalories):
                    highestTotalCalories = currentTotalCalories
                currentTotalCalories = 0
        if (currentTotalCalories > highestTotalCalories):
            highestTotalCalories = currentTotalCalories

        print("Highest Total Calories: " + str(highestTotalCalories))
    except Exception as e:
        print("Invalid file." + str(e))


def partTwo():
    try:
        file = open(os.getcwd() + "\problem1\problem1.txt", "r")
        lines = file.readlines()

        topOne = 0
        topTwo = 0
        topThree = 0
        currentTotalCalories = 0
        for line in lines:
            val = line.strip()
            if (val.isdigit()):
                currentTotalCalories += int(val)
            else:
                if (currentTotalCalories > topOne):
                    topOne = currentTotalCalories
                elif (currentTotalCalories > topTwo):
                    topTwo = currentTotalCalories
                elif (currentTotalCalories > topThree):
                    topThree = currentTotalCalories
                currentTotalCalories = 0
        if (currentTotalCalories > topOne):
            topOne = currentTotalCalories
        elif (currentTotalCalories > topTwo):
            topTwo = currentTotalCalories
        elif (currentTotalCalories > topThree):
            topThree = currentTotalCalories
        total = topOne + topTwo + topThree
        print("Highest Total Calories: " + str(total))
    except Exception as e:
        print("Invalid file." + str(e))


def main():
    # partOne()
    partTwo()

main()