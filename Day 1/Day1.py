import numpy as np #pip3 install numpy

elf_number = 0
total = 0
max_total = 0
greedy_elf = 0
arr = []

with open('input.txt') as f:
    for line in f:
        if line and not line.isspace():
            total = total + int(line)
            if total > max_total:
                max_total = total
                greedy_elf = elf_number
        else:
            arr.append(total)
            print("Elf number " + str(elf_number) + " holds " + str(total) + " calories.")
            elf_number = elf_number + 1
            total = 0

arr.sort(reverse=True)

print("")
print("The 1st Elf holds " + str(arr[0]) + " calories.")
print("The 2nd Elf holds " + str(arr[1]) + " calories.")
print("The 3rd Elf holds " + str(arr[2]) + " calories.")
print("")
print("The total of the top 3 Elves is " + str(int(arr[0]) + int(arr[1]) + int(arr[2])) + " calories.")