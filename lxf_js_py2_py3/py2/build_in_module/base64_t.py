#!/usr/bin/python
#code=utf-8

import base64

def test():
    #encode/decode
    b = base64.b64encode("binary\x00string")
    print "encode-->", b
    print "decode-->", base64.b64decode(b)

    #urlsafe_b64encode/urlsafe_b64decode
    b2 = "ss"
    print "urlsafe_b64encode-->", b2
    print "urlsafe_b64decode-->", base64.urlsafe_b64decode(b2)
    return


if __name__ == "__main__":
    test()