from __future__ import print_function
import sys

ans = []

def syn(fac, _iter):
    print("#"*10)
    print(int(_iter[0]))
    lastval = int(_iter[0])
    for obj in _iter[1:]:
        obj = int(obj)
        if (lastval*fac)+obj == 0 and obj == _iter[-1]:
            print("zero")
        else:
            print((lastval*fac)+obj)
        lastval = (lastval*fac)+obj
        
syn(int(sys.argv[1]), sys.argv[2:])
