#!/usr/bin/python
#code=utf-8

from collections import namedtuple

def test():
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    print "x =", p.x
    print "y =", p.y
    return


if __name__ == "__main__":
    test()