from timeit import default_timer as timer
import string

lines = [line.strip() for line in open("input.txt")]

def sum_up(vals):
    sumv = 0
    for val in vals:
        if val.isupper():
            sumv += ord(val.lower()) + 26 - 96
        else:
            sumv += ord(val) - 96
    return sumv

def part_1():
    start = timer()
    saved = []
    for line in lines:
        part1 = [char for char in line[0:int(len(line)/2)]]
        part2 = [char for char in line[int(len(line)/2):]]
        saved.append(list(set(part1).intersection(set(part2)))[0])
    return sum_up(saved), timer() - start

def part_2():
    start = timer()
    saved = []
    ind = 0
    while ind < len(lines):
        one = set([char for char in lines[ind]])
        two = set([char for char in lines[ind + 1]])
        three = set([char for char in lines[ind + 2]])
        saved.append(list(one.intersection(two, three))[0])
        ind += 3
    return sum_up(list(saved)), timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))