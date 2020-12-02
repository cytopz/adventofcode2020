#!/usr/bin/env python3

inpt = [x.strip("\n") for x in open("input", "r")]

def parse_input():
    res = []
    for line in inpt:
        parsed = {}
        cond, pwd = line.split(": ")
        cond = cond.split(" ")
        parsed['pwd'] = pwd
        parsed['cond'] = {
                'min': int(cond[0].split("-")[0]),
                'max': int(cond[0].split("-")[1]),
                'char': cond[1],
        }
        res.append(parsed)
    return res

def part1(parsed):
    return len([1 for item in parsed if item['cond']['min'] <=
        item['pwd'].count(item['cond']['char']) <= item['cond']['max']])

def part2(parsed):
    return len([1 for item in parsed if (item['pwd'][item['cond']['min']-1] == item['cond']['char'])
            ^ (item['pwd'][item['cond']['max']-1] == item['cond']['char'])])

parsed = parse_input()
print(part1(parsed))
print(part2(parsed))

