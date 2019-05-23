#!/usr/bin/env python3

from collections import defaultdict

def preprocess(data):
    ndata = defaultdict(list)
    for record in data:
        tmp = record.split(' ')
        ndata[tmp[1]].extend([tmp[7]])
    return ndata


def part1(data):
    deps_dict = defaultdict(set)
    for k, vls in data.items():
        for v in vls:
            deps_dict[v].add(k)

    dependant_letters = set()
    free_letters = set()
    final_sequence = []
    for vals in data.values():
        dependant_letters.update(*vals)

    all_letters = dependant_letters.union({k for k in data.keys()})
    start_letters = all_letters - dependant_letters

    while start_letters:
        letter = sorted(start_letters)[0]
        free_letters.add(letter)
        final_sequence.append(letter)
        start_letters.remove(letter)

        for l in data[letter]:
            if deps_dict[l].issubset(free_letters):
                start_letters.add(l)

        del data[letter]

    return ''.join(final_sequence)



def part2(data):
    deps_dict = defaultdict(set)
    for k, vls in data.items():
        for v in vls:
            deps_dict[v].add(k)

    dependant_letters = set()
    free_letters = set()
    final_sequence = []
    for vals in data.values():
        dependant_letters.update(*vals)

    all_letters = dependant_letters.union({k for k in data.keys()})
    start_letters = all_letters - dependant_letters
    free_workers = [0 for _ in range(5)]
    working_workers = []
    time = 0
    letter_penalty = lambda l: 61 + ord(l.upper()) - ord('A')

    while start_letters or working_workers:
        if working_workers:
            worker = working_workers.pop(0)
            free_workers.append(0)
            letter = worker[1]
            free_letters.add(letter)
            final_sequence.append(letter)

            for l in data[letter]:
                if deps_dict[l].issubset(free_letters):
                    start_letters.add(l)

            del data[letter]

        while free_workers and start_letters:
            letter = sorted(start_letters)[0]
            working_workers.append([time + letter_penalty(letter), letter])
            free_workers.pop()
            start_letters.remove(letter)

        if working_workers:
            next_event = min(working_workers, key=lambda tup: tup[0])[0]
            diff = next_event - time
            time += diff

    return time
