#!/usr/bin/env python3

import argparse
import solutions
import sys


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('day', type=int)
    return p.parse_args()


def main():
    args = parse_args()
    day = args.day

    # get input for day_X
    try:
        data = open('inputs/{}.txt'.format(day), 'r').readlines()
    except Exception as e:
        print('You forget your input file')

    try:
        module = solutions.day_to_module[day]
    except Exception as e:
        print('Unregistered module')
        sys.exit(1)

    data = module.preprocess(data)

    print('Day {}, part 1 solution -> {}'.format(day, module.part1(data)))
    print('Day {}, part 2 solution -> {}'.format(day, module.part2(data)))

if __name__ == '__main__':
    main()
