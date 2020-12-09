from input import x
from advent_lib import *


def check(buf, val):
    for x in buf:
        for y in buf:
            if x + y == val:
                return True
    return False

# buf = []
# ctr = 0
# for line in x.split("\n"):
#     if ctr > 25:
#         if not check(buf, int(line)):
#             print(int(line))
#             aoc_submit(int(line), 1)
#         buf[ctr % 25] = int(line) # new 
#     else:
#         buf.append(int(line))

#     ctr +=1 

invalid = 15353384

sums = []
for line in x.split("\n"):
    for s in sums:
        if sum(s) == invalid:
            print(min(s) + max(s))
            aoc_submit(min(s) + max(s), 2)
            break
        else:
            s.append(int(line))
    sums.append([int(line)])