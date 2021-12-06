#!/usr/bin/env python3

import copy
import sys

def get_check_val(values, idx=0):
    bits = tuple(l[idx] for l in values)
    if bits.count('1') < bits.count('0'):
        return "0", "1"
    else:
        return "1", "0"


def check_values(values: list, check_idx: int):
    counter = 0
    fresh_values = copy.deepcopy(values)

    while len(fresh_values) != 1:
        check_bit = get_check_val(fresh_values, idx=counter)
        fresh_values = [entry for entry in fresh_values if entry[counter] == check_bit[check_idx]]
        counter += 1

    return fresh_values.pop()


def main(file_path: str):
    lines = [line.rstrip() for line in open(file_path).readlines()]
    o2_rating = check_values(lines, 0)
    co2_rating = check_values(lines, 1)
    print(o2_rating, co2_rating, int(o2_rating, 2)*int(co2_rating, 2))


if __name__ == "__main__":
    main(sys.argv[1])
