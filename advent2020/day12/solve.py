from input import inp
from advent_lib import *
from math import cos, sin, pi, atan, sqrt

test_inp = """F10
N3
F7
R90
F11"""

# inp = test_inp

rows = inp.split("\n")
grid = [[x for x in row] for row in rows]

boat_pos = [0,0]

#dir = 0
pos = [10, 1]

for move in rows:
    cmd = move[0]
    dist = int(move[1:])
    #print(dir)
    print("before",boat_pos, pos, move)
    if cmd == "N":
        pos[1] += dist
    elif cmd == "S":
        pos[1] -= dist
    elif cmd == "W":
        pos[0] -= dist
    elif cmd == "E":
        pos[0] += dist
    elif cmd == "F":
        # boat_pos[0] += cos(dir * pi / 180) * dist
        # boat_pos[1] += sin(dir * pi / 180) * dist
        #print(pos, dir)

        boat_pos[0] = boat_pos[0] + pos[0] * dist
        boat_pos[1] = boat_pos[1] + pos[1] * dist
    
    elif cmd == "R":
        rad = -1 * dist * pi / 180
        c = cos(rad)
        s = sin(rad)
        x = pos[0]
        y = pos[1]
        pos[0] = c * x - s * y
        pos[1] = s * x + c * y
        #dir = (dir - dist) % 360 

        # r = sqrt(pos[0]**2 + pos[1]**2)
        # dir = atan(pos[1] / pos[0])
        # new = (dir - dist * pi / 180) % (2*pi)
        # pos[0] = cos(new) * r
        # pos[1] = sin(new) * r
        #print(f"{r}, {dir * 180 / pi}, {new* 180 / pi}")
    elif cmd == "L":
        rad = dist * pi / 180
        c = cos(rad)
        s = sin(rad)
        x = pos[0]
        y = pos[1]
        pos[0] = c * x - s * y
        pos[1] = s * x + c * y

        #dir = (dir + dist) % 360

        # r = sqrt(pos[0]**2 + pos[1]**2)
        # dir = atan(pos[1] / pos[0])
        # new = (dir + dist * pi / 180) % (2*pi)
        # pos[0] = cos(new) * r
        # pos[1] = sin(new) * r
        #print(f"{r}, {dir * 180 / pi}, {new* 180 / pi}")
    else:
        print("wtf")
    print("after",boat_pos, pos)
print(boat_pos, pos)

mh_dist = abs(round(boat_pos[0])) + abs(round(boat_pos[1]))
print(mh_dist)

#aoc_submit(mh_dist, 1)
aoc_submit(mh_dist, 2)