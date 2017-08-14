#!/usr/bin/python
#code=utf-8

from collections import Counter

def test():
    c = Counter()
    for ch in "programming":
        c[ch] += 1

    print c
    return


if __name__ == "__main__":
    test()