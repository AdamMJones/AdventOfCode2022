stack1=[]
stack2=[]
stack3=[]
stack4=[]
stack5=[]
stack6=[]
stack7=[]
stack8=[]
stack9=[]

def printStack():
    print(" ")
    print(stack1)
    print(stack2)
    print(stack3)
    print(stack4)
    print(stack5)
    print(stack6)
    print(stack7)
    print(stack8)
    print(stack9)
    print(" ")

def addToStack(line):
    if line[1] != " ":
        stack1.append(line[1])
    if line[5] != " ":
        stack2.append(line[5])
    if line[9] != " ":
        stack3.append(line[9])
    if line[13] != " ":
        stack4.append(line[13])
    if line[17] != " ":
        stack5.append(line[17])
    if line[21] != " ":
        stack6.append(line[21])
    if line[25] != " ":
        stack7.append(line[25])
    if line[29] != " ":
        stack8.append(line[29])
    if line[33] != " ":
        stack9.append(line[33])

def getCrates(fromStack, numberToMove):
    crates=[]
    print(numberToMove)
    for i in range(0, int(numberToMove)):
        if fromStack == 1:
            crates.append(stack1[-1])
            stack1.pop()
        elif fromStack == 2:
            crates.append(stack2[-1])
            stack2.pop()
        elif fromStack == 3:
            crates.append(stack3[-1])
            stack3.pop()
        elif fromStack == 4:
            crates.append(stack4[-1])
            stack4.pop()
        elif fromStack == 5:
            crates.append(stack5[-1])
            stack5.pop()
        elif fromStack == 6:
            crates.append(stack6[-1])
            stack6.pop()
        elif fromStack == 7:
            crates.append(stack7[-1])
            stack7.pop()
        elif fromStack == 8:
            crates.append(stack8[-1])
            stack8.pop()
        elif fromStack == 9:
            crates.append(stack9[-1])
            stack9.pop()

    return crates

def moveCrates(toStack, cratesToMove):
    cratesToMove.reverse()
    print(cratesToMove)
    for crateToMove in cratesToMove:
        if toStack == 1:
            stack1.append(crateToMove)
        elif toStack == 2:
            stack2.append(crateToMove)
        elif toStack == 3:
            stack3.append(crateToMove)
        elif toStack == 4:
            stack4.append(crateToMove)
        elif toStack == 5:
            stack5.append(crateToMove)
        elif toStack == 6:
            stack6.append(crateToMove)
        elif toStack == 7:
            stack7.append(crateToMove)
        elif toStack == 8:
            stack8.append(crateToMove)
        elif toStack == 9:
            stack9.append(crateToMove)

def moveStacks(numberToMove, fromStack, toStack):
    printStack()
    cratesToMove = getCrates(int(fromStack), int(numberToMove))
    print("Moving " + ' '.join(cratesToMove) + " from " + fromStack + " to " + toStack)
    moveCrates(int(toStack), cratesToMove)

with open('input.txt') as f:
    for line in f:
        if line[0] == "[":
            addToStack(line)
        elif line.isspace():
            stack1.reverse()
            stack2.reverse()
            stack3.reverse()
            stack4.reverse()
            stack5.reverse()
            stack6.reverse()
            stack7.reverse()
            stack8.reverse()
            stack9.reverse()
            printStack()
        elif line.strip()[0:4] == "move":
            numberToMove = str(line).split(' ')[1].strip()
            fromStack = str(line).split(' ')[3].strip()
            toStack = str(line).split(' ')[5].strip()
            print("We're going to move " + str(numberToMove) + " crates from " + str(fromStack) + " to " + str(toStack))
            moveStacks(numberToMove, fromStack, toStack)

print(stack1[-1]+stack2[-1]+stack3[-1]+stack4[-1]+stack5[-1]+stack6[-1]+stack7[-1]+stack8[-1]+stack9[-1])