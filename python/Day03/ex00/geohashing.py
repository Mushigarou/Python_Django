import antigravity
import sys

def hashLocation():
    s = antigravity.geohash(3754, -1251, b'2015-05-26-158.68')
    print(s)

if __name__ == "__main__":
    """ TODO: Ask User for input """
    hashLocation()