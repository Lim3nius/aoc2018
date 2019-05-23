#!/usr/bin/env python3

import string

def preprocess(data):
    return list(data[0].strip())


def reaction(a, b):
    if b.swapcase() == a:
        return True
    return False


def part1(data):
    return len(reduce_str(data))


def reduce_str(data):
    new_str = [' ']
    for c in data:
        if reaction(new_str[-1], c):
            new_str.pop()
        else:
            new_str.append(c)
    new_str.pop(0)
    return new_str


def part1_old_version(data):
    reacted = True
    while reacted:
        reacted = False
        i = 1
        while i < len(data):
            if reaction(data[i -1], data[i]):
                data.pop(i -1)
                data.pop(i -1)
                reacted = True
                continue
            i += 1

    return len(data)


def part2(data):
    polymer = reduce_str(data)
    versions = {}

    for c in string.ascii_lowercase:
        versions[c] = len(reduce_str([e for e in polymer if e.lower() != c]))

    _, m = min(versions.items(), key=lambda tup: tup[1])
    return m
