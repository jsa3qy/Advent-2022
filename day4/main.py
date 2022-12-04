from timeit import default_timer as timer

lines = [line.strip() for line in open("input.txt")]

def part_1():
    start = timer()
    count = 0
    for line in lines:
        val = [[int(num) for num in pair.split("-")] for pair in line.split(",")]
        if (val[0][0] <= val[1][0] and val[0][1] >= val[1][1]) or (val[0][0] >= val[1][0] and val[0][1] <= val[1][1]):
            count += 1
    return count, timer() - start

def part_2():
    start = timer()
    count = 0
    for line in lines:
        val = [[int(num) for num in pair.split("-")] for pair in line.split(",")]
        if (val[0][0] <= val[1][0] and val[0][1] >= val[1][0]) or (val[0][0] >= val[1][0] and val[0][0] <= val[1][1]):
            count += 1
    return count, timer() - start
    
# first attempt below

def get_pair(val):
    val = val.split(",")
    one = [int(thing) for thing in val[0].split("-")]
    two = [int(thing) for thing in val[1].split("-")]
    return [set([char for char in range(one[0],one[1] + 1)]),set([char for char in range(two[0],two[1] + 1)])]

def part_1_old():
    start = timer()
    count = 0
    for line in lines:
        val = get_pair(line)
        val[0].intersection(val[1])
        if val[0].issubset(val[1]) or val[1].issubset(val[0]):
            count += 1
    return count, timer() - start

def part_2_old():
    start = timer()
    count = 0
    for line in lines:
        ranges = get_pair(line)
        if len(ranges[0].intersection(ranges[1])) > 0:
            count += 1
    return count, timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))
