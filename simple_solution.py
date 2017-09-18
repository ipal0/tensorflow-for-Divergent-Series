#!/usr/bin/python3
def f(x):
    from math import sqrt
    return int(sqrt(2*int(x)))

from sys import argv
print(f(argv[1]))
