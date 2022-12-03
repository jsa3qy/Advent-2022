from timeit import default_timer as timer

input = [line.strip() for line in open("input.txt")]

def part_1():
    start = timer()
    i = 0
    sums = [0]
    for index,line in enumerate(input):
        if line == "":
            sums.append(0)
            i+=1
        else:
            sums[i] += int(line)
    return max(sums), timer() - start

def part_2():
    start = timer()
    i = 0
    sums = [0]
    for index,line in enumerate(input):
        if line == "":
            sums.append(0)
            i+=1
        else:
            sums[i] += int(line)
    sums = sorted(sums)
    return sum(sums[len(sums) - 3:]), timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))