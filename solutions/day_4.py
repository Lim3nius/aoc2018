#!/usr/bin/env python3

import re
from collections import defaultdict

def preprocess(data):
    data.sort()
    return data_parse(data)


def data_parse(data):
    guards = defaultdict(list)
    gid = None
    sleep_start = None
    for record in data:
        time = re.search(r'[0-9]{2}:[0-9]{2}', record).group(0)
        _, minute = map(int, time.split(':'))
        _, info = record.split(']')

        if 'falls' in info:
            sleep_start = minute

        elif 'wakes' in info:
            guards[gid].extend(list(range(sleep_start, minute)))

        elif 'Guard' in info:
            gid = int(re.search(r'[0-9]+', info).group(0))

    return guards


def part1(data):
    schedule = data

    sleep_length = {gid : len(times) for gid, times in schedule.items()}
    longest_sleeper, _ = max(sleep_length.items(), key=lambda tup: tup[1])

    histogram = {elem: schedule[longest_sleeper].count(elem) for elem in set(schedule[longest_sleeper])}

    minute, _ = max(histogram.items(), key=lambda tup: tup[1])
    return minute * longest_sleeper


def part2(data):
    schedule = data
    sleep_histogram = {gid: {el: sleeps.count(el) for el in set(sleeps)}  for gid, sleeps in schedule.items()}

    frequent_mins = {gid: max(times.items(), key=lambda tup: tup[1]) for gid, times in sleep_histogram.items()}

    sleeper, tup = max(frequent_mins.items(), key=lambda tup: tup[1][1])
    minute, _ = tup
    return sleeper * minute
