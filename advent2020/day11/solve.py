from input import inp
from advent_lib import *

# inp = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

state = inp.split("\n")

# def adjacent(l, s):
#     if l == 0:
#         if s == 0:
#             return state[l][s + 1] + state[l + 1][s]  + state[l + 1][s + 1]
#         if s == len(state[0]) - 1:
#             return state[l][s - 1] + state[l + 1][s - 1]  + state[l + 1][s]
#         return state[l][s - 1] + state[l][s + 1] + state[l + 1][s - 1]  + state[l + 1][s]  + state[l + 1][s + 1]
#     if l == len(state) - 1:
#         if s == 0:
#             return state[l][s + 1] + state[l - 1][s]  + state[l - 1][s + 1]
#         if s == len(state[0]) - 1:
#             return state[l][s - 1] + state[l - 1][s - 1]  + state[l - 1][s]
#         return state[l][s - 1] + state[l][s + 1] + state[l - 1][s - 1]  + state[l - 1][s]  + state[l - 1][s + 1]
#     if s == 0:
#         return state[l][s + 1] + state[l - 1][s]  + state[l - 1][s + 1] + state[l + 1][s]  + state[l + 1][s + 1]
#     if s == len(state[0]) - 1:
#         return state[l][s - 1] + state[l - 1][s]  + state[l - 1][s - 1] + state[l + 1][s]  + state[l + 1][s - 1]
#     return state[l][s - 1] + state[l][s + 1] + state[l - 1][s - 1]  + state[l - 1][s]  + state[l - 1][s + 1] + state[l + 1][s - 1]  + state[l + 1][s]  + state[l + 1][s + 1]

def adjacent(state, l,s):
    seen = []
    if s < len(state[0]) - 1:
        x = s + 1
        while x < len(state[0]):
            if state[l][x] != ".":
                seen.append(state[l][x])
                break
            x+= 1
    if s > 0:
        x = s - 1
        while x >= 0:
            if state[l][x] != ".":
                seen.append(state[l][x])
                break
            x-= 1
    if l < len(state) - 1:
        y = l+ 1
        while y < len(state):
            if state[y][s] != ".":
                seen.append(state[y][s])
                break
            y+= 1
    if l > 0:
        y = l - 1
        while y >= 0:
            if state[y][s] != ".":
                seen.append(state[y][s])
                break
            y-= 1
    if l > 0 and s > 0:
        x = l - 1 #i fucked up the namiing
        y = s - 1
        while x >= 0 and y >= 0:
            if state[x][y] != ".":
                seen.append(state[x][y])
                break
            x -=1
            y-=1 
    if l > 0 and s < len(state[0]) - 1:
        x = l - 1 #i fucked up the namiing
        y = s + 1
        while x >= 0 and y < len(state[0]):
            if state[x][y] != ".":
                seen.append(state[x][y])
                break
            x-= 1
            y += 1
    if l < len(state) -1 and s > 0:
        x = l + 1 #i fucked up the namiing
        y = s  - 1
        while x < len(state) and y>= 0:
            if state[x][y] != ".":
                seen.append(state[x][y])
                break
            x += 1
            y-= 1
    if l < len(state) -1 and s <len(state[0]) -1:
        x = l + 1#i fucked up the namiing
        y = s + 1
        while x < len(state) and y < len(state):
            if state[x][y] != ".":
                seen.append(state[x][y])
                break
            x += 1
            y += 1
    return "".join(seen)

def step(state):
    new_state = state.copy()
    for l in range(len(state)):
        for s in range(len(state[l])):
            seat = state[l][s]
            #print(seat)
            adj = adjacent(state,l,s)
            #print(l,s,adj)
            if seat == "L":
                if not "#" in adj:
                    #print("changing")
                    new_state[l]  = new_state[l][:s] + "#" + new_state[l][s+1:]
            elif seat == "#":
                #if sum([1 if c == "#" else 0 for c in adj]) >= 4:
                if sum([1 if c == "#" else 0 for c in adj]) >= 5:
                    #print("changing")
                    new_state[l] = new_state[l][:s] + "L" + new_state[l][s+1:]
    return new_state 
def print_s(state):
    for row in state:
        print(row)

last = state
print_s(state)
print("---")
while True:
    last = state
    state = step(state)
    print_s(state)
    print("---")
    if state == last:
        break

# anss = [
#     """#.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##""",
# """#.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#""",
# """#.L#.##.L#
# #L#####.LL
# L.#.#..#..
# ##L#.##.##
# #.##.#L.##
# #.#####.#L
# ..#.#.....
# LLL####LL#
# #.L#####.L
# #.L####.L#""",
# """#.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##LL.LL.L#
# L.LL.LL.L#
# #.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLL#.L
# #.L#LL#.L#""",
# """#.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.#L.L#
# #.L####.LL
# ..#.#.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#""",
# """#.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.LL.L#
# #.LLLL#.LL
# ..#.L.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#""",
# ]
# for ans in anss:
#     ans = ans.split("\n")
#     last = state
#     state = step(state)
#     print_s(state)
#     print("---")


#     for i in range(len(state)):
#         for j in range(len(state[0])):
#             if state[i][j] != ans[i][j]:
#                 print(i,j, "differ", state[i][j] , ans[i][j])



total = 0
for a in state:
    for b in a:
        if b == "#":
            total+=1

# aoc_submit(total,1)
aoc_submit(total,2)
