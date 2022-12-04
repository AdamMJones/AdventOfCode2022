total_count = 0
first_start = int
first_end = int
second_start = int
second_end = int

with open('input.txt') as f:
    for line in f:
        firstpart, secondpart = str(line).strip().split(',')
        first_start, first_end = str(firstpart).strip().split('-')
        second_start, second_end = str(secondpart).strip().split('-')

        first_start = int(first_start)
        first_end = int(first_end)
        second_start = int(second_start)
        second_end = int(second_end)

        if (first_start <= second_start and first_end >= second_end) or \
           (second_start <= first_start and second_end >= first_end) or \
           (second_start <= first_end and second_end >= first_end) or \
           (first_start <= second_end and first_end >= second_end):
            total_count = total_count + 1
            print(line + str(total_count))
