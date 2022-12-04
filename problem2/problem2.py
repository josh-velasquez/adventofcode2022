import os

def partTwo():
    try:
        file = open(os.getcwd() + "\problem2\problem1.txt")
        lines = file.readlines()

        score = 0

        for line in lines:
            opponent, outcome = line.strip().split(" ")

            # print("OP: " + opponent + " user: " + user)
            
            if (opponent == "A"): # rock
                if (outcome == "X"): # lose (scissor)
                    score += (0 + 3)
                elif (outcome == "Y"): # draw (rock)
                    score += (3 + 1)
                elif (outcome == "Z"): # win (paper)
                    score += (6 + 2)
            elif (opponent == "B"): # paper
                if (outcome == "X"): # lose (rock)
                    score += (0 + 1)
                elif (outcome == "Y"): # draw (paper)
                    score += (3 + 2)
                elif ( outcome == "Z"): # win (scissor)
                    score += (6 + 3)
            elif (opponent == "C"): # scissor
                if (outcome == "X"): # lose (paper)
                    score += (0 + 2)
                elif (outcome == "Y"): # draw (scissor)
                    score += (3 + 3)
                elif (outcome == "Z"): # win (rock)
                    score += (6 + 1)

        print("Score: " + str(score))

    except Exception as e:
        print("Error: " + e)

def partOne():
    try:
        file = open(os.getcwd() + "\problem2\problem1.txt")
        lines = file.readlines()

        score = 0

        for line in lines:
            opponent, user = line.strip().split(" ")

            # print("opponent: " + opponent + " user: " + user)

            if (user == "X"): # user rock
                score += 1
                if (opponent == "A"): # opponent rock
                    score += 3
                elif (opponent == "C"): # opponent scissor
                    score += 6
            elif (user == "Y"): # user paper
                score += 2
                if (opponent == "A"): # opponent rock
                    score += 6
                elif (opponent == "B"): # opponent paper
                    score += 3
            elif (user == "Z"): # user scissors
                score += 3
                if (opponent == "B"): # opponent paper
                    score += 6
                elif (opponent == "C"): # opponent scissor
                    score += 3

        print("Score: " + str(score))

    except Exception as e:
        print("Error: " + e)


def main():
    # partOne()
    partTwo()


main()