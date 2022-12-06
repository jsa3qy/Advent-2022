from timeit import default_timer as timer

from cv2 import line
import re
import numpy as np
import csv

# reader = csv.reader(open("stacks.txt"), delimiter=" ")
# cols = list(zip(*reader))[:-1]
# columns = {}
# for i,col in enumerate(cols):
#     columns[str(i + 1)] = [char for char in list(col[1:]) if len(char) > 0]

moves = [[char.strip() for i,char in enumerate(line.split(" ")) if i % 2 == 1] for line in open("input.txt")]

def part_1():
    columns = {
        "1" : ["M","J","C","B","F","R","L","H"],
        "2" : ["Z","C","D"],
        "3" : ["H","J","F","C","N","G","W"],
        "4" : ["P","J","D","M","T","S","B"],
        "5" : ["N","C","D","R","J"],
        "6" : ["W","L","D","Q","P","J","G","Z"],
        "7" : ["P","Z","T","F","R","H"],
        "8" : ["L","V","M","G"],
        "9" : ["C","B","G","P","F","Q","R","J"]
    }
    start = timer()
    for move in moves:
        for _ in range(int(move[0])):
            columns[move[2]].append(columns[move[1]].pop())
    answer = ""
    for key in columns:
        answer += columns[key].pop()
    return answer, timer() - start

def part_2():
    columns = {
        "1" : ["M","J","C","B","F","R","L","H"],
        "2" : ["Z","C","D"],
        "3" : ["H","J","F","C","N","G","W"],
        "4" : ["P","J","D","M","T","S","B"],
        "5" : ["N","C","D","R","J"],
        "6" : ["W","L","D","Q","P","J","G","Z"],
        "7" : ["P","Z","T","F","R","H"],
        "8" : ["L","V","M","G"],
        "9" : ["C","B","G","P","F","Q","R","J"]
    }
    start = timer()
    for move in moves:
        vals = []
        for _ in range(int(move[0])):
            vals.append(columns[move[1]].pop())
        vals.reverse()
        columns[move[2]] += vals
    answer = ""
    for key in columns:
        answer += columns[key].pop()
    return answer, timer() - start

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))
