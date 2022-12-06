stack=[]
count=0

with open('input.txt') as f:
    for line in f:
        for character in line:
            count=count+1
            print("The character is " + character + " and the characters are " + ' '.join(stack))
            stack=[]
            mySet=[]
            stack=(line[count-1],line[count],line[count+1],line[count+2])
            mySet = set(stack)
            print(str(len(stack)) + "  " + str(len(mySet)))
            if len(stack) == len(mySet):
                print("The position is " + str(count+3) + " and the characters are " + ' '.join(stack))
                break