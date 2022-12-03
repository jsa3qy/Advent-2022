from timeit import default_timer as timer

input = [line.strip() for line in open("input.txt")]

map_xyz = {0:"Z",1:"X",2:"Y",3:"Z",4:"X"} # rock paper scissors
xyz_map = {"X":1,"Y":2,"Z":3}

def get_choice(abc,xyz):
    if abc == "A":
        return map_xyz[xyz_map[xyz] - 1]
    if abc == "B":
        return xyz
    if abc == "C":
        return map_xyz[xyz_map[xyz] + 1]

def winner(abc,xyz):
    if abc == "A":
        if xyz == "X":
            return xyz_map[xyz] + 3
        if xyz == "Y":
            return xyz_map[xyz] + 6
        if xyz == "Z":
            return xyz_map[xyz]
    if abc == "B":
        if xyz == "X":
            return xyz_map[xyz]
        if xyz == "Y":
            return xyz_map[xyz] + 3
        if xyz == "Z":
            return xyz_map[xyz] + 6
    if abc == "C":
        if xyz == "X":
            return xyz_map[xyz] + 6
        if xyz == "Y":
            return xyz_map[xyz]
        if xyz == "Z":
            return xyz_map[xyz] + 3

def part_1():
    start = timer()
    score = 0
    for line in input:
        score += winner(line[0],line[2])
    return score, timer() - start

def part_2():
    start = timer()
    score = 0
    for line in input:
        score += winner(line[0],get_choice(line[0],line[2]))
    return score, timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))