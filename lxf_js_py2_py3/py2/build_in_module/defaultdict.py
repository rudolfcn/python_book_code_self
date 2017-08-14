#!/usr/bin/python
#code=utf-8

from collections import defaultdict

def test():
    d = defaultdict(lambda:"N/A")   #set default value
    d["key1"] = "s1"
    print "key1 =", d["key1"]   #exist, return real value
    print "key2 =", d["key2"]   #not exist, return default value
    return


if __name__ == "__main__":
    test()