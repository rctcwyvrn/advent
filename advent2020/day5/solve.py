from input_file import *

#x = """BFFFBBFRRR"""
ids = []
for seat in x.split("\n"):
    row = 0
    for i,b in enumerate(seat[:-3]):
        if b == "B":
            row += 2**(6-i)
    col = 0
    for i,b in enumerate(seat[-3:]):
        if b == "R":
            col += 2**(2-i)
    #print(row,col, row*8 + col)
    ids.append(row*8 + col)

print(max(ids))

for id in range(max(ids)):
    if id not in ids and id + 1 in ids and id - 1 in ids:
        print(id)