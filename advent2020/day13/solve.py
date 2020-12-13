from input import inp
from advent_lib import *

test_inp = """939
7,13,x,x,59,x,31,19"""

# inp = test_inp

rows = inp.split("\n")
grid = [[x for x in row] for row in rows]

#start = int(rows[0])
#busses = []
# for x in rows[1].split(","):
#     # if x != "x":
#     #     busses.append(int(x))

# print(busses, [b - start % b for b in busses])
# t = min([b - start % b for b in busses])
# val = busses[[b - start % b for b in busses].index(t)] * t
# print(val)
# aoc_submit(val, 1)

#N = 1
busses = []
offsets = []
for i, bus in enumerate(rows[1].split(",")):
    if bus != "x":
        busses.append(int(bus))
        #N *= int(bus)
        offsets.append(int(bus) - i)

# t such that t % busses[0] == 0 and t % busses[i] = i

# rosetta code chinese remainder theorem

# Python 3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
x =  chinese_remainder(busses, offsets)

print(x)
# aoc_submit(x, 2) 

