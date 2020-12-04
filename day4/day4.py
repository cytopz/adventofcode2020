#!/usr/bin/env python3

from functools import reduce

inpt = [p.split(' ') for p in [x.strip().replace('\n', ' ') for x in open('input', 'r').read().split('\n\n')]]

expected_keys = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
])

validator = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (150 <= int(x[:len(x)-2]) <= 193 if x[len(x)-2:] == 'cm'
                     else 59 <= int(x[:len(x)-2]) <= 76)
                     if x[len(x)-2:] in ['cm', 'in'] else False,
    'hcl': lambda x: len(x) == 7 and x[0] == '#' and
                     reduce(lambda a, b: a and b in '#01234567879abcdef', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9 and all(c.isdigit() for c in x)
}

def parse_pas(pas):
    return {p.split(':')[0]: p.split(':')[1] for p in pas} 

def part1():
    res = []
    for pas in inpt:
        parsed = parse_pas(pas)
        parsed_set = set(parsed.keys())
        if len(expected_keys - parsed_set) == 0:
            res.append(parsed)
    return res

def part2():
    count = 0
    parsed = part1()
    for pas in parsed:
        valid = all(validator[k](pas[k]) for k in pas if k != 'cid')
        count += 1 if valid else 0
    return count

print(len(part1()))
print(part2())
