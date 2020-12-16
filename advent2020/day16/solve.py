from input import inp
from advent_lib import *

# test_inp = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12"""

test_inp = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

# inp = test_inp

rows = inp.split("\n")
grid = [[x for x in row] for row in rows]

rules = []
mode = 0
my_ticket = None
nearby = []
for line in rows:
    if line.strip() == "":
        mode += 1
        continue
    if mode == 0:
        name = line.split(":")[0]
        r1 = line.split(":")[1].split(" or ")[0]

        l1 = int(r1.split("-")[0])
        u1 = int(r1.split("-")[1])

        r2 = line.split(":")[1].split(" or ")[1]
        l2 = int(r2.split("-")[0])
        u2 = int(r2.split("-")[1])

        rules.append([name, (l1,u1), (l2,u2)])
    elif mode == 1:
        if "your ticket" in line:
            continue
        my_ticket = [int(x) for x in line.split(",")]
    else:
        if "nearby" in line:
            continue
        t = [int(x) for x in line.split(",")]
        nearby.append(t)
print(rules, my_ticket, nearby)
invalid = []
bad_values = []
valid_tickets = []
for t in nearby:
    bad = False
    for val in t:
        valid = False
        for name, (l1,u1), (l2,u2) in rules:
            valid = valid or (l1 <= val and val <= u1) or (l2 <= val and val <= u2)
        if not valid:
            print(f"value {val} in ticket {t} is invalid")
            invalid.append(t)
            bad_values.append(val)
            bad = True
            break
    if not bad:
        valid_tickets.append(t)
    

# print(invalid)
# print(sum(bad_values))
# aoc_submit(sum(bad_values), 1)

labels = []
print(valid)
for i in range(len(my_ticket)):
    values = [t[i] for t in valid_tickets]
    values.append(my_ticket[i])
    print(f"{i} | {values}")
    found = False
    maybe = []
    for name, (l1,u1), (l2,u2) in rules:
        valid = True
        for val in values:
            valid = valid and ((l1 <= val and val <= u1) or (l2 <= val and val <= u2))
        if valid and name not in labels:
            print(f"label for {i} is {name}")
            #labels.append(name)
            maybe.append(name)
            found = True
            #break
    labels.append(maybe)
    if not found:
        print("ERROR BAJBKLASDJFJLAKFJASF")
        break

# solver
final = list(range(len(my_ticket)))
added = []
# for i,s in enumerate(labels):
#     if len(s) == 1:
#         final[i] = s[0]
#         added.append(i)

# print(f"after start | {final}")
while True:
    print(f"loop | {final}")
    for i,s in enumerate(labels):
        if i in added:
            continue

        can_work = []
        for name in s:
            if name not in final:
                can_work.append(name)
        print(f"{i} | {can_work} | {s}")
        if len(can_work) == 1:
            final[i] = can_work[0]
            added.append(i)
    if len(added) == len(final):
        break

print(final)

m = 1
for i,l in enumerate(final):
    if "departure" in l:
        print(l,i, my_ticket[i])
        m *= my_ticket[i]

print(m)