#!/usr/bin/env python3

from functools import reduce

# part1
inpt = [l.replace('\n', '') for l in [x.strip() for x in open('input', 'r').read().split('\n\n')]]
print(sum([len(set(q)) for q in inpt]))

# part2
inpt = [l.split('\n') for l in [x.strip() for x in open('input', 'r').read().split('\n\n')]]
print(sum([len(reduce(lambda a, b: set(a) & set(b), g)) for g in inpt]))

