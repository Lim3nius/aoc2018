#!/usr/bin/env python3

import re

def preprocess(data):
    new_data = []
    for record in data:
        new_data.append(list(map(int, re.findall(r'\d+', record))))
    return new_data


def assign_claims(data):
    grid = {}

    for record in data:
        id, x, y, width, height = record

        for i in range(width):
            for j in range(height):

                if not grid.get((x+i, y+j)):
                    grid[(x+i, y+j)] = []
                grid[(x+i, y+j)].append(id)

    return grid


def part1(data):
    claims = assign_claims(data)
    return sum([1 for x in claims.values() if len(x) > 1])


def part2(data):
    ids = {id : w*h for id, _, _, w, h in data}
    claims = assign_claims(data)
    free = [x[0] for x in claims.values() if len(x) == 1]

    helper = {}
    for id in free:
        if not helper.get(id):
            helper[id] = 0

        helper[id] += 1

    for id, area in helper.items():
        if ids.get(id, 0) == area:
            return id
