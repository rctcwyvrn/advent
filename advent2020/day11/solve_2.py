from input import inp 
from advent_lib import *

state = inp.split("\n")

num_rows = len(state)
num_cols = len(state[0])

def limit(row, col, row_dir, col_dir):
    res = True
    if row_dir == "up":
        res = res and row >= 0
    elif row_dir == "down":
        res = res and (row < num_rows)

    if col_dir == "left":
        res = res and col >= 0
    elif col_dir == "right":
        res = res and (col < num_cols)
    
    return res

def walk(state, start_row, start_col, row_dir= None, col_dir= None):
    row = start_row 
    col = start_col
    while limit(row, col, row_dir, col_dir):
        #print(row, col ,start_row, start_col, num_rows, num_cols, row_dir, col_dir, limit(row, col, row_dir, col_dir))
        x = state[row][col]
        if x != ".":
            return x 
        
        if row_dir == "up":
            row -= 1
        if row_dir == "down":
            row += 1
        if col_dir == "left":
            col -= 1
        if col_dir == "right":
            col += 1
    return ""

def adjacent(state, start_row, start_col):
    adj = ""
    if start_row > 0:
        adj += walk(state, start_row - 1, start_col, row_dir="up")
    if start_row < num_rows - 1:
        adj += walk(state, start_row + 1, start_col, row_dir="down")
    
    if start_col > 0:
        adj += walk(state, start_row, start_col - 1, col_dir="left")
    if start_col < num_cols - 1:
        adj += walk(state, start_row, start_col + 1, col_dir="right")
    

    if start_row > 0 and start_col > 0:
        adj += walk(state, start_row - 1, start_col - 1, row_dir="up", col_dir="left")
    if start_row < num_rows - 1 and start_col > 0:
        adj += walk(state, start_row + 1, start_col - 1, row_dir="down", col_dir="left")
    
    if start_row > 0 and start_col < num_cols - 1:
        adj += walk(state, start_row - 1, start_col + 1, row_dir="up", col_dir="right")
    if start_row < num_rows - 1 and start_col < num_cols - 1:
        adj += walk(state, start_row + 1, start_col + 1, row_dir="down", col_dir="right")


    return adj

def print_s(state):
    for row in state:
        print(row)

# test = [["a","b","c"], ["d","e","f"], ["g","h","i"]]
# print_s(test)
# print(adjacent(test, 1, 1))
# print(adjacent(test, 0, 0))

def step(state):
    new_state = state.copy()
    for l in range(len(state)):
        for s in range(len(state[l])):
            seat = state[l][s]
            adj = adjacent(state,l,s)
            if seat == "L":
                if not "#" in adj:
                    new_state[l]  = new_state[l][:s] + "#" + new_state[l][s+1:]
            elif seat == "#":
                if sum([1 if c == "#" else 0 for c in adj]) >= 5:
                    new_state[l] = new_state[l][:s] + "L" + new_state[l][s+1:]
    return new_state 

last = state
while True:
    last = state
    state = step(state)
    if state == last:
        break

total = 0
for a in state:
    for b in a:
        if b == "#":
            total+=1

aoc_submit(total,2)