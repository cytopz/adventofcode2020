#!/usr/bin/env python3

from collections import defaultdict

inpt = [int(x.strip()) for x in open('input', 'r')]

def part1():
    inpt.append(0)
    li = sorted(inpt)
    d = d1 = 0
    d3 = 1
    for i, j in zip(range(len(li)-1), range(1, len(li))):
        d = li[j] - li[i]
        if d == 1: d1 += 1
        elif d == 3: d3 += 1
    return d1 * d3

def part2():
    d = defaultdict(int)
    li = sorted(inpt)
    d[0] = 1
    for j in li:
        d[j] += d[j - 1] + d[j - 2] + d[j - 3]
    return d[li[-1:][0]]
print(part1())
print(part2())
