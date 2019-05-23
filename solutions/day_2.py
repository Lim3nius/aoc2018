#!/usr/bin/env python3

from itertools import combinations


def preprocess(data):
    return data


def code_to_histogram(code):
    return { c : code.count(c) for c in set(code)}


def part1(data):
    double_letters = 0
    triple_letters = 0

    for code in data:
        hist = {c : code.count(c) for c in set(code)} # converts str to histogram of letter usage
        doubles = (sum(filter(lambda x: x == 2, hist.values())) > 1)
        triples = (sum(filter(lambda x: x == 3, hist.values())) > 1)

        double_letters += doubles
        triple_letters += triples

    return double_letters * triple_letters


def part2(data):
    one_letter_diff = lambda s1, s2: len([a for a, b in zip(s1, s2) if a != b])

    # combinations take from input list always X elements, compute 1 letter diff between them
    # if == 1, then extract common letters into string
    sol = [''.join([a for a, b in zip(s1, s2)]) for s1, s2 in combinations(data, 2) if one_letter_diff(s1, s2) == 1]
    return sol[0]
