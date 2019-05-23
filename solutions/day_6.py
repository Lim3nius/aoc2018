#!/usr/bin/env python3

import numpy as np

def preprocess(data):
    ndata = []
    for record in data:
        x, y = map(int, record.split(', '))
        ndata.append((x, y))
    return ndata


def l1_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bounding_box(data):
    mins = [min(data, key=lambda tup: tup[0])[0], min(data, key=lambda tup: tup[1])[1]]
    maxs = [max(data, key=lambda tup: tup[0])[0], max(data, key=lambda tup: tup[1])[1]]
    return mins, maxs


def part1(data):
    mins, maxs = bounding_box(data)
    grid = {}
    infinite_arrays = set()
    # compute l1 distances of all points
    xs = list(range(mins[0], maxs[0]))
    ys = list(range(mins[1], maxs[1]))
    for pt in [(x, y) for x in xs for y in ys]:
        distances = [(c, l1_dist(*c, *pt)) for c in data]
        center, dist = min(distances, key=lambda tup: tup[1])

        if pt[0] in [mins[0], maxs[0]] or pt[1] in [mins[1], maxs[1]]:
            infinite_arrays.add(center)

        if len([1 for c, d in distances if d == dist]) > 1:
            grid[pt] = (-1, -1)
        else:
            grid[pt] = (center, dist)


    closed_centers = {c : 0 for c in data if c not in infinite_arrays}
    for _, tup in grid.items():
        if tup[0] in closed_centers.keys():
            closed_centers[tup[0]] += 1

    return max(closed_centers.items(), key=lambda tup: tup[1])[1]

def part2(data):
    mins, maxs = bounding_box(data)
    region_size = 0
    # compute l1 distances of all points
    xs = list(range(mins[0], maxs[0]))
    ys = list(range(mins[1], maxs[1]))
    for pt in [(x, y) for x in xs for y in ys]:
        distances = [l1_dist(*c, *pt) for c in data]
        if sum(distances) < 10000:
            region_size += 1

    return region_size
