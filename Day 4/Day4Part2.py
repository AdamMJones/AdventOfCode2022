priority = 0
total_priority = 0
counter = 0
line1 = ""
line2 = ""
line3 = ""

def determinePriority(letter):
    if letter.isupper():
        return (ord(letter)-38)
    else:
        return (ord(letter)-96)

with open('input.txt') as f:
    for line in f:
        counter = counter + 1
        if counter == 1:
            line1 = line.strip()
        elif counter == 2:
            line2 = line.strip()
        elif counter == 3:
            line3 = line.strip()
            priority = determinePriority(list(set(line1).intersection(line2).intersection(line3))[0])
            total_priority = total_priority + priority
            print(str(counter) + " " + str(total_priority))
            print(line1 + " " + line2 + " " + line3)
            counter = 0

