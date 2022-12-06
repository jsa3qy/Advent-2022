from timeit import default_timer as timer

input = [line.strip() for line in open("input.txt")][0]

def part_1():
    start = timer()
    i = 0
    while True:
        if len(set([char for char in input[i:i+4]])) == 4:
            return i+4, timer() - start
        i += 1

def part_2():
    start = timer()
    i = 0
    while True:
        if len(set([char for char in input[i:i+14]])) == 14:
            return i+14, timer() - start
        i += 1

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))