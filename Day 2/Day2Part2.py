opposition = " "
outcome = " "
responseScore = 0
gameScore = 0
roundScore = 0
totalScore = 0

def determineShape(code):
    if code == "A" or code == "X":
        return "Rock"
    if code == "B" or code == "Y":
        return "Paper"
    if code == "C" or code == "Z":
        return "Scissors"

def determineCode(shape):
    if shape == "Rock":
        return "X"
    elif shape == "Paper":
        return "Y"
    elif shape == "Scissors":
        return "Z"

def determineOutcome(outcome):
    if outcome == "X":
        return "Loss"
    elif outcome == "Y":
        return "Draw"
    elif outcome == "Z":
        return "Win"

def determineResponseScore(response):
    if response == "Rock":
        return 1
    elif response == "Paper":
        return 2
    elif response == "Scissors":
        return 3

def determineGameScore(opposition, response):
    if determineShape(opposition) == determineShape(response):
        return 3
    elif determineShape(opposition) == "Rock" and determineShape(response) == "Scissors":
        return 0
    elif determineShape(opposition) == "Scissors" and determineShape(response) == "Paper":
        return 0
    elif determineShape(opposition) == "Paper" and determineShape(response) == "Rock":
        return 0
    else:
        return 6

def determineResponseShape(opposition, outcome):
    if outcome == "Win":
        if opposition == "Rock":
            return "Y"
        elif opposition == "Paper":
            return "Z"
        elif opposition == "Scissors":
            return "X"
    elif outcome == "Loss":
        if opposition == "Rock":
            return "Z"
        elif opposition == "Paper":
            return "X"
        elif opposition == "Scissors":
            return "Y"
    elif outcome == "Draw":
        return determineCode(opposition)

with open('input.txt') as f:
    for line in f:
        opposition = str(line).split(' ')[0]
        outcome = str(line).split(' ')[1].strip()

        responseShape = determineResponseShape(determineShape(opposition), determineOutcome(outcome))
        gameScore = determineGameScore(opposition, responseShape)
        responseScore = determineResponseScore(determineShape(responseShape))
        roundScore = gameScore + responseScore
        totalScore = totalScore + roundScore

        print(" ")
        print("Opposition played " + determineShape(opposition) + ". You should play " + determineShape(responseShape) + ".")
        print("This shape will score you " + str(responseScore) + ".")
        print("This game will score you " + str(gameScore) + ".")
        print("Total score for this round is " + str(roundScore))
        print("Total score is " + str(totalScore))