#!/usr/bin/env python3

import sys

def main(file_path: str):
    lines = [line.rstrip() for line in open(file_path).readlines()]
    gamma = 0
    epsilon = 0

    for bits in zip(*lines):
        gamma = (gamma << 1) + int(bits.count('1') > bits.count('0'))
        epsilon = (epsilon << 1) + int(bits.count('1') < bits.count('0'))

    print(f"gamma = {gamma}, epsilon = {epsilon}")
    print(gamma * epsilon)

if __name__ == "__main__":
    main(sys.argv[1])
