#!/usr/bin/python
#code=utf-8

import hashlib

def test():
    #md5
    md5 = hashlib.md5()
    md5.update("123456")
    print md5.hexdigest()

    return


if __name__ == "__main__":
    test()