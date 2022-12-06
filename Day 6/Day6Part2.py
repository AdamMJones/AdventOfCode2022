stack=[]
count=0

with open('input.txt') as f:
    for line in f:
        for character in line:
            count=count+1
            print("The character is " + character + " and the characters are " + ' '.join(stack))
            stack=[]
            mySet=[]
            stack=(line[count-1],line[count],line[count+1],line[count+2],line[count+3],line[count+4],line[count+5],line[count+6],line[count+7],line[count+8],line[count+9],line[count+10],line[count+11],line[count+12])
            mySet = set(stack)
            print(str(len(stack)) + "  " + str(len(mySet)))
            if len(stack) == len(mySet):
                print("The position is " + str(count+13) + " and the characters are " + ' '.join(stack))
                break