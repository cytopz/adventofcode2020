#!/usr/bin/env python3

from itertools import combinations

inpt = [int(x) for x in open('input', 'r')]

# part 1
print([num1 * num2 for num1, num2 in combinations(inpt, 2) if num1 + num2 == 2020])

# part 2
print([num1 * num2 * num3 for num1, num2, num3 in combinations(inpt, 3) if num1 + num2 + num3 == 2020])

