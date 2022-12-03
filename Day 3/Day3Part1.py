priority = 0
total_priority = 0

def determinePriority(letter):
    if letter.isupper():
        return (ord(letter)-38)
    else:
        return (ord(letter)-96)

with open('input.txt') as f:
    for line in f:
        firstpart, secondpart = line.strip()[:len(line)//2], line.strip()[len(line)//2:]
        print(firstpart, secondpart)
        list1 = list(firstpart)
        list2 = list(secondpart)
        priority = determinePriority(list(set(list1).intersection(list2))[0])
        total_priority = total_priority + priority
        print(str(priority) + " - " + str(total_priority))
