#!/usr/bin/env python3

import sys
from itertools import cycle

def preprocess(data):
    return list(map(int, data))

def part1(data):
    return sum(data)


def part2(data):
    freqs = {0: 1}
    acc = 0

    for num in cycle(data):
        acc += num

        if freqs.get(acc, None):
            return acc

        freqs[acc] = 1
