#!/usr/bin/env python3

inpt = [x.strip() for x in open('input', 'r')]

def run(prog):
    success = True
    seen = set()
    acc = 0
    i = 0
    while i < len(prog):
        ins, val = prog[i].split(' ')
        val = int(val)
        if i in seen:
            success = False
            # print(acc) part1
            break
        seen.add(i)
        if ins == 'acc':
            acc += val
        elif ins == 'jmp':
            i += val
            continue
        i += 1
    return acc if success else False

def part2():
    for i, ins in enumerate(inpt):
        new_inpt = inpt.copy()
        if ins.startswith('nop'):
            new_inpt[i] = new_inpt[i].replace('nop', 'jmp')
        elif ins.startswith('jmp'):
            new_inpt[i] = new_inpt[i].replace('jmp', 'nop')
        res = run(new_inpt)
        if res:
            return res

# run(inpt) part1
print(part2())
