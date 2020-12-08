from input import x
from advent_lib import *

# x = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

# instrs = x.split("\n")
# ip = 0
# acc = 0
# seen = []

# while True:
#     instr = instrs[ip]
#     print(instr)
#     if ip in seen:
#         break 
#     else:
#         seen.append(ip)
#     op = instr.split(" ")[0]
#     val = instr.split(" ")[1]
#     sign = val[0]
#     val = int(val[1:])

#     if op == "jmp":
#         if sign == "-":
#             ip -=val 
#         else:
#             ip += val
#         continue
#     elif op == "acc":
#         if sign == "-":
#             acc -=val 
#         else:
#             acc += val
#     else:
#         pass
#     ip +=1 
# print(acc)
# aoc_submit(acc, 1)

# x = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

def calculate(instrs):
    ip = 0
    acc = 0
    seen = []

    while True:
        if ip in seen:
            return seen 
        elif ip == len(instrs):
            return acc
        else:
            seen.append(ip)

        instr = instrs[ip]
        #print(instr)
        op = instr.split(" ")[0]
        val = instr.split(" ")[1]
        sign = val[0]
        val = int(val[1:])

        if op == "jmp":
            if sign == "-":
                ip -=val 
            else:
                ip += val
            continue
        elif op == "acc":
            if sign == "-":
                acc -=val 
            else:
                acc += val
        else:
            pass
        ip +=1 
        
instrs = x.split("\n")
looped = calculate(instrs)

for ip in looped:
    instr = instrs[ip]
    #print(instr)
    op = instr.split(" ")[0]
    val = instr.split(" ")[1]
    sign = val[0]
    val = int(val[1:])

    new_instrs = instrs.copy()
    if op == "jmp":
        new_instrs[ip] = "nop +0"
    elif op == "nop":
        new_instrs[ip] = "jmp " + sign + str(val)
    else:
        continue
    print(f"switched {instrs[ip]} to {new_instrs[ip]}")
    x = calculate(new_instrs)
    #print(x)
    try:
        len(x)
    except Exception:
        print("FOUND:", x)
        aoc_submit(x, 2)