#!/usr/bin/env python3

if __name__ == "__main__":
    l = [int(line.strip()) for line in open('input.txt').readlines()]
    prev = -1
    count = 0
    for a, b, c in zip(l, l[1:], l[2:]):
        if prev != -1:
            if prev < a+b+c:
                count += 1
        prev = a+b+c
    print(count)
