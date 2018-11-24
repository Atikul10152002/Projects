#!/usr/bin/env python3
import time
from concurrent.futures import ThreadPoolExecutor

lli = list(range(10000))

def _print(_input):
    print(_input)

# starting_time = time.time()
# with Exec(max_workers=2) as executor:
#     executor.map(_print, lli)

# # list(map(_print, lli))

# print("Time:: ",time.time()-starting_time)
# # Time::  1.1296241283416748

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(_print, lli)
    print(future.result())
