from random import choice
from sys import argv
import time

nitrogen_bases = ["A", "T", "C", "G"]


def random_base(num):
    bases = []
    for i in range(num):
        base = choice(nitrogen_bases)
        bases.append(base)
    return bases


def comp_base(bases):
    _strand = ""
    for i in range(len(bases)):
        base = bases[i]
        if base == "A":
            _strand = _strand + base + " -- T\n"

        elif base == "T":
            _strand = _strand + base +" -- A\n"

        elif base == "C":
            _strand = _strand + base +" -- G\n"

        elif base == "G":
            _strand = _strand + base +" -- C\n"
    return _strand

def make_strand(num=23):
    _strand = comp_base( random_base(num) )
    print(_strand)


try:
    make_strand(int(argv[1]))
except Exception as e:
    print(e)
    make_strand()
