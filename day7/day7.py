#!/usr/bin/env python3

inpt = [x.strip() for x in open('input', 'r')]
rules = {}
for r in inpt:
        p, c = r.split(' bags contain ')
        if 'no' in c:
            continue
        c = [x.strip('s') for x in c[:-1].split(', ')]
        c = {x[2:-4]: int(x[:-len(x)+1]) for x in c}
        rules[p] = c

def find_contains(col):
    return [c for c in rules if set(col) & set(rules[c].keys())]

def count(k):
    tot = 0
    if k in rules:
        for ck, c in rules[k].items():
            tot += (c * (1+count(ck)))
    return tot

def part1():
    c = find_contains(['shiny gold'])
    res = []
    while c:
        res += c
        c = find_contains(list(set(c)))
    return set(res)

def part2():
    cur = rules['shiny gold']
    tot = 0
    for k, c in cur.items():
        tot += (c* (1+count(k)))
    return tot
        
print(len(part1()))
print(part2())

