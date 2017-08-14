#!/usr/bin/python
#code=utf-8

from collections import deque

def test():
    q = deque([])
    q.append("a")
    q.append("ss")
    print "1--", q
    q.pop()
    print "2--", q
    q.appendleft("la")
    q.appendleft("ls")
    print "3--", q
    q.popleft()
    print "4--", q
    return


if __name__ == "__main__":
    test()