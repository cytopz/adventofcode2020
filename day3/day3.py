#!/usr/bin/env python3

from functools import reduce

inpt = [x.strip('\n') for x in open('input', 'r')]

def part1(sx, sy):
    i = j = trees = 0
    while i < len(inpt):
        if inpt[i][j] == '#':
            trees += 1
        i += sy
        j = (j + sx) % len(inpt[0])
    return trees

def part2():
    slopes = [
       (1, 1),
       (3, 1),
       (5, 1),
       (7, 1),
       (1, 2),
    ]
    return reduce(lambda a, b: a * b, [part1(*x) for x in slopes])

print(part1(3, 1))
print(part2())

