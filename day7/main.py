from timeit import default_timer as timer

lines = [line.strip() for line in open("input.txt")]
summm = 0
needed = 0
answer = 0

def part_1():
    start = timer()
    dir_to_inners = {}
    cur_path = [""]
    i = 0
    while i < len(lines):
        cmd = lines[i]
        if "cd /" in cmd:
            cur_path = [""]
        elif ".." in cmd:
            cur_path.pop()
        elif "cd" in cmd:
            cur_path.append(cmd.split(" ")[2])
        elif "ls" in cmd:
            inners = []
            for ind,cmd2 in enumerate(lines[i+1:]):
                if "$" in cmd2:
                    break
                if "dir" in cmd2:
                    inners.append(cmd2.split(" ")[1])
                else:
                    inners.append(cmd2.split(" ")[0])
            dir_to_inners["/".join(cur_path)] = inners
            i += ind
        i+=1
    get_sum_inners("",dir_to_inners)
                
    return summm, timer() - start

def get_sum_inners(start, dir_to_inners):
    global summm
    sum = 0
    for val in dir_to_inners[start]:
        if val.isdigit():
            sum += int(val)
        else:
            sum += get_sum_inners("/".join([start,val]), dir_to_inners)
    if sum <= 100000:
        summm+=sum
    return sum

def get_sum_inners_2(start, dir_to_inners):
    global answer
    sum = 0
    for val in dir_to_inners[start]:
        if val.isdigit():
            sum += int(val)
        else:
            sum += get_sum_inners_2("/".join([start,val]), dir_to_inners)
    if sum >= needed and (sum < answer or answer == 0):
        answer = sum
    return sum

def part_2():
    global needed, answer
    start = timer()
    dir_to_inners = {}
    cur_path = [""]
    i = 0
    while i < len(lines):
        cmd = lines[i]
        if "cd /" in cmd:
            cur_path = [""]
        elif ".." in cmd:
            cur_path.pop()
        elif "cd" in cmd:
            cur_path.append(cmd.split(" ")[2])
        elif "ls" in cmd:
            inners = []
            for ind,cmd2 in enumerate(lines[i+1:]):
                if "$" in cmd2:
                    break
                if "dir" in cmd2:
                    inners.append(cmd2.split(" ")[1])
                else:
                    inners.append(cmd2.split(" ")[0])
            dir_to_inners["/".join(cur_path)] = inners
            i += ind
        i+=1
    total = get_sum_inners("",dir_to_inners)
    needed = -1 * (70000000 - int(total) - 30000000)
    
    get_sum_inners_2("", dir_to_inners)
    
    return answer, timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))