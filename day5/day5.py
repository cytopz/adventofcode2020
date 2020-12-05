#!/usr/bin/env python3

inpt = [x.strip() for x in open('input', 'r')]

def part1():
    ids = []
    for l in inpt:
        min = row = 0
        max = 127
        range = max - min + 1
        for c in l[:7]:
            range //=  2
            if c == 'F':
                row = max = max - range
            else:
                row = min = min + range
        min = col = 0
        max = 7
        range = max - min + 1
        for c in l[7:]:
            range //= 2
            if c == 'L':
                col = max = max - range
            else:
                col = min = min + range
        ids.append(row * 8 + col)
    return ids

def part2():
    ids = part1()
    return [s for s in range(min(ids), max(ids)) if s not in ids]

print(max(part1()))
print(part2())
