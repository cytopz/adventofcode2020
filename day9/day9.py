#!/usr/bin/env python3

inpt = [int(x.strip()) for x in open('input', 'r')]

def find_set(idx, inv):
    sum = 0
    res = []
    for i in range(idx, -1, -1):
        sum += inpt[i]
        res.append(inpt[i])
        if sum == inv:
            return res

def part1():
    for i, j in zip(range(len(inpt)-24), range(25, len(inpt)+1)):
        pre = inpt[i:j]
        if (inpt[j]-min(pre)) < min(pre):
            return j

def part2():
    inv_idx = part1()
    inv = inpt[inv_idx]
    for i in range(inv_idx, -1, -1):
        if inpt[i] < inv:
            res = find_set(i, inv)
            if res:
                return min(res) + max(res) 

print(inpt[part1()])
print(part2())
