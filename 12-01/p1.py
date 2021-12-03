#!/usr/bin/env python3

if __name__ == "__main__":
    inc_count = 0
    l = [int(line.strip()) for line in open('input.txt').readlines()]
    for a, b in zip(l, l[1:]):
        if a < b:
            inc_count += 1
    print(inc_count)
