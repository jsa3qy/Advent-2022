from timeit import default_timer as timer

lines = [[int(val) for val in line.strip()] for line in open("input.txt")]

def check_place(i,j,grid):
    cur_val = grid[j][i]
    visible_count = 4
    for x in range(i):
        if grid[j][x] >= cur_val:
            visible_count -= 1
            break
    if visible_count == 4:
        return True
    for x in range(i+1,len(grid[0])):
        if grid[j][x] >= cur_val:
            visible_count -= 1
            break
    if visible_count == 3:
        return True
    for y in range(j):
        if grid[y][i] >= cur_val:
            visible_count -= 1
            break
    if visible_count == 2:
        return True
    for y in range(j+1,len(grid)):
        if grid[y][i] >= cur_val:
            visible_count -= 1
            break
    if visible_count == 1:
        return True
    return False
            

def part_1():
    start = timer()
    count = 2*len(lines)+2*len(lines[0]) - 4
    for j in range(1,len(lines) - 1):
        for i in range(1,len(lines[0]) - 1):
            if check_place(i,j,lines):
                count += 1
    return count, timer() - start

def score(i,j,grid):
    cur_val = grid[j][i]
    score = 1
    # left
    view_count_x = 1
    for x in range(i):
        pos_x = i - 1 - x
        if grid[j][pos_x] < cur_val:
            view_count_x += 1
        else:
            break
        if x == i - 1:
            view_count_x -= 1
    score*=view_count_x
    view_count_x = 1
    for x in range(i+1,len(lines[0])):
        if grid[j][x] < cur_val:
            view_count_x += 1
        else:
            break
        if x == len(lines[0]) - 1:
            view_count_x -= 1
    score*=view_count_x
    view_count_y = 1
    for y in range(j):
        pos_y = j - 1 - y
        if grid[pos_y][i] < cur_val:
            view_count_y += 1
        else:
            break
        if y == j - 1:
            view_count_y -= 1
    score*=view_count_y
    view_count_y = 1
    for y in range(j+1,len(lines)):
        if grid[y][i] < cur_val:
            view_count_y += 1
        else:
            break
        if y == len(lines) - 1:
            view_count_y -= 1
    score*=view_count_y
    return score

def part_2():
    start = timer()
    max_val = 0
    for j in range(1,len(lines) - 1):
        for i in range(1,len(lines[0]) - 1):
            cur_score = score(i,j,lines)
            if cur_score > max_val:
                max_val = cur_score
    return max_val, timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))