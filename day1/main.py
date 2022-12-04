from timeit import default_timer as timer

input = [line.strip() for line in open("input.txt")]

def part_1():
    start = timer()
    return max([sum([int(num) for num in char.split("\n")]) for char in open('input.txt', 'r').read().split("\n\n")]), timer() - start

def part_2():
    start = timer()
    return sum(sorted([sum([int(num) for num in char.split("\n")]) for char in open('input.txt', 'r').read().split("\n\n")])[-3:]), timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))