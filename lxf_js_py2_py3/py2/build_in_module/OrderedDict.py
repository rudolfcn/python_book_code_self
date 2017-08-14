#!/usr/bin/python
#code=utf-8

from collections import OrderedDict

def test():
    d = OrderedDict([('a',1), ("b", 2), ("c", 3)])   #set default value
    print  d

    d2 = OrderedDict()
    d2["c"] = 2
    d2['s'] = 4
    print d2.keys()
    return


if __name__ == "__main__":
    test()